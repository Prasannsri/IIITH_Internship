import os
import random
import shutil

# paths
image_dir = "images"
label_dir = "labels"

output_dir = "dataset"

# create folders
for split in ["train", "val"]:
    os.makedirs(os.path.join(output_dir, "images", split), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "labels", split), exist_ok=True)

# get all images
images = [f for f in os.listdir(image_dir) if f.endswith(".jpg")]

random.shuffle(images)

# split
train_images = images[:100]
val_images = images[100:140]

def copy_files(image_list, split):
    for img in image_list:
        label = img.replace(".jpg", ".txt")

        shutil.copy(os.path.join(image_dir, img),
                    os.path.join(output_dir, "images", split, img))

        if os.path.exists(os.path.join(label_dir, label)):
            shutil.copy(os.path.join(label_dir, label),
                        os.path.join(output_dir, "labels", split, label))

# copy
copy_files(train_images, "train")
copy_files(val_images, "val")

print("✅ Dataset split done!")