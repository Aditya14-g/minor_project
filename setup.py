import setuptools
# we are reading our README.md file here.
# Because if we want to publish this as a package in pypi website it will be use full.
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.1"

REPO_NAME = "If anybody is going to upload in his github they can write there repository name here."
AUTHOR_USER_NAME = "jokofi"
# This is inside our src file where every file is present.
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "jokofi222@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)