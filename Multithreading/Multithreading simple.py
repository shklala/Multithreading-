import threading
import time
import random

# Define the task for classification
def classify_images(thread_name):
    print(f'{thread_name}: Starting image classification')
    for i in range(5):  # Simulating classification of 5 images
        time.sleep(random.uniform(0.5, 1.5))  # Simulate time taken to classify an image
        print(f'{thread_name}: Classified image {i+1}')
    print(f'{thread_name}: Finished image classification')

# Define the task for object detection
def detect_objects(thread_name):
    print(f'{thread_name}: Starting object detection')
    for i in range(5):  # Simulating detection in 5 frames
        time.sleep(random.uniform(0.5, 1.5))  # Simulate time taken to detect objects in a frame
        print(f'{thread_name}: Detected objects in frame {i+1}')
    print(f'{thread_name}: Finished object detection')

# Define the task for sending data
def send_data(thread_name):
    print(f'{thread_name}: Starting data transmission')
    for i in range(5):  # Simulating sending 5 data packets
        time.sleep(random.uniform(0.5, 1.5))  # Simulate time taken to send data
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

print('All tasks have completed.')
