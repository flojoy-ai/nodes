This example shows a simple way to use the Feedback node within a Loop to access data from the previous iterations:


Read the docs for the [`LOOP`](https://github.com/flojoy-io/nodes/blob/main/LOGIC_GATES/LOOPS/LOOP/LOOP.py) node to understand how loops work within Flojoy.


In the application above the [`CONSTANT`](https://github.com/flojoy-io/nodes/blob/main/GENERATORS/SIMULATIONS/CONSTANT/CONSTANT.py) node is used to define a starting value (5 in this example), and an increment value (2) which will be added to the starting value during each iteration thanks to the [`ADD`](https://github.com/flojoy-io/nodes/blob/main/TRANSFORMERS/ARITHMETIC/ADD/ADD.py) node.


After that, the Visualization node [`BIG_NUMBER`](https://github.com/flojoy-io/nodes/blob/main/VISUALIZERS/PLOTLY/BIG_NUMBER/BIG_NUMBER.py) is called to display the result of the operation. The result will be updated after each iteration.


The parameter 'reffered_node' of the ['FEEDBACK'](https://github.com/flojoy-io/nodes/blob/main/GENERATORS/SIMULATIONS/FEEDBACK/FEEDBACK.py) node is set
to : [`ADD`](https://github.com/flojoy-io/nodes/blob/main/TRANSFORMERS/ARITHMETIC/ADD/ADD.py), to reuse the value stored during the previous iteration of the loop.


Thanks to the ['FEEDBACK'](https://github.com/flojoy-io/nodes/blob/main/GENERATORS/SIMULATIONS/FEEDBACK/FEEDBACK.py) node, the increment value is added to the previous result during each new iteration.
