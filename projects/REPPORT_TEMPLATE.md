# Project report: a mini-article

Your report is a short scientific article, the kind of paper a lab writes to share one result.
It is the written part of your case study; the 30-minute presentation on Monday 23 November
presents this article.

## Format

- **4 pages maximum**, references and annex excluded, as a **PDF**, in English.
- **Annex**: your project notebook, cleaned, that runs from top to bottom without error
  (*Kernel > Restart & Run All*). Anyone must be able to reproduce every number of the article.
- **Due**: Friday 20 November, with your notebook. The presentation follows on Monday 23 November.

## Structure (IMRaD)

**Title**: a claim, not a topic. I don't want to see any *"Project report"*.

**Authors**: the members of the group.

**Abstract** (150 words maximum): the question, what you did, the main result **with a number**,
and the main limit.

**1. Introduction** (about half a page)
- The context: a brain computer interface.
- The question asked by the PI, in your own words.
- Why the answer matters, for the device and for our understanding of neurons.

**2. Data and Methods** (about one page): enough detail for another group to reproduce your work.
- The recordings: number of trials, neurons, trial duration, classes.
- Your features: what you count, over which time windows; how you standardize, and on which trials.
- Your model, with the notation of the course: $z = w \cdot x + b$, $y = \varphi(z)$, the learning rule, $\eta$, the number of epochs.
- Your evaluation protocol: the train / test split (and its seed), the metrics (accuracy, confusion matrix).

**3. Results** (about one page): facts only, interpretation comes in the Discussion.
- At least **two figures**, numbered, with a caption, axis labels and units, each one cited in the text.
- Every score is measured on **held-out trials**. Give the confusion matrix, not only the accuracy.
- Compare your options (for example spike counts vs time-binned features) on the same test trials.

**4. Discussion** (about one page)
- Your answer to the PI's question, and the results that support it.
- **Your bridge**: fill the table below for your own pipeline.
- The limits of your study: amount of data, a single split, synthetic recordings, ...
- What you would change next (the bonus of your subject).

| Biological reality | What your pipeline turned it into | Kept, simplified or discarded? | Consequence for your results |
|:---|:---|:---|:---|
| Spike trains over time | ... | ... | ... |
| Synaptic strength and sign | ... | ... | ... |
| Each neuron's identity (channel) | ... | ... | ... |
| Trial-to-trial variability | ... | ... | ... |
| How the brain learns | ... | ... | ... |

**5. Conclusion**: three to five sentences. What you found, what it means, what remains open.

**References** (optional): the course slides, papers, documentation you used.

## What we look at

- The question is clearly stated, and the conclusion answers it.
- The methods are precise enough to reproduce the results, and the notebook actually does.
- Every score comes from held-out trials.
- The figures are readable, captioned, and support what the text says.
- The interpretation goes back to the biology: the bridge, what is kept, what is discarded.
- The limits are stated honestly.
