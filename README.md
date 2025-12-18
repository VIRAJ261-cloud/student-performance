##  End to End Machine Learning Project
Learning 1:
Why do we need setup.py?
It helps to:
    Install your project using pip
    Share your code as a package
    Manage dependencies (required libraries)
    Define project info (name, version, author)

Learning 2:
The simple rule (most important)
📦 A folder is considered a Python package if it contains an __init__.py file
find_packages():
    Scans your project folders
    Finds folders with __init__.py
    Treats them as packages
    Includes them in your installation