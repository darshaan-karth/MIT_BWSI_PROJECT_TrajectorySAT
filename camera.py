from picamera2 import Picamera2

picam2 = Picamera2()
preview_config = picam2.create_preview_configuration()
picam2.start()

# Capture an image as a numpy array
array = picam2.capture_file("test.jpg")