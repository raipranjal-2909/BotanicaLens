import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Resizing, Rescaling
from data_collection_and_splitting import train_data, val_data, test_data
from tensorflow.keras.models import load_model


# Preprocessing Layer
resize_and_rescale = Sequential([
    Resizing(224, 224),
    Rescaling(1./255)
])

# Importing Xception Model
base_model = MobileNetV2(
    weights='imagenet',
    input_shape=(224, 224, 3),
    include_top=False,
    pooling='avg'
)

# Constructing the Model
base_model.trainable = False

inputs = tf.keras.Input(shape=(299, 299, 3))
x = resize_and_rescale(inputs)
x = base_model(x, training=False)
x = tf.keras.layers.Dense(128, activation='relu')(x)
x = tf.keras.layers.Dropout(0.2)(x)
outputs = tf.keras.layers.Dense(80, activation='softmax')(x)
model = tf.keras.Model(inputs, outputs)

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Prefetch for performance
AUTOTUNE = tf.data.AUTOTUNE
train_data = train_data.prefetch(buffer_size=AUTOTUNE)
val_data = val_data.prefetch(buffer_size=AUTOTUNE)
test_data = test_data.prefetch(buffer_size=AUTOTUNE)

# Layer Description of the Model
model.summary()
print("Train data available? ", train_data)

# Training the Model with 30 Epochs
history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=20
)

# Evaluating the Test Data
model.evaluate(test_data)

# Saving the Model
model.save("model.h5")

# Plotting Accuracy Graph
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()
