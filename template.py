import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",

]


for filepath in list_of_files:
    filepath = Path(filepath)
    # we are doing this to saperate our folders and files we will first create our folders then our files.
    filedir, filename = os.path.split(filepath)

# if filedir is empty it means there is not file or folder so we will not run the if condition.
    if filedir != "":
        # in this line of code it will make us folder if it don't exist if it exist it will not create the folder.
        os.makedirs(filedir, exist_ok=True)
        # want to see my log info in my terminal.
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    # checking if file exits or not||we are also checking the size of the file.
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # we are opening file in writing mode 'w' denotes writing mode.
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")
