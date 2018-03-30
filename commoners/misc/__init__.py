import yaml
import pickle
import hashlib


def load_yaml(path):
    with open(path, "r") as fi:
        yml = yaml.load(fi)

        return yml

load_config = load_yaml


def to_pickle(obj, path):
    with open(path, "wb") as fp:
        pickle.dump(obj, fp)


def unpickle(path):
    with open(path, "rb") as fi:
        return pickle.load(fi)


def hash256(s):
    return hashlib.sha256(s.encode()).hexdigest()


def hash512(s):
    return hashlib.sha512(s.encode()).hexdigest()
