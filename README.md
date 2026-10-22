# Neural Communication

> ### From biological mechanisms to artificial computational architectures
> *CESI Bachelor AI (Year 2) &bull; ECUE 3.1.3 &bull; Instructor: Jérémy MARTIN*

This repository holds everything you need during the course: the notebooks of each chapter and the material of the team projects. **Content is added as the course goes**, so come back and `git pull` after each session.

---

## The course in one sentence

How does a living neuron, made of ions, membranes and synapses, become `z = w · x + b` and `y = φ(z)`? And what do we keep, and what do we throw away, along the way? We call this the **epistemological bridge**, and we cross it step by step, in pure Python and NumPy.

It is **not** a neuroscience course (no memorizing brain regions) and **not** a black-box deep learning course (no `import torch` to train a huge model). We build the blocks ourselves, to understand why weights, thresholds and activations are designed the way they are.

## The week at a glance

25 hours together. Every chapter mixes lecture, **paper & pencil** exercises and **live coding** in Jupyter.

| | Morning | Afternoon |
|:---|:---|:---|
| **Monday** | Ice breaker, the module, the bridge, the projects | **Ch. 2** The biological neuron, start of **Ch. 3** |
| **Tuesday** | **Ch. 3** From biology to mathematics | **Ch. 4** Logic gates workshop, start of **Ch. 5** |
| **Wednesday** | **Projects**: autonomous work, questions | **Ch. 5** The first learning neuron, start of **Ch. 6** |
| **Thursday** | **Ch. 6** The XOR crisis, start of **Ch. 7** | **Ch. 7** and **Ch. 8** closure, then **Projects**: autonomous work |

### The chapters

**Part 1: Foundations**

1. **Introduction & the epistemological bridge**: scope, core concepts, the projects
2. **The biological neuron**: anatomy, resting potential, the synapse
3. **From biology to mathematics**: abstraction, firing rate, rasters and PSTH, the weighted sum, bias, activation
4. **Logic gates & McCulloch-Pitts neurons**: AND, OR, NOT, and the first hint of a limit

**Part 2: Architectures & learning**

5. **The first learning neuron**: from Hebb to Rosenblatt's perceptron, training, evaluating a decoder
6. **Limits & evolution**: the XOR crisis, and the way out
7. **Multi-layer perceptrons**: non-linearity, layers as matrices, feedforward
8. **Synthesis & closure**: the complete bridge, and where the map differs from the territory

Each step on the right comes from a limit found on the left.

---

## What is in this repository

```
notebooks/   the exercises of each chapter
projects/    the subjects, datasets and helpers of the two team projects
slides/      the slides that we will see together during the course
```

---

## Get ready

### 1. Install the tools

- **[uv](https://github.com/astral-sh/uv)**, a fast Python package and environment manager (see [Astral.sh](https://docs.astral.sh/uv/#installation) website)
- **Git**

### 2. Get the code and the environment

```bash
git clone https://github.com/martin-jeremy/cesi-2026-neuronal_communication.git
cd cesi-2026-neuronal_communication
uv sync                # creates the environment and installs the dependencies
uv run jupyter lab     # opens Jupyter
```

### 3. Check that it works

Open and run `notebooks/Chapter1_Setup.ipynb`. If it prints **Environment OK**, you are ready.

If something fails, tell me at the break or at the end of the morning, do not lose your day on it.

### Stay up to date

```bash
git pull
```

Your own work stays on your machine. I won't edit any of these current file, just updating the slides pdf.

---

## The team projects

You work in **two groups**, on two case studies of the epistemological bridge. Both start from spike-train recordings.

| | **Project 1: Neural decoding for a BCI** | **Project 2: Motor effort test & prosthesis** |
|:---|:---|:---|
| Data | biological neurons answering two visual stimuli | biological neurons during a motor effort |
| You start from | nothing: you build the decoder | an inherited decoder that fails on the new data |
| Core task | build, train, evaluate, interrogate | audit, repair, explain |
| Bonus | what would need to change to account for what was discarded? | does it matter where you put activations across layers? |

*BCI: brain-computer interface. MET: motor effort test.*

### What you need, and when you get it

You are not expected to have a model on day one. Every tool comes in a chapter:

| To succeed in the projects, you need to... | Chapter | When |
|:---|:---:|:---:|
| Read spike trains: rasters, PSTH, firing rates | 2 and 3 | Mon PM, Tue AM |
| Turn a trial into a vector of numbers (features) | 3 | Tue AM |
| Code a neuron, then a perceptron, in NumPy | 3 to 5 | Tue, Wed PM |
| Evaluate a decoder: train / test split, accuracy, standardization | 5 | Wed PM |
| Handle more than two classes, layers and activations | 7 | Thu |
| Criticize your model: what is kept, what is discarded | the bridge | every chapter |

### Project time

- **Wednesday morning (2h)**: autonomy, with me around for your questions. Explore the data, build your first features. Project 2: reproduce the failure and start the audit.
- **Thursday afternoon (2h)**: models, results, your bridge.

### Deliverables

- A **mini-article**: 4 pages maximum, PDF, in English, with your cleaned notebook in annex (it must run top to bottom without error). The structure and tips are in `projects/REPORT_TEMPLATE.md`.
- A **30-minute presentation** of this article followed by a **Q&A session**.
- **Due date: 20/11.**

---

## Good habits for this course

- **Paper first, code second.** Every exercise comes in both forms, in that order.
- **Restart & Run All** before you trust a notebook: *Kernel > Restart Kernel and Run All Cells*.
- **Ask what is kept and what is discarded.** At every step of the bridge, this is the question that matters, and the one the projects are graded on.
