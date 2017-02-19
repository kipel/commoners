import yaml


def load_yaml(path):
    with open(path, "r") as fi:
        yml = yaml.load(fi)

        return yml

load_config = load_yaml
