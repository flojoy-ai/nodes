This example shows the function of the `PEAK_DETECTION` node. This node detects peaks in signals and returns the peak heights and widths.

First the need nodes were added: 1 `BASIC_OSCILLATOR`, 1 `LINE`, 1 `PEAK_DETECTION`, and 2 `SCATTER` nodes.

The `phase` parameter of the `BASIC_OSCILLATOR` node was changed to -1.48.

The app was run showing the results in the example. Note that although the height and width scatter plots seem to change, they range from 0.998-1.00 and 0.4984-0.499 respecitvely.

The results show 10 peaks with heights of ~1 and widths of ~0.5.
