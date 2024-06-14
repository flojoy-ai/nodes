import os
import shutil
import sys
import textwrap
import traceback

path = os.path

__generated_docs = []

N_PATH = "nodes/"
boilar_plates = {
    "notes.md": "No theory or technical notes have been contributed for this node yet.",
    "media.md": "No supporting screenshots, photos, or videos have been added to the media.md file for this node.",
    "hardware.md": "This node does not require any peripheral hardware to operate. Please see INSTRUMENTS for nodes that interact with the physical world through connected hardware.",
}


def get_common_md(node_file_path: str):
    return """
[//]: # (Custom component imports)

import DocString from '@site/src/components/DocString';
import DocStringJSON from '@site/src/components/DocStringJSON';

import PythonCode from '@site/src/components/PythonCode';
import AppDisplay from '@site/src/components/AppDisplay';
import SectionBreak from '@site/src/components/SectionBreak';
import AppendixSection from '@site/src/components/AppendixSection';

[//]: # (Docstring)

import DocstringSource from '!!raw-loader!./a1-[autogen]/docstring.txt';
import DocstringJson from '!!raw-loader!./a1-[autogen]/docstring.json';
import PythonSource from '!!raw-loader!./a1-[autogen]/python_code.txt';

<DocString>{{DocstringSource}}</DocString>
<DocStringJSON data={{DocstringJson}} />
<PythonCode GLink='{node_file_path}'>{{PythonSource}}</PythonCode>

<SectionBreak />

    """.format(
        node_file_path=node_file_path
    )


def get_md_example_section(node_label: str, node_path: str):
    return """

[//]: # (Examples)

## Examples

<AppDisplay 
  GLink='{node_path}'
  nodeLabel='{node_label}'>
</AppDisplay>

<SectionBreak />

    """.format(
        node_label=node_label, node_path=node_path
    )


def get_appendix_section(appendix_folder_path: str):
    return """

[//]: # (Appendix)

import Notes from './appendix/notes.md';
import Hardware from './appendix/hardware.md';
import Media from './appendix/media.md';

## Appendix

<AppendixSection index={{0}} folderPath='{appendix_folder_path}'><Notes /></AppendixSection>
<AppendixSection index={{1}} folderPath='{appendix_folder_path}'><Hardware /></AppendixSection>
<AppendixSection index={{2}} folderPath='{appendix_folder_path}'><Media /></AppendixSection>


""".format(
        appendix_folder_path=appendix_folder_path
    )


def get_md_file_content(file_path: str, node_label: str):
    file_dir, _ = path.split(file_path)
    nodes_index = file_dir.replace("\\", "/").rfind(N_PATH)
    node_path = file_dir[nodes_index:].replace("\\", "/").replace(N_PATH, "")
    node_file_path = (
        file_path[nodes_index:]
        .replace("\\", "/")
        .replace(N_PATH, "")
        .replace(".md", ".py")
    )
    appendix_folder_path = path.join(file_dir[nodes_index:], "appendix/").replace(
        "\\", "/"
    )

    common_section = get_common_md(node_file_path)

    example_section_default = get_md_example_section(
        node_label=node_label, node_path=node_path
    )

    appendix_section = get_appendix_section(appendix_folder_path=appendix_folder_path)

    return common_section + example_section_default + appendix_section


def write_file_recursive(file_path: str, content: str):
    # Split the path into directory and file name
    directory, _ = path.split(file_path)

    # Create directories recursively if they don't exist
    os.makedirs(directory, exist_ok=True)

    # Write the file
    with open(file_path, "w") as file:
        file.write(content)


def compare_two_str(first_str: str, second_str: str) -> bool:
    return first_str.replace("\n", "").replace(" ", "") != second_str.replace(
        "\n", ""
    ).replace(" ", "")


def get_content(file_path: str):
    c = ""
    with open(file_path, "r", encoding="utf-8") as opened_file:
        c = opened_file.read()
    return c


def process_python_file(input_file_path: str, output_path: str):
    input_dir, input_file_name = path.split(input_file_path)
    node_name = input_file_name.replace(".py", "")
    if not node_name.isupper():  # all node file names should be in upper case
        return
    try:
        node_content = get_content(input_file_path)

        # Extract docstring
        docstring = extract_docstring(node_content)

        # Extract function code
        function_code = extract_function_code(node_content)
        autogen_dir_name = "a1-[autogen]"

        # Write docstring to a file
        docstring_file_path = path.join(output_path, autogen_dir_name, "docstring.txt")
        write_to_docs(content=docstring, file_path=docstring_file_path, docstring=True)
        shutil.copy(
            f"{os.path.dirname(input_file_path)}/docstring.json",
            f"{output_path}/{autogen_dir_name}/",
        )

        # Write function code to a file
        function_code_file_path = path.join(
            output_path, autogen_dir_name, "python_code.txt"
        )
        write_to_docs(content=function_code, file_path=function_code_file_path)

        md_file_path = path.join(output_path, f"{node_name}.md")
        # appendix
        appendix_dir_path = path.join(output_path, "appendix")
        for f in ["hardware.md", "media.md", "notes.md"]:
            if not path.exists(path.join(appendix_dir_path, f)):
                write_file_recursive(path.join(appendix_dir_path, f), boilar_plates[f])
            else:
                c = get_content(path.join(appendix_dir_path, f))
                if c.strip() == "":
                    c = boilar_plates[f]
                write_file_recursive(path.join(appendix_dir_path, f), c)

        # examples
        example_dir_path = path.join(output_path, "examples", "EX1")
        for f in ["app.json", "example.md"]:
            f_path = path.join(input_dir, f)
            if path.exists(f_path):
                c = get_content(f_path)
                if not path.exists(path.join(example_dir_path, f)):
                    write_file_recursive(path.join(example_dir_path, f), c)
                else:
                    if f == "app.json":
                        existing_c = get_content(path.join(example_dir_path, f))
                        diff = compare_two_str(c, existing_c)
                        if diff:
                            write_file_recursive(path.join(example_dir_path, f), c)

        # write md file with file name
        md_file_content = get_md_file_content(md_file_path, node_name)
        if not path.exists(md_file_path):
            write_file_recursive(md_file_path, md_file_content)
            __generated_docs.append(node_name)

    except Exception as e:
        print(
            f"failed to write doc for {node_name}, input path: {input_file_path} ",
            e,
            traceback.format_exc(),
        )


def write_to_docs(content: str, file_path: str, docstring: bool = False):
    if not path.exists(file_path):
        write_file_recursive(
            file_path, textwrap.dedent(content) if docstring else content
        )
    else:
        doc_str = get_content(file_path)
        diff = compare_two_str(content, doc_str)
        if diff:
            write_file_recursive(
                file_path, textwrap.dedent(content) if docstring else content
            )


def extract_docstring(content: str):
    # Find the start and end of the docstring
    if '"""' in content:
        docstring_start = content.find('"""')
        docstring_end = content.find('"""', docstring_start + 3)

        # Extract the docstring
        docstring = content[docstring_start + 3 : docstring_end]

        return docstring
    elif "'''" in content:
        docstring_start = content.find("'''")
        docstring_end = content.find("'''", docstring_start + 3)

        # Extract the docstring
        docstring = content[docstring_start + 3 : docstring_end]

        return docstring
    return ""


def extract_function_code(content: str):
    # Find the start of the function code
    docstring = extract_docstring(content)
    content = content.replace(docstring, "").replace('"""', "")

    return content


nodes_dir = path.abspath(path.curdir)


def write_doc(docs_dir: str):
    file_path = None
    for root, _, files in os.walk(nodes_dir):
        for file in files:
            if (
                file.endswith(".py")
                and "test" not in file
                and file.split(".py")[0] != "__init__"
            ):
                path_index = nodes_dir.rfind("nodes")
                path_from_second_dir = root[path_index:]
                docs_file_path = path.join(docs_dir, path_from_second_dir)
                file_path = path.join(root, file)
                process_python_file(file_path, docs_file_path)


docs_dir = ""
if __name__ == "__main__":
    docs_dir_path = sys.argv[1]
    docs_dir = path.abspath(path.join(docs_dir_path, "docs"))
    print("docs dir: ", docs_dir)
    write_doc(docs_dir=docs_dir)
    if __generated_docs:
        print(f"Generated new docs for: {', '.join(__generated_docs)}")
