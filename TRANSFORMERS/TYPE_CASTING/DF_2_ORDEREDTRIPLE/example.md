In this example, we use the nodes `R_DATASET` and `DF_2_ORDEREDTRIPLE`. The parameters of these nodes use in this example are the following:

`R_DATASET` : airquality

`DF_2_ORDEREDTRIPLE` : x=5, y=4, z=3

Here the airquality dataset have 6 columns in total and using these parameters we will generate an OrderedTriple with the column x, y and z corresponding to the 3 last ones as described higher in the parameters. 

We can see the node effect by observing the difference between the two `TABLE` nodes where the table showing the resulting OrderedTriple name the columns x and y instead of there previous name and the column values are different from the one of the previous table as expected since we select different columns. Then comparing the `SCATTER3D` nodes we can see that the the graph are different as expected since the first one show the graph of the 3 first columns and the one showing the resulting OrderedTriple use the 3 last columns.