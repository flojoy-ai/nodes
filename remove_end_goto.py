import os
import json

base_path = os.path.abspath(os.path.join(os.pardir, "nodes"))


def get_app_files(base_path: str):
    app_files = []
    for root, _, files in os.walk(base_path):
        for file in files:
            if file == "app.txt":
                app_files.append(os.path.join(root, file))
    return app_files


def remove_end_goto(app_files: list):
    for file in app_files:
        with open(file, "r") as f:
            lines = f.read()
            json_load = json.loads(lines)
            rf = json_load["rfInstance"]
            nodes = list(map(map_nodes, rf["nodes"]))
            #   nodes = list(filter(filter_end_from_nodes("END-"), rf['nodes']))
            #   edges = list(filter(filter_end_from_edges("END-"), rf['edges']))
            #   nodes = list(filter(filter_end_from_nodes("GOTO-"), nodes))
            #   edges = list(filter(filter_end_from_edges("GOTO-"), edges))
            json_load["rfInstance"]["nodes"] = nodes
            json_load["rfInstance"]["edges"] = rf["edges"]
            with open(file, "w") as app:
                app.write(json.dumps(json_load, indent=4))


import typing


def map_nodes(node: dict[str, typing.Any]):
    try:
        node["data"]["selected"] = False
        node["selected"] = False
    except Exception:
        pass
    return node


def filter_end_from_nodes(removal_id: str):
    def r(node: dict[str, typing.Any]):
        if node["id"].startswith(removal_id):
            return False
        return True

    return r


def filter_end_from_edges(removal_id: str):
    def r(edge: dict[str, typing.Any]):
        if edge["target"].startswith(removal_id) or edge["source"].startswith(
            removal_id
        ):
            return False
        return True

    return r


if __name__ == "__main__":
    app_files = get_app_files(base_path)
    remove_end_goto(app_files)
