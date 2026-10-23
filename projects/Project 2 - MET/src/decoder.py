"""Stimulus decoder -- written by the previous intern.

    "Trained on the visual recordings (grating / face / house).
     Accuracy: 100 %. Should work on any recording from our 40-channel array,
     just call ``load_pretrained()`` and ``predict()``."

The model is a multiclass perceptron: one weight vector per class, the class
with the highest score wins, and weights are only updated on mistakes.

Its parameters are shipped in ``models/pretrained_decoder.safetensors``. safetensors is the
standard format to share model weights: an 8-byte header length, a JSON header (tensor names,
shapes, types, and a free-text "model card" in ``__metadata__``), then the raw numbers. It is
simple enough to be read and written here with NumPy only.
"""

import json
import struct
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent.parent   # the project folder
MODEL_PATH = HERE / "models" / "pretrained_decoder.safetensors"

_DTYPES = {"F64": np.float64, "F32": np.float32, "I64": np.int64, "I32": np.int32}


def write_safetensors(path, tensors, metadata=None):
    """Write a dict of NumPy arrays (and a dict of strings) to a .safetensors file."""
    header, chunks, offset = {}, [], 0
    for name, array in tensors.items():
        array = np.ascontiguousarray(array, dtype=np.float64)
        data = array.astype("<f8").tobytes()
        header[name] = {"dtype": "F64", "shape": list(array.shape), "data_offsets": [offset, offset + len(data)]}
        chunks.append(data)
        offset += len(data)
    if metadata:
        header["__metadata__"] = {k: str(v) for k, v in metadata.items()}
    head = json.dumps(header, separators=(",", ":")).encode("utf-8")
    head += b" " * (-len(head) % 8)          # pad the header to a multiple of 8 bytes
    with open(path, "wb") as f:
        f.write(struct.pack("<Q", len(head)) + head + b"".join(chunks))


def read_safetensors(path):
    """Read a .safetensors file: returns (dict of NumPy arrays, dict of metadata strings)."""
    raw = Path(path).read_bytes()
    n = struct.unpack("<Q", raw[:8])[0]
    header = json.loads(raw[8:8 + n])
    metadata = header.pop("__metadata__", {})
    body = raw[8 + n:]
    tensors = {}
    for name, info in header.items():
        start, end = info["data_offsets"]
        dtype = np.dtype(_DTYPES[info["dtype"]]).newbyteorder("<")
        tensors[name] = np.frombuffer(body[start:end], dtype=dtype).reshape(info["shape"]).astype(dtype.type)
    return tensors, metadata


def print_model_card(path=MODEL_PATH):
    """Print what a model file declares about itself, and the shape of each tensor."""
    tensors, metadata = read_safetensors(path)
    print(f"{Path(path).name}")
    for key, value in metadata.items():
        print(f"  {key:22s} {value}")
    print("  tensors:")
    for name, array in tensors.items():
        print(f"    {name:6s} shape {array.shape}")


class StimulusDecoder:
    def __init__(self, n_features=40, n_classes=3, label_names=None):
        self.W = np.zeros((n_classes, n_features))
        self.b = np.zeros(n_classes)
        self.mu = np.zeros(n_features)
        self.sigma = np.ones(n_features)
        self.label_names = label_names

    def features(self, spikes):
        """spikes: (n_trials, n_neurons, n_bins) -> (n_trials, n_neurons)."""
        counts = spikes.sum(axis=2)  # spike count of each neuron in the trial
        return (counts - self.mu) / self.sigma

    def scores(self, spikes):
        return self.features(spikes) @ self.W.T + self.b

    def predict(self, spikes):
        return np.argmax(self.scores(spikes), axis=1)

    def predict_names(self, spikes):
        return np.asarray(self.label_names)[self.predict(spikes)]

    def fit(self, spikes, labels, epochs=20, lr=0.1, seed=0):
        counts = spikes.sum(axis=2)
        self.mu = counts.mean(axis=0)
        self.sigma = counts.std(axis=0) + 1e-8
        X = self.features(spikes)
        rng = np.random.default_rng(seed)
        for _ in range(epochs):
            for k in rng.permutation(len(X)):
                pred = np.argmax(self.W @ X[k] + self.b)
                if pred != labels[k]:
                    self.W[labels[k]] += lr * X[k]
                    self.b[labels[k]] += lr
                    self.W[pred] -= lr * X[k]
                    self.b[pred] -= lr
        return self

    def accuracy(self, spikes, labels):
        return float(np.mean(self.predict(spikes) == labels))

    def save(self, path=MODEL_PATH, **card):
        metadata = {"model": "StimulusDecoder, multiclass perceptron on standardized spike counts",
                    "classes": ",".join(self.label_names), **card}
        write_safetensors(path, {"W": self.W, "b": self.b, "mu": self.mu, "sigma": self.sigma}, metadata)


def load_pretrained(path=MODEL_PATH):
    tensors, metadata = read_safetensors(path)
    names = metadata["classes"].split(",")
    dec = StimulusDecoder(n_features=tensors["W"].shape[1], n_classes=len(names), label_names=names)
    dec.W, dec.b, dec.mu, dec.sigma = tensors["W"], tensors["b"], tensors["mu"], tensors["sigma"]
    return dec


def train_intern_model():
    """How the intern produced the model file: train on the visual recordings, report the training accuracy."""
    from src.spikes import load_dataset

    spikes, labels, names, _ = load_dataset("visual_3stim")
    dec = StimulusDecoder(label_names=names)
    dec.fit(spikes, labels)
    acc = dec.accuracy(spikes, labels)
    print(f"Accuracy: {100 * acc:.1f} %")
    dec.save(author="previous intern", trained_on="visual_3stim", reported_accuracy=f"{100 * acc:.0f} %")
    print(f"Saved the model to {MODEL_PATH}")


if __name__ == "__main__":
    train_intern_model()
