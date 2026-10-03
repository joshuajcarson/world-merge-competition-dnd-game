"""Load tools/image-gen/config.yaml."""
import pathlib

import yaml

DEFAULT_CONFIG_PATH = pathlib.Path(__file__).parent / "config.yaml"


def load_config(path=None):
    path = pathlib.Path(path) if path else DEFAULT_CONFIG_PATH
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)
