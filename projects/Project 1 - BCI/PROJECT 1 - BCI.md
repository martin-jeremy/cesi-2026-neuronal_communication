# Project 1: Neural Decoding for a Brain Computer Interface

Spike-train recordings, one question: what does an artificial neuron keep from the biology, and what does it discard? You build a decoder from nothing (a Perceptron in NumPy), then you interrogate it.

| | |
|:---|:---|
| Notebook | `Project1_BrainComputerInterface.ipynb` |
| Data | `data/bci_visual_2stim_*.csv` |
| You start from | nothing: you build the decoder |
| Core task | build, train, evaluate, interrogate |
| Bonus | what would need to change to account for what was discarded? |

## Files

| File | What it is |
|:---|:---|
| `data/*.csv` | the recordings, as the lab shares them: one row per spike, one row per trial. Open them in a spreadsheet or in VS Code |
| `data/README.md` | the data dictionary: what every file and every column means |
| `src/spikes.py` | helpers: `load_dataset` (CSV to arrays), `preview` (first lines of the files), `plot_raster`, `plot_psth` |
| `REPORT_TEMPLATE.md` | how to write your report: a 4-page mini-article |

Open the notebook from this folder (`projects/v2/Project 1 - BCI/`), with the environment created by `uv sync` at the repository root.

## What you need, and when you get it

| To succeed in the projects, you need to... | Chapter | When |
|:---|:---:|:---:|
| Read spike trains: rasters, PSTH, firing rates | 2 and 3 | Mon PM, Tue AM |
| Turn a trial into a vector of numbers (features) | 3 | Mon PM, Tue AM |
| Code a neuron, then a perceptron, in NumPy | 3 to 5 | Tue, Wed PM |
| Evaluate a decoder: train / test split, accuracy, confusion matrix, standardization | 5 | Wed PM |
| Criticize your model: what is kept, what is discarded | the bridge | every chapter |

- **Wednesday morning (2h)**: project time, in autonomy, with me around for your questions. Explore the data, build your first features.
- **Thursday afternoon (2h)**: project time again: models, results, your bridge. Ask your questions while we are together.
- **Friday 20 November**: the mini-articles and their notebooks are due. **Monday 23 November**: the lab meeting presentations.

## Deliverables: 20 and 23 November

1. A **mini-article**: 4 pages maximum, IMRaD, following `REPORT_TEMPLATE.md`, with your notebook, cleaned and runnable, in annex.
2. Its **30-minute presentation** at the lab meeting.

Both must show:
- your decoder and its performance on **held-out** trials;
- at least **two figures** supporting your interpretation;
- **your bridge**: what your model keeps and discards from the biology;
- a clear answer to the question asked in your subject.
