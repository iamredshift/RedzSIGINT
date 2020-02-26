A head start when RE signal. Run in this order. 
CaptureSoI > ReviewSoIWithNoise > SimpleAMDemodulation > TwoStageDownsample

Many items in these will have to be changed for the signal you are looking at. 
This also is not a soup to nuts RE every signal out there, but a push in the right direction. 
The examples GRC above are targeted for AM signal. 
Lets say you need to look at a FM signal, you would change all the "complex to mag" to "quadrature demodulator", etc, etc. 


