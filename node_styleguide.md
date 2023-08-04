# Python `NODE` style guide

## Docstrings

**Every node should have a docstring.** Docstring are used to generated the "Node description" preamble of a node's documentation page. 
Available node parameters should be spelled out using numpy's convention for list parameters:
```
Parameters
----------
x : type
    Description of parameter `x`.
y
    Description of parameter `y` (with type not specified).
```
(see https://numpydoc.readthedocs.io/en/latest/format.html#parameters)

Eventually, we may use the `Parameters` section of a node's docstring to auto-create the parameter manifest file. (@corinaldi is investigation)

Docstrings should with, "The x node ...", where x is the name of the node in all caps. For example:

```
The ADD node can be used to add 2 or more numeric arrays, matrices, dataframes, or constants element-wise. When a constant is added to an array or matrix, each element in the array or matrix will be increased by the constant value. If 2 arrays or matrices of different sizes are added, the output will be the size of the larger array or matrix with only the overlapping elements changed.
```

## Unit testing

### Overview

All nodes need to be unit-tested using the `pytest` framework (https://docs.pytest.org/en/stable/). A test script should be added in the same directory as the node itself, and should be named `<node_name>_test_.py`. For example, the `ADD` node should have a corresponding `ADD_test_.py` file. 

The test script should contain at least 1 test function, named `test_<node_name>`. For example, the `ADD` node should have a corresponding `test_ADD` function. 

There exists a `mock_flojoy_decorator` fixture (in `conftest.py`) that can be re-used in any test to mock the `@flojoy` decorator. This is useful for testing nodes outside of `studio`. To use the `mock_flojoy_decorator` object, supply it as an argument to your test function. For example:

```python
# ADD_test_.py

import pytest

def test_ADD(mock_flojoy_decorator):
    import ADD

    assert ADD.ADD(1, 2) == 3
```

**IMPORTANT** Additionally, if the node under test writes to the Flojoy cache directory (`~/.flojoy`), PLEASE use the `cleanup_flojoy_cache_fixture` fixture (present in `conftest.py`). Any cache written by your test will then be cleaned up once the test finishes running, and that ensures CI testing will not crash due to excessive disk volume usage.

### Best practices

1. Test the node with a variety of inputs, and try to cover multiple test cases.
2. Feel free to include files to help with testing. For example, if your node is supposed to work with images, add a test image to the same directory as the test script, run it through your test and check for the expected output.
3. Your test should run successfully in our CI/CD pipeline. If you're not sure how to do this, please open an issue.
4. Feel free to mock out any moving part of the node that you don't need to test or that you can't test. For example, if your node requires a remote API, make sure to mock that out in your test. You do not want to be making API calls in your test.
5. Always test your code locally before pushing it to the repo, this will save you time.

For further information on testing, please refer to this great tutorial by RealPython: https://realpython.com/pytest-python-testing/


## Node naming

Node names should always appear in `ALL_CAPS`, using `code` styling when available. Words should be seperated with underscores. Because node names need to appear on node GUI elements, node name length should be optimized for shortness and never more than 20 characters.
- Node function name, Node file name and Node key in the manifest file must be the same. Because it helps studio frontend to construct correct GitHub path for each node.
- Folders in nodes directory should not contain any space. Words should be separated by using `_` underscore.
- The category folder name should follow it's key from [`COMMAND_TREE` here](https://github.com/flojoy-io/studio/blob/develop/src/utils/ManifestLoader.ts#L89)

## Ease of use

Nodes should be forgiving in terms of their input and ouutput parameters. Flojoy's target audience is engineers and technicians who may not know anything about Python - we want to create a productive, supportive UX for them.

### Weak typing

The first arg that the @flojoy decorator injects into a node function is always a `DataContainer` object with a `type` key set to one of the following:
- `ordered_pair`
- `ordered_triplet`
- `image` (a color image encoded in 3 R/G/B matrices)
- `greyscale` (a greyscale image incoded in 1 matrix)
- `timeseries`
- `constant` (TODO: rename to `scalar`)
- `matrix` (eg, from numpy)
- `dataframe` (eg, from pandas)
- `plotly` (a plotly object)

Nodes should try to accomodate any reasonable combination of inputs that a first-time Flojoy Studio user might try. 

For example, the `ADD` node should make a best effort to do something reasonable when a matrix is added to a dataframe, or a 2 matrices of a different size are added.

### Variable number of inputs

Where possible and reasonable, nodes should be able to accept a variable number of inputs. For example, the `ADD` node should be able to accept 2-N inputs.

## Code style

When finished writing your node, please use `black` (https://github.com/psf/black) and PEP8 to ensure code style uniformity and readability between nodes.

## Node categories

Node categories (such as DATA > GENERATORS > SIMULATION) should always be in ALL_CAPS with underscores seperating words. Categories may change and shift as more nodes are added to the standard corpus.

There are 2 top-level node categories:
- Standard nodes (manually written by humans)
- Library nodes (machine generated by introspection of Python libraries like numpy, sklearn, etc)

## Visualization and control nodes

Unlike other nodes, visualization and control nodes require adding a component on the frontend to display the visualization object or control widget. In other words, they require working knowledge of Typescript/React in addition to Python.







