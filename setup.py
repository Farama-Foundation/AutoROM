import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AutoROM",
    version="0.3.0",
    author="PettingZoo Team",
    author_email="justinkterry@gmail.com",
    description="Automated installation of Atari ROMs for Gym/ALE-Py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PettingZoo-Team/AutoROM",
    keywords=["Reinforcement Learning", "game", "RL", "AI", "gym"],
    packages=setuptools.find_packages(),
    install_requires=[
        "click",
        "requests",
        "tqdm",
        'importlib-resources; python_version < "3.9"',
    ],
    entry_points={
        "console_scripts": ["AutoROM=AutoROM:main"],
    },
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
