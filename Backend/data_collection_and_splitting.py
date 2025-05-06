import tensorflow as tf
import matplotlib.pyplot as plt
import os
import numpy as np
from tensorflow.keras.preprocessing import image_dataset_from_directory

# Collecting Dataset from Path
dataset = image_dataset_from_directory(
    r"D:\BotanicaLens\dataset",   # <- Use raw string
    shuffle=False,                # <- No shuffle here
    batch_size=16,
    image_size=(299, 299),
)

# AUTOTUNE = tf.data.AUTOTUNE
# dataset = dataset.prefetch(buffer_size=AUTOTUNE)

# Class Information
class_names = dataset.class_names
print("Class Names:", class_names)
print("Number of Classes:", len(class_names))

# Find the batch size
for images, labels in dataset.take(1):  # Take one batch from the dataset
    print("Batch Size:", images.shape[0])
    print("Image Size:", images.shape[1:])
    print("Image Data Type:", images.dtype)
    print("Label Data Type:", labels.dtype)
    print("Label Shape:", labels.shape)
    print("Labels in Batch:", labels.numpy())

# Total number of batches in the dataset
total_batches = tf.data.experimental.cardinality(dataset).numpy()
print("Total Number of Batches:", total_batches)

# Total number of images in the dataset
total_images = total_batches * images.shape[0]
print("Total Number of Images:", total_images)

# Data Split
def get_dataset_partitions_tf(ds, train_split=0.75, val_split=0.15, test_split=0.1, shuffle=True, shuffle_buffer_size=1000):
    if shuffle:
        ds = ds.shuffle(buffer_size=shuffle_buffer_size, seed=12)
    
    dataset_size = tf.data.experimental.cardinality(ds).numpy()

    train_size = int(train_split * dataset_size)
    val_size = int(val_split * dataset_size)

    train_ds = ds.take(train_size)
    val_ds = ds.skip(train_size).take(val_size)
    test_ds = ds.skip(train_size + val_size)

    return train_ds, val_ds, test_ds

train_data, val_data, test_data = get_dataset_partitions_tf(dataset)

print("Train Data batches:", tf.data.experimental.cardinality(train_data).numpy())
print("Validation Data batches:", tf.data.experimental.cardinality(val_data).numpy())
print("Test Data batches:", tf.data.experimental.cardinality(test_data).numpy())
