
# PDD2026: Road Pavement Deformation Dataset

## Dataset Access

This repository provides supporting materials, documentation, metadata, dataset split information, annotation guidelines, and source code related to the **PDD2026 (Pavement Deformation Dataset 2026)**.

Due to the large size of the dataset, the complete collection of original images cannot be hosted directly within this GitHub repository.

### Original Images Dataset

The original images collected during the data acquisition process can be accessed through Google Drive:

🔗 **Google Drive Repository**  
[Access Original Dataset](https://drive.google.com/drive/folders/1PhjeT0Okik784VXfbqcIUFtHJCpHWk46?usp=sharing)

---

### Resized Dataset (1024 × 1024)

For training and evaluation purposes, all images were resized to a standardized resolution of **1024 × 1024 pixels**. The resized version of the dataset is publicly available through Mendeley Data:

🔗 **Mendeley Data Repository**  
[Access Resized Dataset](http://dx.doi.org/10.17632/fgtjn9kjkd.2)

---

## Repository Contents

```text
.
├── README.md
├── annotation_guideline/
├── metadata/
├── split_generation/
├── source_code/
└── supplementary_files/
```

### Description

- **annotation_guideline/**  
  Annotation guidelines used during mask generation and expert validation.

- **metadata/**  
  Dataset metadata and supplementary information.

- **split_generation/**  
  Source code used to generate training, validation, and testing splits.

- **source_code/**  
  Scripts used for preprocessing, dataset preparation, and experiments.

- **supplementary_files/**  
  Additional files supporting dataset documentation.

---

## Citation

If you use this dataset in your research, please cite the associated publication:

**PDD2026: A Pixel-Level Annotated Dataset for Road Pavement Deformation Semantic Segmentation**

---

## Notes

- The original images are provided in their native resolutions as collected from multiple acquisition devices.
- The Mendeley Data version contains the resized images (1024 × 1024 pixels) used for model development and benchmarking.
- Both repositories are publicly accessible and intended to support reproducible research in pavement distress detection and semantic segmentation.
