In this example, `LINSPACE` generates an array from 0 to 99 (eg: [0, 1, 2… 99]). 

This array is then passed to both the `SINE` and `RAND` nodes, which compute `numpy.sine()` and `numpy.rand()` on each element of this array (respectively). 

Finally, these 2 arrays are added together element-wise - click the *Output* tab above to see the result. You guessed it - the output is a noisy sine wave.