import os
import json
from typing import Any, Optional, Union
from .build_manifest import create_manifest
import pathlib

__all__ = ["generate_manifest"]

NODES_PATH = pathlib.Path(__file__).parent.parent

NAME_MAP = {
    "AI_ML": "AI & ML",
    "EXTRACTORS": "Extract",
    "GENERATORS": "Generate",
    "INSTRUMENTS": "I/O",
    "LOGIC_GATES": "Logic",
    "LOADERS": "Load",
    "TRANSFORMERS": "Transform",
    "VISUALIZERS": "Visualize",
    "NUMPY": "numpy",
    "LINALG": "np.linalg",
    "RANDOM": "np.rand",
    "SCIPY": "scipy",
    "SIGNAL": "sp.signal",
    "STATS": "sp.stats",
    "GAMES": "Games",
}

# Types that are allowed in the manifest, this is for styling in the frontend.
# A node will inherit the type of its parent if it is not in the allowed types.
ALLOWED_TYPES = [
    "AI_ML",
    "GENERATORS",
    "VISUALIZERS",
    "LOADERS",
    "EXTRACTORS",
    "TRANSFORMERS",
    "ARITHMETIC",
    "INSTRUMENTS",
    "LOGIC_GATES",
    "CONDITIONALS",
    "NUMPY",
    "GAMES",
    "SCIPY",
]

# Sort order in sidebar
ORDERING = [
    "AI_ML",
    "GENERATORS",
    "VISUALIZERS",
    "EXTRACTORS",
    "TRANSFORMERS",
    "LOADERS",
    "INSTRUMENTS",
    "LOGIC_GATES",
    "NUMPY",
    "SCIPY",
    "GAMES",
]

__failed_nodes: list[str] = []
__generated_nodes: list[str] = []


def browse_directories(
    dir_path: str, cur_type: Optional[str] = None, root_dir: str | None = None
):
    result: dict[str, Union[str, list[Any], None]] = {}
    basename = os.path.basename(dir_path)
    result["name"] = (
        "ROOT"
        if os.path.basename(dir_path) in ["flojoy_nodes"] + [root_dir]
        else NAME_MAP.get(basename, basename)
    )
    if result["name"] != "ROOT":
        result["key"] = basename

    result["children"] = []
    entries = sorted(
        os.scandir(dir_path), key=lambda e: e.name
    )  # Sort entries alphabetically

    for entry in entries:
        if entry.is_dir():
            if (
                entry.name.startswith(".")
                or entry.name.startswith("_")
                or entry.name == "assets"
                or entry.name == "utils"
                or entry.name == "MANIFEST"
                or "examples" in entry.path
                or "a1-[autogen]" in entry.path
                or "appendix" in entry.path
                or "flojoy_nodes/nodes" in entry.path.replace("\\", "/")
            ):
                continue
            cur_type = basename if basename in ALLOWED_TYPES else cur_type
            subdir = browse_directories(entry.path, cur_type)
            result["children"].append(subdir)
        elif entry.is_file() and entry.name.endswith(".py"):
            continue
    if not result["children"]:
        try:
            n_file_name = f"{os.path.basename(dir_path)}.py"
            n_path = os.path.join(dir_path, n_file_name)
            result = create_manifest(n_path)
            __generated_nodes.append(n_file_name)
        except Exception as e:
            print(
                "❌ Failed to generate manifest from ",
                f"{os.path.basename(dir_path)}.py ",
                e,
                "\n",
            )
            __failed_nodes.append(f"{os.path.basename(dir_path)}.py")

        if not result.get("type"):
            result["type"] = cur_type
        result["children"] = None

    return result


def sort_order(element):
    try:
        return ORDERING.index(element["key"])
    except ValueError:
        return len(ORDERING)


def deep_merge_dict(dict1: dict[str, Any], dict2: dict[str, Any]):
    result = dict1.copy()
    if not dict2["children"]:
        return result
    child = deep_merge_lists(dict1["children"], dict2["children"])
    result["children"] = child
    return result


def deep_merge_lists(list1: list[dict[str, Any]], list2: list[dict[str, Any]]):
    result = list1.copy()
    for item in list2:
        if any(item1["key"] == item["key"] for item1 in list1):
            item_index = next(
                (i for i, x in enumerate(list1) if x["key"] == item["key"]), -1
            )
            child = deep_merge_lists(list1[item_index]["children"], item["children"])
            result[item_index]["children"] = child
        else:
            result.append(item)
    return result


def generate_manifest(
    out_path: str, custom_nodes_path: str | None = None, root_dir: str | None = None
):
    nodes_map = browse_directories(NODES_PATH.__str__())
    nodes_map["children"].sort(key=sort_order)  # type: ignore
    if custom_nodes_path:
        custom_nodes_map = browse_directories(custom_nodes_path, root_dir=root_dir)
        print("custom_nodes_map", custom_nodes_map, flush=True)
        print("custom_nodes_map ch", custom_nodes_map["children"], flush=True)
        if custom_nodes_map["children"]:
            custom_nodes_map["children"].sort(key=sort_order)  # type: ignore
            nodes_map = deep_merge_dict(nodes_map, custom_nodes_map)
    print(
        f"✅ Successfully generated manifest from {__generated_nodes.__len__()} nodes !"
    )
    print(
        f"⚠️ {__failed_nodes.__len__()} nodes require upgrading to align with the new API!"
    )
    with open(out_path, "w") as f:
        f.write(json.dumps(nodes_map, indent=3))
        f.close()
