import sys
import pathlib

if sys.version_info < (3, 9):
    import importlib_resources as resources
else:
    import importlib.resources as resources


def export():
    return list(
        map(
            pathlib.Path,
            filter(
                lambda file: file.suffix == ".bin", resources.files(__name__).iterdir()
            ),
        )
    )
