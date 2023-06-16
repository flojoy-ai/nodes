In this example, `LINSPACE` generates an array of 1000 samples.

The array is then passed down to a `SINE` node which generates a sawtooth wave of 20hz.

Finally, the signal is passed down to `FFT` which performs the fast fourier transform algorithm, 
transforming the input from the time domain into the frequency domain. Note that a `blackman` 
window is used here to reduce spectral leakage.

