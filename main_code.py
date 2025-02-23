"""
The Python code you will write for this module should read
acceleration data from the IMU. When a reading comes in that surpasses
an acceleration threshold (indicating a shake), your Pi should pause,
trigger the camera to take a picture, then save the image with a
descriptive filename. You may use GitHub to upload your images automatically,
but for this activity it is not required.

The provided functions are only for reference, you do not need to use them. 
You will need to complete the take_photo() function and configure the VARIABLES section
"""

#import libraries
import time
import board
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX as LSM6DS
from adafruit_lis3mdl import LIS3MDL
from git import Repo
from picamera2 import Picamera2

#camera_on = False
camera_on = True

#GLOBAL VARIABLES
interval = 0.1                                                  # The approx. duration before measureing the position of the cubesat    
image_location = "tx"                                           # Location of the image taken for saving it as a part of the image file name
INFO_msg = "\033[92m[INFO]\033[0m "                             # Green color code for information messages
ERROR_msg = "\033[91m[ERROR]\033[0m "                           # Red color code for error information message 
accuracy = 2                                                    # The decimal places for setting the threshold accuracy by rounding 
(X_THRESHOLD, Y_THRESHOLD, Z_THRESHOLD) = (-0.03, 0.31, -9.6)      # Any desired value from the accelerometer
REPO_PATH = "/MIT_BWSI_PROJECT"                                 # Your github repo path: ex. /home/pi/FlatSatChallenge
FOLDER_PATH = "Images"                                          # Your image folder path in your GitHub repo: ex. /Images

#IMU initialization for I2C Access
i2c = board.I2C()
accel_gyro = LSM6DS(i2c)
mag = LIS3MDL(i2c)

#PiCamera preview configuration
picam2 = Picamera2()
preview_config = picam2.create_preview_configuration()
picam2.start()

def git_push(ADD_PATH):
    """
    This function stages, commits, and pushes new images to your GitHub repo.
    
    Parameters:
        ADD_PATH (str): path of the image file to commit and push.

    Raise:
        [ERROR] Problem with uploading the file to git
    """
    try:
        repo = Repo(REPO_PATH)
        print(repo)
        origin = repo.remote('origin')
        print(INFO_msg + 'Added repo remote')
        origin.pull()
        print(INFO_msg + 'Pulled changes to the repo')
        repo.index.add(ADD_PATH)
        repo.index.commit('Image file uploaded at {}'.format(time.strftime("%H:%M:%S")))
        origin.push()
        print(INFO_msg + 'Commited and Pushed Images')
    except Exception as e:
        print(ERROR_msg + 'Problem with uploading the file to git')
        print(e)

def img_gen(img_location):
    """
    This function generates a new image name.

    Parameters:
        img_location (str): location of the image taken.

    Raise:
        None
    """
    t = time.strftime("_%H%M%S")
    imgname = (f'{FOLDER_PATH}/{img_location}{t}.jpg')
    return(imgname)


def take_photo():
    """
    This function takes a photo when the FlatSat is shaken.
    """
    while True:
        accelx, accely, accelz = accel_gyro.acceleration
        print("| accelx : {} || accely : {} || accelz : {} |".format(round(accelx, 3), round(accely, 3), round(accelz, 3)))
        if (True or ((round(accelx, accuracy) >= X_THRESHOLD)  and (round(accely, accuracy) >= Y_THRESHOLD)  and (round(accelz, accuracy) >= Z_THRESHOLD) )):
            print(INFO_msg + "Close to the target attitude of the cubesat")
            time.sleep(interval/2)

            if (camera_on == True):
                #Generating unique image file name
                print(INFO_msg + "Generating unique image file path")
                ADD_PATH = img_gen(image_location)

                #Capturing the image and saving it in the path stated in ADD_PATH
                print(INFO_msg + "Capturing and saving the image to the set path")
                picam2.capture_file(ADD_PATH)

                #Commiting and Pushing the Image file
                git_push(ADD_PATH=ADD_PATH)

        time.sleep(interval/2)

def main():
    take_photo()

if __name__ == '__main__':
    main()
