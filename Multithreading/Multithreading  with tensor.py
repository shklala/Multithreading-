import threading
import time
import random
import tensorflow as tf
import numpy as np

# Define the task for classification
def classify_images(thread_name):
    print(f'{thread_name}: Starting image classification')
    model = tf.keras.applications.MobileNetV2(weights='imagenet')
    for i in range(5):
        img = np.random.random((1, 224, 224, 3)) * 255
        preds = model.predict(img)
        print(f'{thread_name}: Classified image {i+1} with label {tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0][0][1]}')
        time.sleep(random.uniform(0.5, 1.5))
    print(f'{thread_name}: Finished image classification')

# Define the task for object detection
def detect_objects(thread_name):
    print(f'{thread_name}: Starting object detection')
    model = tf.keras.applications.MobileNetV2(weights='imagenet')
    for i in range(5):
        img = np.random.random((1, 224, 224, 3)) * 255
        preds = model.predict(img)
        print(f'{thread_name}: Detected objects in frame {i+1} with label {tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0][0][1]}')
        time.sleep(random.uniform(0.5, 1.5))
    print(f'{thread_name}: Finished object detection')

# Define the task for sending data
def send_data(thread_name):
    print(f'{thread_name}: Starting data transmission')
    for i in range(5):
        time.sleep(random.uniform(0.5, 1.5))
        print(f'{thread_name}: Sent data packet {i+1}')
    print(f'{thread_name}: Finished data transmission')

# Create threads for each task
classification_thread = threading.Thread(target=classify_images, args=('Classifier',))
detection_thread = threading.Thread(target=detect_objects, args=('Detector',))
sending_thread = threading.Thread(target=send_data, args=('Sender',))

# Start the threads
classification_thread.start()
detection_thread.start()
sending_thread.start()

# Wait for all threads to complete
classification_thread.join()
detection_thread.join()
sending_thread.join()

print('All tasks have completed 👍.')
