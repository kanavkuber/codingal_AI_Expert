import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Load MNIST dataset
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

# Normalize the data
train_images, test_images = train_images / 255.0, test_images / 255.0

# Build the model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

# Train the model
model.fit(train_images, train_labels, epochs=5)

# Evaluate the model
loss_value, accuracy_value = model.evaluate(test_images, test_labels)
print(f"Test accuracy: {accuracy_value}")

# Make predictions
predictions = model.predict(test_images)

# Display the first image and prediction
plt.imshow(test_images[0], cmap=plt.cm.binary)
plt.title(
    f"Predicted Digit: {prediction_results[0].argmax()}"
)
plt.show()