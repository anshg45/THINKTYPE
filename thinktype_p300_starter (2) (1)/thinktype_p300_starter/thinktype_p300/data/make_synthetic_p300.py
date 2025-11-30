import numpy as np, argparse
from config import FS, GRID_ROWS, GRID_COLS, EPOCH_TMIN, EPOCH_TMAX

def simulate_trial(target_idx, n_seq=12, flash_on_ms=100, isi_ms=75, fs=256, n_channels=8):
    flash_samples = int(fs*(flash_on_ms/1000.0 + isi_ms/1000.0))
    total_flashes = n_seq*(GRID_ROWS+GRID_COLS)
    T = total_flashes*flash_samples + int(fs*1.0)
    eeg = 1e-6*np.random.randn(n_channels, T)

    t = np.arange(int(fs*0.8)) / fs
    p300 = 2e-6*np.exp(-((t-0.3)**2)/(2*0.05**2))

    t_row = target_idx // GRID_COLS
    t_col = target_idx % GRID_COLS

    s = int(fs*0.5)
    events = []
    for _ in range(n_seq):
        rows = np.random.permutation(GRID_ROWS)
        cols = np.random.permutation(GRID_COLS)
        for r in rows:
            is_target = 1 if r==t_row else 0
            events.append((s, {"kind":"ROW","id":int(r),"target":is_target}))
            if is_target:
                for ch in [1,2,3]:
                    eeg[ch, s:s+len(p300)] += p300
            s += flash_samples
        for c in cols:
            is_target = 1 if c==t_col else 0
            events.append((s, {"kind":"COL","id":int(c),"target":is_target}))
            if is_target:
                for ch in [1,2,3]:
                    eeg[ch, s:s+len(p300)] += p300
            s += flash_samples
    return eeg, events

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="data/p300_demo_epochs.npz")
    ap.add_argument("--subjects", type=int, default=3)
    ap.add_argument("--trials", type=int, default=24)
    args = ap.parse_args()

    np.random.seed(7)
    allX, ally = [], []
    for subj in range(args.subjects):
        for tr in range(args.trials):
            target_idx = np.random.randint(0, GRID_ROWS*GRID_COLS)
            eeg, events = simulate_trial(target_idx, n_seq=12)
            fs = FS
            n_times = int((EPOCH_TMAX - EPOCH_TMIN)*fs)
            for s, info in events:
                start = int(s + EPOCH_TMIN*fs); end = start + n_times
                if start < 0 or end > eeg.shape[1]: continue
                X = eeg[:, start:end]; y = int(info["target"])
                allX.append(X); ally.append(y)
    X = np.array(allX, dtype=np.float32); y = np.array(ally, dtype=np.int64)
    np.savez(args.out, X=X, y=y)
    print("Saved", args.out, "shape", X.shape, "targets", y.sum())
