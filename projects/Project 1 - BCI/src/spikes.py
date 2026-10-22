"""Small helpers for the project: loading, previewing and plotting spike trains.

The recordings come as CSV files in ``data/``, next to this file (open them in any spreadsheet
or text editor, see ``data/README.md``):

    datasets.csv            one row per dataset: number of trials and neurons, duration, resolution
    <name>_trials.csv       one row per trial: trial, label, label_name
    <name>_spikes.csv       one row per spike: trial, neuron, time_ms
"""

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def read_csv(path):
    """Read a CSV file into a list of dictionaries, one per row (all values are strings)."""
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def dataset_info(name):
    """The row of ``datasets.csv`` describing one dataset."""
    for row in read_csv(DATA_DIR / "datasets.csv"):
        if row["dataset"] == name:
            return row
    raise ValueError(f"unknown dataset {name!r}")


def preview(name, n=5):
    """Print the description of a dataset and the first lines of its two CSV files."""
    info = dataset_info(name)
    print(f"{name}: {info['description']}")
    print(f"  {info['n_trials']} trials, {info['n_neurons']} neurons, {info['duration_ms']} ms per trial, "
          f"{info['bin_ms']} ms resolution, stimulus onset: {info['stimulus_onset_ms'] or 'none'}")
    for suffix in ("trials", "spikes"):
        path = DATA_DIR / f"{name}_{suffix}.csv"
        with open(path, encoding="utf-8") as f:
            lines = [next(f).rstrip() for _ in range(n + 1)]
        n_rows = sum(1 for _ in open(path, encoding="utf-8")) - 1
        print(f"\n{path.name} ({n_rows} rows)")
        print("\n".join("  " + line for line in lines))


def load_dataset(name):
    """Load ``data/<name>_*.csv`` into arrays.

    Returns (spikes, labels, label_names, dt) where spikes has shape
    (n_trials, n_neurons, n_bins) and holds 1 for a spike in that bin.
    """
    info = dataset_info(name)
    n_trials, n_neurons = int(info["n_trials"]), int(info["n_neurons"])
    bin_ms = int(info["bin_ms"])
    n_bins = int(info["duration_ms"]) // bin_ms

    trials = read_csv(DATA_DIR / f"{name}_trials.csv")
    labels = np.array([int(r["label"]) for r in trials])
    label_names = [None] * (labels.max() + 1)
    for r in trials:
        label_names[int(r["label"])] = r["label_name"]

    table = np.loadtxt(DATA_DIR / f"{name}_spikes.csv", delimiter=",", skiprows=1, dtype=int, ndmin=2)
    spikes = np.zeros((n_trials, n_neurons, n_bins), dtype=np.uint8)
    spikes[table[:, 0], table[:, 1], table[:, 2] // bin_ms] = 1
    return spikes, labels, label_names, bin_ms / 1000


def plot_raster(spikes, labels, neuron, label_names, dt, n_trials=20, ax=None):
    """Raster of one neuron: a row per trial, a tick per spike, one colour per class."""
    ax = ax or plt.gca()
    row = 0
    for c, name in enumerate(label_names):
        trials = np.flatnonzero(labels == c)[:n_trials]
        for k in trials:
            times = np.flatnonzero(spikes[k, neuron]) * dt
            ax.vlines(times, row, row + 0.8, color=f"C{c}", lw=0.8)
            row += 1
        ax.plot([], [], color=f"C{c}", label=name)
    ax.set(xlabel="time (s)", ylabel="trial", title=f"neuron {neuron}")
    ax.legend(loc="upper right", fontsize="small")
    return ax


def plot_psth(spikes, labels, neuron, label_names, dt, bin_size=0.05, ax=None):
    """Peri-stimulus time histogram: mean firing rate (Hz) over time, per class."""
    ax = ax or plt.gca()
    n_bins = spikes.shape[2]
    step = int(round(bin_size / dt))
    edges = np.arange(0, n_bins - step + 1, step)
    for c, name in enumerate(label_names):
        s = spikes[labels == c, neuron].astype(int)
        rate = np.add.reduceat(s, edges, axis=1).mean(axis=0) / bin_size
        ax.plot(edges * dt, rate, color=f"C{c}", label=name)
    ax.set(xlabel="time (s)", ylabel="rate (Hz)", title=f"neuron {neuron}")
    ax.legend(loc="upper right", fontsize="small")
    return ax
