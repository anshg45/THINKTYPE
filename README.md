# ThinkType P300 Speller — Quick Guide

## Install
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
```

## Create demo data (synthetic)
```bash
python data/make_synthetic_p300.py --out data/p300_demo_epochs.npz
```

## Train flash classifier (xDAWN+LR)
```bash
python models/train_p300_xdawn.py --data data/p300_demo_epochs.npz
```

## Run flasher UI (sends LSL markers)
```bash
python stimuli/p300_grid.py
```

## Live
1) Ensure your EEG streams over LSL (type=EEG)
2) Calibrate while focusing prompted keys:
```bash
python realtime/p300_live.py --mode calibrate --seconds 60
```
3) Type (focus your desired letter):
```bash
python realtime/p300_live.py --mode type
```

### Edit config
- `FS`, `CHANNELS`
- `FLASH_ON_MS`, `ISI_MS`, `SEQUENCES_PER_TRIAL`
- `EPOCH_TMIN`, `EPOCH_TMAX`

### Tips
- Place electrodes at **Cz, Pz, Oz, POz** (add P3/P4/Fz if available)
- Keep luminance moderate, blink during ISI
- 60–120s calibration improves accuracy a lot
