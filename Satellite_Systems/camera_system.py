from git import Repo
from picamera2 import Picamera2
import time

def git_push(REPO_PATH, img_path):
    """
    This function stages, commits, and pushes new images to your GitHub repo.
    
    Parameters:
        img_path (str): path of the image file to commit and push.
    """
    try:
        repo = Repo(REPO_PATH)
        origin = repo.remote('origin')
        origin.pull()
        repo.index.add(img_path)
        repo.index.commit('Image file uploaded at {}'.format(time.strftime("%H:%M:%S")))
        origin.push()
    except Exception as e:
        return(e)

def img_gen(FOLDER_PATH):
    """
    This function generates a new image name.

    Parameters:
        img_location (str): location of the image taken.
    """
    t = time.strftime("_%H%M%S")
    imgname = (f'{FOLDER_PATH}/image{t}.jpg')
    return(imgname)

def take_photo(FOLDER_PATH):
    """
    This function takes a photo when the FlatSat is shaken.
    """
    #PiCamera preview configuration
    picam2 = Picamera2()
    preview_config = picam2.create_preview_configuration()
    picam2.start()

    #Capturing the image and saving it in the path stated in ADD_PATH
    ADD_PATH = img_gen(FOLDER_PATH)
    picam2.capture_file(ADD_PATH)
    return(ADD_PATH)

def main(push = False):  
    REPO_PATH = "/MIT_BWSI_PROJECT"  
    FOLDER_PATH = "../Images"

    img_path = take_photo(FOLDER_PATH)
    if (push):
        git_push(REPO_PATH=REPO_PATH, img_path=img_path)

if __name__ == '__main__':
    main()
