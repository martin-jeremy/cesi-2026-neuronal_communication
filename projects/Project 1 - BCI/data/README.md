# Recordings: data dictionary

All files are plain CSV (comma-separated, UTF-8, one header line). Open them in a spreadsheet,
in VS Code, or load them in Python with `load_dataset` from `src/spikes.py` (in the project folder).

## `datasets.csv`: what is in this folder

| Column | Meaning |
|:---|:---|
| `dataset` | name of the recording session, prefix of its two files |
| `n_trials` | number of trials |
| `n_neurons` | number of recorded neurons: one per channel of the 40-channel array, numbered `0` to `39` |
| `duration_ms` | duration of every trial, in milliseconds |
| `bin_ms` | time resolution of the spike times, in milliseconds |
| `stimulus_onset_ms` | time of the stimulus in each trial (empty: no stimulus, the state lasts the whole trial) |
| `classes` | the possible labels, separated by a vertical bar |
| `description` | what the session is |

| Dataset | Trials | Duration | Classes | Used in |
|:---|:---:|:---:|:---|:---|
| `bci_visual_2stim` | 200 | 1000 ms, stimulus at 200 ms | stimulus_A, stimulus_B | Project 1 |

## `<dataset>_trials.csv`: one row per trial

| Column | Meaning |
|:---|:---|
| `trial` | trial number, from `0` |
| `label` | class of the trial, as a number (`0`, `1`, ...) |
| `label_name` | class of the trial, as a name |

## `<dataset>_spikes.csv`: one row per spike

| Column | Meaning |
|:---|:---|
| `trial` | trial in which the spike happened |
| `neuron` | neuron (channel) that fired |
| `time_ms` | time of the spike from the start of the trial, in milliseconds |

A neuron that never fires has **no row at all**: check `n_neurons` in `datasets.csv` rather than
the neurons you see in the file.
