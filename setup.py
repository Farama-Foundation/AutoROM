import setuptools
import os

here = os.path.dirname(os.path.abspath(__file__))

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
    install_requires=f"""
        click
        requests
        tqdm
        importlib-resources; python_version < "3.9"
    """,
    extras_require={
        "accept-rom-license": [
            # We have to specify an absolute path for the time being.
            # This will be fixed by: https://github.com/pypa/pip/issues/6658
            # which is held up on pypa/packaging because of the stdlib urlparse.
            # For the time being we'll need to patch .egg-info/requires.txt to the
            # relative directory so we don't include the abspath of the build machine.
            f"AutoROM-licensed-roms @ file://localhost/{os.path.join(here, 'AutoROM', 'licensed')}"
        ]
    },
    entry_points={
        "console_scripts": ["AutoROM=AutoROM:cli"],
        "ale_py.roms": ["AutoROM=AutoROM.roms:export"]
    },
    zip_safe=False,
    package_data={
        "AutoROM.roms": ["*.bin"]
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
