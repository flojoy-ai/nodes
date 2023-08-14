import os
from importlib import import_module
import pathlib

__all__ = ["get_module_func", "create_map"]

NODES_PATH = pathlib.Path(__file__).parent.parent

mapping = {}


def get_module_func(file_name: str):
    if not mapping:
        create_map()
    file_path = mapping.get(file_name)

    if file_path is not None:
        module = import_module(file_path)
        return module

    else:
        print(f"File {file_name} not found in subdirectories of {NODES_PATH}")


def create_map():
    print("creating a node mapping")
    for root, _, files in os.walk(NODES_PATH):
        if root == NODES_PATH:
            continue

        for file in files:
            # map file name to file path
            if file.endswith(".py"):
                mapping[file[:-3]] = "flojoy_nodes." + (
                    os.path.join(root[root.find("nodes") + 6 :], file[:-3])
                    .replace("/", ".")
                    .replace("\\", ".")
                )
