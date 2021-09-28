import setuptools

setuptools.setup(
    name="AutoROM",
    package_dir={"AutoROM": "src"},
    packages=["AutoROM", "AutoROM.roms"],
    extras_require={"accept-rom-license": ["AutoROM.accept-rom-license"]},
    entry_points={
        "console_scripts": ["AutoROM=AutoROM:cli"],
        "ale_py.roms": ["AutoROM=AutoROM.roms:export"],
    },
    package_data={"AutoROM.roms": ["*.bin"]},
    include_package_data=True,
)
