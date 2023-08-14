In this example, `LINSPACE` is used to generate a list of 2000 samples, it is then passed onto the `RAND` node,
which randomizes the values within the list with a normal (or Gaussian) distribution.

The distribution is then plotted with `HISTOGRAM` and as expected of a Gaussian distribution,
the output of the `HISTOGRAM` node converges towards a bell curve.

There's also a `RAND` node with no inputs, in which case a single number would be generated, which is displayed by `BIG_NUMBER` in this example.
