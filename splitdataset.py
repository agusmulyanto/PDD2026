# ============================================================
# AUTO SPLIT DATASET YOLO SEGMENTATION
# HANYA IMAGE YANG MEMILIKI LABEL AKAN DICOPY
# TRAIN : VAL : TEST = 70 : 20 : 10
# ============================================================

import os
import shutil
import random
from pathlib import Path

# ============================================================
# SOURCE DATASET
# ============================================================

SOURCE_DIR = "PDD2026"

image_dir = os.path.join(SOURCE_DIR, "images/train")
label_dir = os.path.join(SOURCE_DIR, "labels/train")

# ============================================================
# OUTPUT
# ============================================================

OUTPUT_DIR = "PDD2026_split"

# ============================================================
# SPLIT RATIO
# ============================================================

TRAIN_RATIO = 0.70
VAL_RATIO   = 0.20
TEST_RATIO  = 0.10

# ============================================================
# IMAGE EXTENSIONS
# ============================================================

IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png"]

# ============================================================
# CREATE OUTPUT FOLDER
# ============================================================

folders = [
    "images/train",
    "images/val",
    "images/test",
    "labels/train",
    "labels/val",
    "labels/test",
]

for folder in folders:
    os.makedirs(os.path.join(OUTPUT_DIR, folder), exist_ok=True)

# ============================================================
# GET ONLY LABELED IMAGES
# ============================================================

images = []

for image_file in os.listdir(image_dir):

    ext = Path(image_file).suffix.lower()

    if ext not in IMAGE_EXTENSIONS:
        continue

    image_name = Path(image_file).stem

    label_file = image_name + ".txt"

    label_path = os.path.join(label_dir, label_file)

    # ========================================================
    # ONLY INCLUDE IMAGE IF LABEL EXISTS
    # ========================================================

    if os.path.exists(label_path):

        # OPTIONAL:
        # skip empty label file
        if os.path.getsize(label_path) > 0:

            images.append(image_file)

# ============================================================
# SHUFFLE
# ============================================================

random.shuffle(images)

# ============================================================
# SPLIT
# ============================================================

total = len(images)

train_count = int(total * TRAIN_RATIO)
val_count   = int(total * VAL_RATIO)

train_files = images[:train_count]
val_files   = images[train_count:train_count + val_count]
test_files  = images[train_count + val_count:]

# ============================================================
# COPY FUNCTION
# ============================================================

def copy_files(file_list, split_name):

    for image_file in file_list:

        image_name = Path(image_file).stem

        src_image = os.path.join(image_dir, image_file)
        src_label = os.path.join(label_dir, image_name + ".txt")

        dst_image = os.path.join(
            OUTPUT_DIR,
            "images",
            split_name,
            image_file
        )

        dst_label = os.path.join(
            OUTPUT_DIR,
            "labels",
            split_name,
            image_name + ".txt"
        )

        shutil.copy2(src_image, dst_image)
        shutil.copy2(src_label, dst_label)

# ============================================================
# COPY DATA
# ============================================================

copy_files(train_files, "train")
copy_files(val_files, "val")
copy_files(test_files, "test")

# ============================================================
# SUMMARY
# ============================================================

print("===================================")
print("DATASET SPLIT FINISHED")
print("===================================")

print(f"Total Labeled Images : {total}")
print(f"Train Images         : {len(train_files)}")
print(f"Validation Images    : {len(val_files)}")
print(f"Test Images          : {len(test_files)}")

print("===================================")