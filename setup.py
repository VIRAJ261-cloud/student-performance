from setuptools import find_packages,setup
HYPEN_E_DOT = "-e ."
def get_library(filePath):
    with open(filePath,'r',encoding='utf-8') as f:
        content = f.read()
        f.close()
        a =content.split("\n")
        if HYPEN_E_DOT in a:
            a.remove(HYPEN_E_DOT)
        return a

setup(
    name="MLProject",
    version='0.0.0',
    author="Viraj",
    author_email="virajvwankhede2610@gmail.com",
    packages=find_packages(),
    install_requires = get_library("C:\\Projects\\DataScienceEndToEnd\\student-performance\\requirements.txt")
)
