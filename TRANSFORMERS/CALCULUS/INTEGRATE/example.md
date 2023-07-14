In this example, `LINSPACE` and `RAND` nodes generate two lists (the `Ordered_pair` composed of x and y) that are required for the `INTEGRATE` node.

Then `INTEGRATE` node computes its integration using trapezoidal rule on the given input lists.

With the two `LINE` nodes we can see that the one showing the integrate function indeed represent the variation of the area under the curve of the original function as expected.
