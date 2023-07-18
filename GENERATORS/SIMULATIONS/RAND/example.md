In this example, the `LINSPACE` node is used to generate a large number of samples (2000) in this case, which is then passed on to `RAND` node to generate 
a list of random numbers with a normal (or Gaussian) distribution.

A `SCATTER` Viz node is then used to show the randomly generated numbers. With the x-axis being the sample number, and y-axis being the random value.

The distribution of the random numbers can be plotted with `HISTOGRAM`, and as expected of a Gaussian distribution,
the output of the `HISTOGRAM` node converges towards a bell curve.