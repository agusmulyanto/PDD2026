# YOLO26 Segmentation on PDD2026

This repository provides the code for training and evaluating **YOLO26s-Seg** for pixel-level road pavement deformation segmentation using the **PDD2026 dataset**.

The implementation uses the standard **Ultralytics YOLO segmentation framework** and includes:

* Dataset preparation
* YOLO26s-Seg model loading
* Model training
* Validation
* Test-set prediction
* Training-result visualization
* Confusion matrix and precision/recall analysis

---

## 1. Dataset

The model is trained using the **PDD2026: A Pixel-Level Annotated Dataset for Road Pavement Deformation Segmentation** dataset.

The dataset is publicly available through Mendeley Data:

**Dataset DOI:**
http://dx.doi.org/10.17632/fgtjn9kjkd.2

Download the dataset before running the training notebook.

After downloading and extracting the dataset, place the dataset directory inside the project directory so that the following path is available:

```text
FinalDataset_1024/
```

The expected dataset configuration file is:

```text
FinalDataset_1024/data.yaml
```

---

## 2. Dataset Structure

The dataset should follow the YOLO segmentation directory structure:

```text
FinalDataset_1024/
│
├── data.yaml
│
├── images/
│   ├── train/
│   ├── val/
│   └── test/
│
└── labels/
    ├── train/
    ├── val/
    └── test/
```

The `data.yaml` file defines the dataset paths and segmentation classes.

An example configuration is:

```yaml
path: FinalDataset_1024

train: images/train
val: images/val
test: images/test

names:
  0: Depression
  1: Rutting
  2: Upheaval
  3: Pothole
  4: Patching
```

Make sure that the paths in `data.yaml` correspond to the actual location of the dataset on your computer.

---

## 3. Classes

PDD2026 contains five road pavement deformation classes:

| ID | Class      |
| -: | ---------- |
|  0 | Depression |
|  1 | Rutting    |
|  2 | Upheaval   |
|  3 | Pothole    |
|  4 | Patching   |

The annotations are provided at the **pixel level** using polygon-based segmentation labels in YOLO format.

---

## 4. Requirements

The code requires Python and the following Python packages:

```bash
pip install ultralytics matplotlib pillow
```

Alternatively, install the dependencies individually:

```bash
pip install ultralytics
pip install matplotlib
pip install pillow
```

It is recommended to use a CUDA-enabled NVIDIA GPU for training.

---

## 5. Clone the Repository

Clone this repository:

```bash
git clone https://github.com/agusmulyanto/PDD2026.git
cd PDD2026
```

If the training notebook is located in a different repository, place the downloaded dataset in the same project directory as the notebook.

---

## 6. Download and Prepare the Dataset

### Step 1 — Download PDD2026

Download the dataset from:

http://dx.doi.org/10.17632/fgtjn9kjkd.2

### Step 2 — Extract the Dataset

Extract the downloaded dataset.

The project directory should contain:

```text
project/
│
├── FinalDataset_1024/
│   ├── data.yaml
│   ├── images/
│   │   ├── train/
│   │   ├── val/
│   │   └── test/
│   └── labels/
│       ├── train/
│       ├── val/
│       └── test/
│
└── training_notebook.ipynb
```

### Step 3 — Check `data.yaml`

Make sure that:

```text
FinalDataset_1024/data.yaml
```

exists and correctly points to the training, validation, and test images.

---

## 7. YOLO26s-Seg Model

The training code uses:

```text
yolo26s-seg.pt
```

The model is loaded using the Ultralytics API:

```python
from ultralytics import YOLO

model = YOLO("yolo26s-seg.pt")
```

If the pretrained model is not available locally, Ultralytics will normally download the required model weights when the model is initialized.

---

## 8. Training Configuration

The default training configuration used in the notebook is:

| Parameter  |                 Value |
| ---------- | --------------------: |
| Model      |      `yolo26s-seg.pt` |
| Task       | Instance Segmentation |
| Epochs     |                   400 |
| Image Size |             640 × 640 |
| Batch Size |                     8 |
| Workers    |                     4 |
| Device     |                 GPU 0 |
| AMP        |               Enabled |
| Cache      |              Disabled |

The training command is:

```python
results = model.train(
    data=DATA_YAML,
    epochs=400,
    imgsz=640,
    batch=8,
    workers=4,
    cache=False,
    device=0,
    amp=True
)
```

---

## 9. Run Training

Open the provided Jupyter Notebook and execute the cells sequentially.

The main configuration is:

```python
DATA_YAML = "FinalDataset_1024/data.yaml"
MODEL = "yolo26s-seg.pt"
```

The model is then initialized:

```python
model = YOLO(MODEL)
```

and trained using:

```python
results = model.train(
    data=DATA_YAML,
    epochs=400,
    imgsz=640,
    batch=8,
    workers=4,
    cache=False,
    device=0,
    amp=True
)
```

Training results are automatically stored by Ultralytics in the corresponding `runs/` directory.

---

## 10. Validation

After training, the trained model is evaluated using:

```python
metrics = model.val()
```

This performs validation using the dataset configuration specified in:

```text
FinalDataset_1024/data.yaml
```

The validation output includes segmentation evaluation metrics generated by Ultralytics.

---

## 11. Test-Set Prediction

After validation, the trained model is used to perform prediction on the test images:

```python
model.predict(
    source="FinalDataset_1024/images/test",
    imgsz=640,
    conf=0.25,
    save=True,
    project="runs_yolo26_seg",
    name=f"{RUN_NAME}_predict"
)
```

The prediction uses:

* Test images from `FinalDataset_1024/images/test`
* Input size: `640 × 640`
* Confidence threshold: `0.25`
* Prediction results: saved automatically

The predicted images can be found under:

```text
runs_yolo26_seg/
```

---

## 12. Training Results

The notebook automatically displays commonly generated Ultralytics plots, including:

```text
results.png
confusion_matrix.png
PR_curve.png
P_curve.png
R_curve.png
F1_curve.png
```

These files provide information about:

### `results.png`

Training and validation performance across epochs, including loss and evaluation metrics.

### `confusion_matrix.png`

Class-level prediction performance represented using a confusion matrix.

### `PR_curve.png`

Precision–Recall relationship across different confidence thresholds.

### `P_curve.png`

Precision as a function of confidence threshold.

### `R_curve.png`

Recall as a function of confidence threshold.

### `F1_curve.png`

F1-score as a function of confidence threshold.

---

## 13. Output Directory

The training output is generated by Ultralytics.

The notebook obtains the training output directory using:

```python
save_dir = results.save_dir
```

The location is then printed:

```text
Training Results Saved To:
<training output directory>
```

Prediction results are stored separately under:

```text
runs_yolo26_seg/
```

---

## 14. Complete Workflow

The overall workflow implemented in this repository is:

```text
PDD2026 Dataset
       │
       ▼
Download Dataset
       │
       ▼
FinalDataset_1024
       │
       ▼
data.yaml
       │
       ▼
YOLO26s-Seg
       │
       ▼
Model Training
       │
       ▼
Validation
       │
       ▼
Test-Set Prediction
       │
       ▼
Visualization
       │
       ├── results.png
       ├── confusion_matrix.png
       ├── PR_curve.png
       ├── P_curve.png
       ├── R_curve.png
       └── F1_curve.png
```

---

## 15. Reproducibility

The training configuration is explicitly defined in the notebook to make the experiment easier to reproduce.

The main parameters are:

```python
epochs=400
imgsz=640
batch=8
workers=4
cache=False
device=0
amp=True
```

To reproduce the experiment, use the same dataset version and training configuration.

The dataset used in this repository is:

**PDD2026, Version 2**

DOI:

http://dx.doi.org/10.17632/fgtjn9kjkd.2

---

## 16. Notes

### GPU

The default configuration uses:

```python
device=0
```

which means that the first CUDA-enabled GPU is used.

For CPU-only execution, the configuration can be changed according to the Ultralytics environment.

### Batch Size

The default batch size is:

```python
batch=8
```

If GPU memory is insufficient, reduce the batch size.

For example:

```python
batch=4
```

or:

```python
batch=2
```

### Image Size

The training input size is:

```python
imgsz=640
```

This is independent of the original image resolution in the dataset because the images are processed according to the YOLO input configuration during training.

---

## 17. Citation

If you use the PDD2026 dataset in your research, please cite the corresponding dataset publication and dataset DOI.

### Dataset

**PDD2026: A Pixel-Level Annotated Dataset for Road Pavement Deformation Segmentation**

Dataset DOI:

http://dx.doi.org/10.17632/fgtjn9kjkd.2

---

## 18. Repository

Source code and related materials:

https://github.com/agusmulyanto/PDD2026

---

## 19. License

Please refer to the dataset and repository license information before redistributing the dataset or modifying and redistributing the source code.

---

## 20. Acknowledgment

This work uses the PDD2026 dataset for road pavement deformation segmentation research.

The dataset was developed to support research on pixel-level segmentation of road pavement deformation, including **depression, rutting, upheaval, pothole, and patching**.
