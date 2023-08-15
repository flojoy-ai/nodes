import os, shutil
import traceback
import sys
import textwrap


path = os.path

N_PATH = "nodes/"


def get_md_file_content(
    file_path: str, node_label: str, has_example: bool, example_section: str
):
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

    common_section = """
[//]: # (Custom component imports)

import DocString from '@site/src/components/DocString';
import PythonCode from '@site/src/components/PythonCode';
import AppDisplay from '@site/src/components/AppDisplay';
import SectionBreak from '@site/src/components/SectionBreak';
import AppendixSection from '@site/src/components/AppendixSection';

[//]: # (Docstring)

import DocstringSource from '!!raw-loader!./a1-[autogen]/docstring.txt';
import PythonSource from '!!raw-loader!./a1-[autogen]/python_code.txt';

<DocString>{{DocstringSource}}</DocString>
<PythonCode GLink='{node_file_path}'>{{PythonSource}}</PythonCode>

<SectionBreak />

    """.format(
        node_file_path=node_file_path
    )

    example_section_default = """

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

    appendix_section = """

[//]: # (Appendix)

import Notes from '!!raw-loader!./appendix/notes.md';
import Hardware from '!!raw-loader!./appendix/hardware.md';
import Media from '!!raw-loader!./appendix/media.md';

## Appendix

<AppendixSection index={{0}} folderPath='{appendix_folder_path}'>{{Notes}}</AppendixSection>
<AppendixSection index={{1}} folderPath='{appendix_folder_path}'>{{Hardware}}</AppendixSection>
<AppendixSection index={{2}} folderPath='{appendix_folder_path}'>{{Media}}</AppendixSection>


""".format(
        appendix_folder_path=appendix_folder_path
    )

    return (
        common_section + example_section + appendix_section
        if has_example
        else common_section + example_section_default + appendix_section
    )


def get_example_section(node_label: str, has_app_image: bool, has_output_image: bool):
    app_image = "import appImg from './examples/EX1/app.jpeg'" if has_app_image else ""
    output_image = (
        "import outputImg from './examples/EX1/output.jpeg'" if has_output_image else ""
    )
    app_image_val = "{appImg}" if has_app_image else "{''}"
    output_image_val = "{outputImg}" if has_output_image else "{''}"
    example_section = """

[//]: # (Examples)

## Examples

import Example1 from './examples/EX1/example.md';
import App1 from '!!raw-loader!./examples/EX1/app.json';
{app_image}
{output_image}

<AppDisplay 
    nodeLabel='{node_label}'
    appImg={app_image_val}
    outputImg={output_image_val}
    >
    {{App1}}
</AppDisplay>

<Example1 />

<SectionBreak />
  
    """.format(
        node_label=node_label,
        app_image=app_image,
        output_image=output_image,
        app_image_val=app_image_val,
        output_image_val=output_image_val,
    )
    return example_section


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
        content = get_content(input_file_path)

        # Extract docstring
        docstring = extract_docstring(content)

        # Extract function code
        function_code = extract_function_code(content)
        autogen_dir_name = "a1-[autogen]"
        # Write docstring to a file
        docstring_file_path = path.join(output_path, autogen_dir_name, "docstring.txt")
        if not path.exists(docstring_file_path):
            write_file_recursive(docstring_file_path, textwrap.dedent(docstring))
        else:
            doc_str = get_content(docstring_file_path)
            diff = compare_two_str(docstring, doc_str)
            if diff:
                write_file_recursive(docstring_file_path, textwrap.dedent(docstring))

        # Write function code to a file
        function_code_file_path = path.join(
            output_path, autogen_dir_name, "python_code.txt"
        )
        if not path.exists(function_code_file_path):
            write_file_recursive(function_code_file_path, function_code)
        else:
            func_str = get_content(function_code_file_path)
            diff = compare_two_str(func_str, function_code)
            if diff:
                write_file_recursive(function_code_file_path, function_code)

        # appendix
        appendix_dir_path = path.join(output_path, "appendix")
        for f in ["hardware.md", "media.md", "notes.md"]:
            if not path.exists(path.join(appendix_dir_path, f)):
                write_file_recursive(path.join(appendix_dir_path, f), "")
            else:
                lines = [
                    {
                        "prev": "./appendix/notes.md",
                        "new": "!!raw-loader!./appendix/notes.md",
                    },
                    {
                        "prev": "./appendix/hardware.md",
                        "new": "!!raw-loader!./appendix/hardware.md",
                    },
                    {
                        "prev": "./appendix/media.md",
                        "new": "!!raw-loader!./appendix/media.md",
                    },
                ]
                md_file_path = path.join(
                    output_path, path.basename(input_file_path).replace(".py", ".md")
                )
                if path.exists(md_file_path):
                    c = get_content(md_file_path)
                    for line in lines:
                        if line["new"] not in c:
                            c = c.replace(line["prev"], line["new"])
                    write_file_recursive(md_file_path, c)

        # examples
        has_example = False
        example_dir_path = path.join(output_path, "examples", "EX1")
        # for f in ["app.json", "example.md"]:
        for f in ["app.json"]:
            if path.exists(path.join(input_dir, f)):
                has_example = True
                c = get_content(path.join(input_dir, f))
                if not path.exists(path.join(example_dir_path, f)):
                    write_file_recursive(path.join(example_dir_path, f), c)
                else:
                    existing_c = get_content(path.join(example_dir_path, f))
                    diff = compare_two_str(c, existing_c)
                    if diff:
                        write_file_recursive(path.join(example_dir_path, f), c)
            else:
                has_example = False

        # write md file with file name
        # md_file_path = path.join(output_path, f"{node_name}.md")
        # app_jpg = "app.jpeg"
        # output_jpg = "output.jpeg"
        # img_map = {app_jpg: False, output_jpg: False}
        # for f in [app_jpg, output_jpg]:
        #     img_path = path.join(input_dir, f)
        #     if path.exists(img_path):
        #         shutil.copy2(img_path, path.join(example_dir_path, f))
        #         img_map[f] = True

        # example_section = get_example_section(
        #     node_name,
        #     has_app_image=img_map[app_jpg],
        #     has_output_image=img_map[output_jpg],
        # )
        # md_file_content = get_md_file_content(
        #     md_file_path,
        #     node_name,
        #     has_example=has_example,
        #     example_section=example_section,
        # )
        # if not path.exists(md_file_path):
        #     write_file_recursive(md_file_path, md_file_content)
        # else:
        #     if path.exists(path.join(example_dir_path, "app.json")) and has_example:
        #         write_file_recursive(md_file_path, md_file_content)
    except Exception as e:
        print(
            f"failed to write doc for {node_name}, input path: {input_file_path} ",
            e,
            traceback.format_exc(),
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
    print(" docs dir: ", docs_dir)
    write_doc(docs_dir=docs_dir)
