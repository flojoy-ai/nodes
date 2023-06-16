In this example, the `TIMESERIES` node generates random time series data 

<!-- '<table border="1" class="dataframe">  <thead>   <tr style="text-align: right;">     <th></th>     <th>Timestamp</th>     <th>Data</th>  </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>2023-01-01</td>      <td>-0.187903</td>    </tr>    <tr>      <th>1</th>      <td>2023-01-02</td>      <td>0.204290</td>    </tr>    <tr>      <th>2</th>      <td>2023-01-03</td>      <td>-0.659945</td>    </tr>  </tbody></table>' -->

This dataframe is then passed to the `PROPHET_PREDICT` node, with the default parameters
of `run_forecast=True` and `periods=365`. This node trains a `Prophet` model and runs a prediction
forecast over a 365 period. 

It returns a DataContainer with the following
* `type`: `dataframe`
* `m`: The forecasted dataframe
* `extra`: 
  * `run_forecast`: `True` (because that's what was passed in)
  * `prophet`: The trained `Prophet` model
  * `original`: The dataframe passed into the node

Finally, this is passed to 2 nodes, `PROPHET_PLOT` and `PROPHET_COMPONENTS`, wherein
the forecast and the trend components are plotted in Plotly. Because a forecast was already run,
the `PROPHET_PLOT` and `PROPHET_COMPONENTS` nodes know to use the already predicted dataframe.