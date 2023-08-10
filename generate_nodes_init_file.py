import os
import pathlib

__all__ = ["generate_nodes_import_statements"]

NODES_PATH = pathlib.Path(__file__).parent.joinpath("flojoy_nodes")

badbadnotgood = ["VCTR.py", "__init__.py", ".DS_Store"]
ignore_folders = ["assets", "utils", "flojoy_nodes/nodes"]


def get_node_files():
    # List to store the file paths
    file_paths: list[str] = []
    for root, _, files in os.walk(NODES_PATH):
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


def generate_nodes_import_statements():
    node_files = get_node_files()
    import_statements: list[str] = list()
    for single_file in node_files:
        import_statement = make_import_statement(single_file[:-3])
        import_statements.append(import_statement)
    nodes_init_file = os.path.join(NODES_PATH, "nodes", "__init__.py")
    with open(nodes_init_file, "w") as init_file:
        init_file.write("\n".join(sorted(import_statements)))


def make_import_statement(file_path: str):
    module_location = (
        file_path[file_path.find("flojoy_nodes") + 13 :]
        .replace("\\", "/")
        .replace("/", ".")
    )
    module_name = module_location.split(".")[-1]
    if not module_name.isupper():
        return ""
    return f"from ..{module_location} import {module_name}"
