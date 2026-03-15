# Setup Guide

## Requirements

- Python 3.11+
- CUDA-compatible GPU (recommended)
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or pip

---

## 1. Clone the Repository
```bash
git clone https://github.com/your-username/firstdataset.git
cd firstdataset
```

## 2. Create and Activate Conda Environment
```bash
conda create -n yolo python=3.11 -y
conda activate yolo
```

## 3. Install PyTorch with CUDA

For CUDA 12.4:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

For CPU only:
```bash
pip install torch torchvision torchaudio
```

## 4. Install Dependencies
```bash
pip install ultralytics
```

## 5. Train the Model
```bash
cd models
python train.py
```

> Training results will be saved to `models/runs/segment/`

---

## Notes

- Default training uses `device=0` (GPU). Change to `device='cpu'` in `train.py` if no GPU is available.
- To check if CUDA is working:
```bash
python -c "import torch; print(torch.cuda.is_available())"
```
