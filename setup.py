import setuptools
with open("README.md", "r", encoding="utf=8") as f:
    long_description = f.read()
__version__ = "0.0.0"
REPO_NAME= "cnnClassfier"
AUTHOR_USER_NAME= "nitin"
SRC_REPO = "cnnClassfier"
AUTHOR_EMAIL = "nitiniyer.95@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="CNN Classifier",
    long_description=long_description,
    long_description_content="text/markdown",
    url="https://github.com/nitin0533/Disease-Classification-with-DVC",
    project_urls={
        "Bug Tracker": "https://github.com/nitin0533/Disease-Classification-with-DVC/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)