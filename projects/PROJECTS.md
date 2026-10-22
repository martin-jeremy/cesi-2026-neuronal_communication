# Team Projects

Two groups, two case studies, one tool: the **epistemological bridge**. Both projects work on spike-train recordings and ask the same underlying question: what does an artificial neuron keep from the biology, and what does it discard?

| | Project 1: Neural Decoding for a BCI | Project 2: Motor Effort Test & Prosthesis |
|:---|:---|:---|
| Notebook | `Project1_BrainComputerInterface.ipynb` | `Project2_MotorEffortTest.ipynb` |
| Data | `data/bci_visual_2stim_*.csv` | `data/motor_effort_*.csv`, `data/visual_3stim_*.csv` |
| Model | | `models/pretrained_decoder.safetensors`, the intern's decoder |
| You start from | nothing: you build the decoder | an inherited decoder, `decoder.py`, that fails on new data |
| Core task | build, train, evaluate, interrogate | audit, repair, explain |
| Bonus | what would need to change to account for what was discarded? | does it matter where you put activations across layers? |

## Files

| File | What it is |
|:---|:---|
| `data/*.csv` | the recordings, as the lab shares them: one row per spike, one row per trial. Open them in a spreadsheet or in VS Code |
| `data/README.md` | the data dictionary: what every file and every column means |
| `spikes.py` | helpers: `load_dataset` (CSV to arrays), `preview` (first lines of the files), `plot_raster`, `plot_psth` |
| `REPORT_TEMPLATE.md` | how to write your report: a 4-page mini-article |
| `decoder.py` | Project 2 only: the code of the decoder inherited from the previous intern |
| `models/pretrained_decoder.safetensors` | Project 2 only: its trained parameters. **safetensors** is the standard format to share model weights: the tensors, plus a small "model card" of metadata. `decoder.print_model_card()` shows what the file declares about itself |

Open the notebooks from this folder (`projects/v2/`), with the environment created by `uv sync` at the repository root.

## What you need, and when you get it

| To succeed in the projects, you need to... | Chapter | When |
|:---|:---:|:---:|
| Read spike trains: rasters, PSTH, firing rates | 2 and 3 | Mon PM, Tue AM |
| Turn a trial into a vector of numbers (features) | 3 | Tue AM |
| Code a neuron, then a perceptron, in NumPy | 3 to 5 | Tue, Wed PM |
| Evaluate a decoder: train / test split, accuracy, confusion matrix, standardization | 5 | Wed PM |
| Handle more than two classes; layers and activations | 7 | Thu |
| Criticize your model: what is kept, what is discarded | the bridge | every chapter |

- **Wednesday morning (2h)**: project time, in autonomy, with me around for your questions. Explore the data, build your first features. Project 2: reproduce the failure and start the audit.
- **Thursday afternoon (2h)**: project time again: models, results, your bridge. Ask your questions while we are together.
- **20th November**: the mini-articles and the notebooks must be submitted to me.

## Deliverables

1. A **mini-article**: 4 pages maximum, IMRaD, following `REPORT_TEMPLATE.md`, with your notebook, cleaned and runnable, in annex.
2. Its **30-minute presentation** at the lab meeting.

Both must show:
- your decoder and its performance on **held-out** trials;
- at least **two figures** supporting your interpretation;
- **your bridge**: what your model keeps and discards from the biology;
- a clear answer to the question asked in your subject.
