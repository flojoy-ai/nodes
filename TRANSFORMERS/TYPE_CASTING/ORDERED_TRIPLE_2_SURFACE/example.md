In this example we started with `PLOTLY_DATASET` node to generate a DataFrame which we passed to a type casting node `DF_2_ORDEREDTRIPLE` to convert DataFrame into `OrderedTriple` type of `DataContainer` class. 

Then we used `OrderedTriple_2_SURFACE` node to cast `OrderedTriple` to `surface` `DataContainer` type. Finally we vizualized output with Plotly visualizer node `SURFACE3D`.