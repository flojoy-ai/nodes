import json
import os

import pathlib

NODES_PATH = pathlib.Path(__file__).parent.parent

badbadnotgood = ["VCTR.py", "__init__.py", ".DS_Store"]
ignore_folders = ["assets", "utils", "flojoy_nodes/nodes"]


def get_node_files(path_to_nodes: str = NODES_PATH.__str__()):
    # List to store the file paths
    file_paths: list[str] = []
    for root, _, files in os.walk(path_to_nodes):
        for file in files:
            # Check if the file matches the pattern
            if any(
                folder_name in os.path.join(root, file.replace("\\", "/"))
                for folder_name in ignore_folders
            ):
                continue
            if file.endswith(".py") and "_test" not in file:
                # If it matches, add the full path to the list
                if file not in badbadnotgood:
                    file_paths.append(os.path.join(root, file))
    return file_paths


def write_metadata(out_path: str, custom_nodes_dir: str):
    node_files = get_node_files()
    custom_node_files = get_node_files(path_to_nodes=custom_nodes_dir)
    if custom_node_files:
        node_files = node_files + custom_node_files
    function_dict: dict[str, dict[str, str]] = dict()
    for single_file in node_files:
        with open(single_file) as f:
            data = {
                "metadata": f.read(),
                "path": single_file[single_file.find("nodes") + 6 :].replace("\\", "/"),
            }
            function_dict[os.path.basename(single_file)] = data

    s = json.dumps(obj=function_dict, indent=2)
    with open(out_path, "w") as out_file:
        out_file.write(s)
        out_file.write("\n")
