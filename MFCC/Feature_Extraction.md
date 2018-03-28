Mel Frequency Cepstral Coefficients
In sound processing, the mel-frequency cepstrum (MFC) is a representation of the short-term power spectrum of a sound, based on a linear cosine transform of a log power spectrum on a nonlinear mel scale of frequency.

Steps involved in computing MFCCs:
  1. The speech signal goes through a pre-emphasis filter to balance frequency spectrum.
  2. Then gets sliced into (overlapping) frames and a window function is applied to each frame.
  3. Afterwards, we do a Fourier transform on each frame and calculate the power spectrum; and subsequently compute the filter banks. 
  4. To obtain MFCCs, a Discrete Cosine Transform (DCT) is applied to the filter banks retaining a number of the resulting coefficients while the rest are discarded.
  5. The final step is mean normalization. The MFCCs are the amplitudes of the resulting spectrum.
  
  
