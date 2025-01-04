from git import Repo

INFO_msg = "\033[92m[INFO]\033[0m "
ERROR_msg = "\033[91m[ERROR]\033[0m "

REPO_PATH = "~/MIT_BWSI_PROJECT"     #Your github repo path: ex. /home/pi/FlatSatChallenge
FOLDER_PATH = "Images/"   #Your image folder path in your GitHub repo: ex. /Images

def git_push():
    """
    This function is complete. Stages, commits, and pushes new images to your GitHub repo.
    """
    try:
        ADD_PATH = FOLDER_PATH + "test.jpg"
        
        repo = Repo(REPO_PATH)
        origin = repo.remote('origin')
        print(INFO_msg + 'Added repo remote')
        origin.pull()
        print(INFO_msg + 'Pulled changes to the repo')
        repo.index.add(ADD_PATH)
        repo.index.commit('Test Photo Upload Function')
        origin.push()
        print(INFO_msg + 'Commited and Pushed Images')
    except:
        print(ERROR_msg + 'Problem with uploading the file to git')

git_push()