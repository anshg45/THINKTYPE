 🧠 ThinkType

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![MNE](https://img.shields.io/badge/MNE-ECoG%2FEEG%20toolkit-purple)](https://mne.tools/)
[![pylsl](https://img.shields.io/badge/LSL-pylsl-blue)](https://github.com/labstreaminglayer/liblsl-Python)
[![pygame](https://img.shields.io/badge/UI-pygame-orange)](https://www.pygame.org/)

[![Stars](https://img.shields.io/github/stars/USERNAME/REPO?style=social)](https://github.com/USERNAME/REPO/stargazers)
[![Issues](https://img.shields.io/github/issues/USERNAME/REPO)](https://github.com/USERNAME/REPO/issues)
[![License](https://img.shields.io/github/license/USERNAME/REPO)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/USERNAME/REPO/pulls)

> A minimal **P300-based EEG speller** pipeline: synthetic data → xDAWN + Logistic Regression → real-time online spelling with LSL.

---

## 🎯 What is ThinkType?

ThinkType is a **P300 speller** system that lets users “type with attention” on a flashing 6×6 character grid using EEG data.

It includes:

- Synthetic P300 demo data generation
- xDAWN + Logistic Regression flash classifier
- Pygame-based P300 speller UI
- Real-time pipeline using LabStreamingLayer (LSL) for online spelling

---

## ⚙️ Core Configuration (Neuro / Signal Settings)

Key configuration used by the system (see `config.py`):

- **Sampling rate (FS):** `256 Hz` :contentReference[oaicite:0]{index=0}  
- **Channels:** `["Fz", "Cz", "Pz", "Oz", "POz", "P3", "P4"]` :contentReference[oaicite:1]{index=1}  
- **Grid:** `6 × 6` characters (A–Z, 0–9) :contentReference[oaicite:2]{index=2}  
- **Stimulus timing:**
  - Flash ON: `100 ms`
  - Inter-stimulus interval (ISI): `75 ms` :contentReference[oaicite:3]{index=3}  
- **Epoch window:** `-0.2 s` to `0.8 s` around each flash marker :contentReference[oaicite:4]{index=4}  
- **Preprocessing:** Bandpass `0.1–15 Hz` :contentReference[oaicite:5]{index=5}  
- **xDAWN components:** `4` :contentReference[oaicite:6]{index=6}  

These can all be edited in `config.py` to match your EEG setup.

---

## 🧩 Features

- ✅ Full **offline + online** P300 pipeline
- ✅ Synthetic data generator (no hardware needed to test)
- ✅ Easy training script for xDAWN + Logistic Regression classifier
- ✅ Simple Pygame GUI for 6×6 P300 speller grid
- ✅ Real-time mode using LabStreamingLayer (LSL) EEG stream
- ✅ Config-driven (change channels, timings, sequences, etc. from a single file)

---

## 📦 Installation

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux / Mac:
source .venv/bin/activate

pip install -r requirements.txt
````

**Main dependencies:** `mne`, `numpy`, `scipy`, `scikit-learn`, `pylsl`, `pygame`. 

---

## 📁 Project Structure (key scripts)

```bash
data/
  make_synthetic_p300.py   # Generate demo synthetic P300 epochs
models/
  train_p300_xdawn.py      # Train xDAWN + Logistic Regression flash classifier
stimuli/
  p300_grid.py             # Pygame flashing grid UI (sends LSL markers)
realtime/
  p300_live.py             # Real-time calibrate + type modes
config.py                  # Global config: channels, timings, epochs, etc.
```

---

## 🚀 Quick Start

### 1️⃣ Create demo data (synthetic)

No EEG hardware? No problem. Generate demo P300 epochs:

```bash
python data/make_synthetic_p300.py --out data/p300_demo_epochs.npz
```



### 2️⃣ Train the xDAWN + Logistic Regression classifier

```bash
python models/train_p300_xdawn.py --data data/p300_demo_epochs.npz
```



This will:

* Load epochs
* Apply xDAWN spatial filtering
* Train a Logistic Regression classifier for target vs non-target flashes
* Save the trained model (check script for output path)

### 3️⃣ Run the P300 flasher UI

```bash
python stimuli/p300_grid.py
```



This launches a **6×6 speller grid** where rows/columns flash and LSL markers are sent for each flash.

### 4️⃣ Real-time mode (with EEG over LSL)

1. Make sure your **EEG is streaming over LSL** (`type=EEG`).

2. **Calibrate** while focusing on prompted keys:

   ```bash
   python realtime/p300_live.py --mode calibrate --seconds 60
   ```

3. Then start **typing** (focus your desired letter):

   ```bash
   python realtime/p300_live.py --mode type
   ```



---

## 🛠️ Tuning & Tips

From the quick guide: 

* Place electrodes at **Cz, Pz, Oz, POz** (add **P3, P4, Fz** if available).
* Keep screen luminance moderate.
* Blink during ISI (not during flashes).
* **60–120 s** of calibration improves accuracy significantly.

Key config parameters to play with (in `config.py`):

* `CHANNELS`
* `FLASH_ON_MS`, `ISI_MS`
* `SEQUENCES_PER_TRIAL`
* `EPOCH_TMIN`, `EPOCH_TMAX`

---

## 🧪 Future Ideas / TODO

* [ ] Support more EEG montages & channel configs
* [ ] Save and visualize ERP waveforms for each user
* [ ] GUI for model training + evaluation
* [ ] Online accuracy and ITR dashboard
* [ ] Integration with spelling assistive interfaces (e.g. text-to-speech)

---

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

* Open an issue: [GitHub Issues](https://github.com/USERNAME/REPO/issues)
* Fork the repo, create a branch, and open a PR 🚀

---

## 📜 License

This project uses the license defined in the [`LICENSE`](LICENSE) file.
(If you haven't added one yet, MIT is a good default.)

---


