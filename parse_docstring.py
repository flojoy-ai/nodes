import ast
import json
import os

from docstring_parser import parse

# Get the current directory
current_directory = os.getcwd()

# Walk through all the folders and files in the current directory
for root, dirs, files in os.walk(current_directory):
    # Iterate through the files
    for file in files:
        # Check if the file is a Python file and has the same name as the folder
        if file.endswith(".py") and file[:-3] == os.path.basename(root):
            # Construct the file path
            file_path = os.path.join(root, file)

            # Read the contents of the Python file
            with open(file_path, "r") as f:
                code = f.read()

            # Parse the code
            tree = ast.parse(code)

            # Find functions in the code
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    function_name = node.name

                    if function_name != os.path.basename(root):
                        # don't parse for any function that has a different
                        # name than the node file name
                        continue

                    # Extract docstring if available
                    if (
                        node.body
                        and isinstance(node.body[0], ast.Expr)
                        and isinstance(node.body[0].value, ast.Str)
                    ):
                        docstring = node.body[0].value.s

                        # Process the docstring using docstring_parser
                        parsed_docstring = parse(docstring)

                        if (
                            parsed_docstring.short_description
                            or parsed_docstring.long_description
                        ):
                            # Build the JSON data
                            json_data = {
                                "description": parsed_docstring.long_description,
                                "parameters": [
                                    {
                                        "name": param.arg_name,
                                        "type": param.type_name,
                                        "description": param.description,
                                    }
                                    for param in parsed_docstring.params
                                ],
                                "returns": [
                                    {
                                        "name": rtn.return_name,
                                        "type": rtn.type_name,
                                        "description": rtn.description,
                                    }
                                    for rtn in parsed_docstring.many_returns
                                ],
                            }

                            # Write the data to a JSON file in the same directory
                            output_file_path = os.path.join(root, "docstring.json")
                            with open(output_file_path, "w") as output_file:
                                json.dump(json_data, output_file, indent=2)

                            # sys.exit(0)
