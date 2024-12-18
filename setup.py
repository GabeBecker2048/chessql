from setuptools import setup

# Read the contents of your requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="chessql",
    version="0.1.0",
    packages=["chessql"],
    include_package_data=True,
    install_requires=requirements,
    package_data={
        '': ['data/*.sql', 'data/*.ttf', 'data/img/*.png'],
    },
)
