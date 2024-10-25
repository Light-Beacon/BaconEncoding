from setuptools import setup, find_packages

setup(
    name = "baconencoding",
    version = "0.0.2",
    author = "Nattiden",
    author_email = " lightbeacon@bugjump.net",
    packages = find_packages(where="src"),
    package_dir = {"":"src"},
    entry_points = {
        'console_scripts': [
            'bacon = baconencoding.main:main'
        ]
    }
)