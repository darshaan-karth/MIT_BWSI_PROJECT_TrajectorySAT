from picamera2 import Picamera2
import time

INFO_msg = "\033[92m[INFO]\033[0m "                             # Green color code for information messages
ERROR_msg = "\033[91m[ERROR]\033[0m "                           # Red color code for error information message 
FOLDER_PATH = "Images"

picam2 = Picamera2()
preview_config = picam2.create_preview_configuration()
picam2.start()

def img_gen(img_location):
    """
    This function generates a new image name.

    Parameters:
        img_location (str): location of the image taken.
    """
    t = time.strftime("_%H%M%S")
    imgname = (f'{FOLDER_PATH}/{img_location}{t}.jpg')
    return(imgname)

while True:
    #Generating unique image file name
    print(INFO_msg + "Generating unique image file path")
    ADD_PATH = img_gen("dls")

    #Capturing the image and saving it in the path stated in ADD_PATH
    print(INFO_msg + "Capturing and saving the image to the set path")
    picam2.capture_file(ADD_PATH)

    time.sleep(0.1)