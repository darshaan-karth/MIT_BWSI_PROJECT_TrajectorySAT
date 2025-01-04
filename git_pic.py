import time
from git import Repo

REPO_PATH = "darshaan-karth/MIT_BWSI_PROJECT"     #Your github repo path: ex. /home/pi/FlatSatChallenge
FOLDER_PATH = "/Images"   #Your image folder path in your GitHub repo: ex. /Images

def git_push():
    """
    This function is complete. Stages, commits, and pushes new images to your GitHub repo.
    """
    try:
        repo = Repo(REPO_PATH)
        origin = repo.remote('origin')
        print('added remote')
        origin.pull()
        print('pulled changes')
        repo.git.add(REPO_PATH + FOLDER_PATH)
        repo.index.commit('New Photo')
        print('made the commit')
        origin.push()
        print('pushed changes')
    except:
        print('Couldn\'t upload to git')


def img_gen(name):
    """
    This function is complete. Generates a new image name.

    Parameters:
        name (str): your name ex. MasonM
    """
    t = time.strftime("_%H%M%S")
    imgname = (f'{REPO_PATH}{FOLDER_PATH}/{name}{t}.jpg')
    return imgname


