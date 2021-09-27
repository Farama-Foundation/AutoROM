import setuptools
import pathlib

from setuptools.command.install import install

class InstallCommand(install):
    def run(self):
        super().run()

        from AutoROM import main as AutoROM
        download_dir = pathlib.Path(self.install_lib) / "AutoROM" / "roms"
        download_dir.mkdir(exist_ok=False, parents=True)
        AutoROM(True, download_dir, False)


setuptools.setup(
    name="AutoROM.accept-rom-license",
    cmdclass={"install": InstallCommand},
)
