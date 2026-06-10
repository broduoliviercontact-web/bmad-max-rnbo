---
title: "Frequency Domain"
source: https://docs.cycling74.com/userguide/frequency_domain/
source_path: /userguide/frequency_domain/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Frequency Domain

Source: https://docs.cycling74.com/userguide/frequency_domain/

## Extracted Text

# Frequency Domain Processing
Max provides several objects for working in the Frequency Domain , including an object for performing a Fourier Transform fft~ , as well as an object that can perform an Inverse Fourier Transform ifft~ . Most of the time, it's easier to work with the convienience object pfft~ , which abstracts over some of the technical details of working with the Fourier transform, including windowing and overlap-add. Very often, you'll see Fourier transform abbreviated to FFT, or Fast Fourier Transform .
## What is Frequency Domain Signal Processing?
Fourier analysis transforms a signal from a time domain representation to one in the frequency domain. Instead of specifying the value of a discete signal (for example sound) at a specific point in time, a frequency domain representation gives the amplitude and phase of each of several sinusoidal functions that, when summed together, would reproduce the original function.
## The fft~ and ifft~ Objects
The fft~ object takes a signal as input and outputs the real and imaginary components. The arguments to the fft~ object let you specify the size of the analysis window, as well as the spacing between analysis frames. You can also specify a global offset in frames, which will offset the Fourier analysis of this particular fft~ object against other fft~ objects. This is useful for performing overlap-add. The cartopol~ object converts between cartesian and polar coordinates, and will transform real-imaginary pairs to amplitude-phase pairs. The last outlet of fft~ and ifft~ is the current analysis bin, which is useful for synchronizing the Fourier transform with other processes.
Fourier analysis of a sawtooth signal at 220 Hertz, using an fft~ object. The cartopol~ object converts to the more intuitive amplitude and phase.
You can perform the inverse of a Fourier transform with the ifft~ object. The arguments to an ifft~ object are the same as to fft~ , and passing a signal first through fft~ and then ifft~ should recover the original signal exactly.
## The pfft~ Object
Most of the time, we want to do something with the signal after taking the Fourier transform. Techniques like phase vocoding, comvolution, and spectral delay all work by taking an input signal, transforming that signal to a frequency domain representation, doing some operation, and then transforming the signal back. However, since we're working with successive frames of Fourier analysis, this can introduce discontinuities, which will become very audible distortions to the final signal.
Commonly, we combine a windowing technique with an overlap-add technique to smooth out the audio signal. Essentially, we analyze the same input signal multiple times with a sliding window, and add the output together after transforming back from the frequency domain.
It's possible to use multiple fft~ and ifft~ objects to do this, but it's usually much easier to use pfft~ . The pfft~ object loads a patch as an abstraction , and then takes care of all of the windowing and overlap-add behind the scenes. The abstraction loaded by pfft~ is free to work entirely in the frequency domain, without worrying about the details of how the Fourier analysis is taking place.
A classic vocoder effect, using pfft~. The pfft~ object takes care of windowing and overlap-add, without the user needed to think about these details.
The argument to a pfft~ object is simply the name of the patcher to load as an abstraction. Similar to fft~ , it's also possible to specify the size of the FFT analysis frame, which must be a power of two. Because pfft~ is also performing overlap-add, it's also possible to set the overlap factor as an argument. Changing the analysis frame size and the overlap factor will affect the quality of the FFT output.
### Inlets and outlets
Similar to polyphonic patches loaded with poly~ , the pfft~ object uses special inlet and outlet objects. For regular Max messages, use the in and out objects. For signal, pfft~ , uses the fftin~ and fftout~ objects.
As is the case with poly~ , if a signal inlet created with fftin~ shares an index with an in object, the parent pfft~ object will create in inlet that can accept messages or signals.
The in object has an index 1, and fftin~ has the same index. The parent inlet can accept a message 'hello' or a signal.
Unlike regular inlet and outlet objects, the fftin~ and fftout~ objects take an argument to specify their index. This means that multiple fftin~ objects can refer to the same inlet, and multiple fftout~ objects can refer to the same outlet. If a signal goes to two different fftout~ objects that refer to the same outlet, those signals will be summed.
The fftin~ and fftout~ objects also let you specify a window function to use on the incoming signal. The special window name`nofft`disables the Fourier transform entirely, which lets you send audio signals into the subpatcher without transforming them.
A simplistic noise gate effect implemented in pfft~. The second inlet uses the 'nofft' window, which disables the FFT operation on the second inlet. This lets the user set the threshold for the gate using a signal.
### Bin index
The last outlet of the fftin~ object specifies the bin index , a continuous ramp from 0 0 0 to F r / 2 − 1 Fr/2 - 1 F r /2 − 1 , where F r Fr F r is the frame size. This is very useful for synchronizing the the FFT itself with other processes. For example, it's common to use the bin index in conjunction with poke~ and index~ , to record and play back an FFT.
Using poke~ and index~ in conjunction with the bin index output of fftin~. This patcher wouldn't really do anything, since the amplitude and phase signals are being read back from the buffer as soon as they're written. However, this illustrates the principle.
### fftinfo
In the context of a pfft~ subpatcher, use the fftinfo~ object to report information about the pfft~ parent patcher. This can be very useful if your pfft~ patcher needs to work differently depending on the way in which the FFT is being computed. For example, you might resize a buffer to hold a single frame of FFT analysis data.
### Window function
Specify a window function as an argument to fftin~ or fftout~ . Supported window functions are`square`(no window),`triangle`,`hanning`(the default),`hamming`, and`blackman`. The special window name`nofft`disables the Fourier transform entirely, which lets you send audio signals into the subpatcher without transforming them.
### Full spectrum
The second argument to pfft~ lets you specify the size of the analysis frame for the Fourier transform. For a given FFT frame size N N N , this will generate N N N complex pairs. This means that the larger the analysis frame size, the greater the frequency resolution if the FFT (although because the frame is larger, this reduces the temporal resolution). However, the full FFT is actually symmetric, so even though an FFT frame size N N N will yield N N N complex pairs, the result has only really resolved the input into N / 2 N/2 N /2 unique frequencies. Normally, pfft~ abstracts over this, and simply leaves out the symmetric, complex pairs. However, you can use the`fullspectrum`argument to ask for the complete FFT analysis. This is an argument to pfft~ , so all other arguments must be supplied as well.
A pfft~ object with the text 'pfft~ gate-subpatcher 512 4 0 1'. The arguments '512 4 0' specify the default values for the first three numeric arguments, but they must be supplied in order to specify a non-default value for the last argument, asking for a full spectrum analysis.
## Using gen~
When using gen~ inside of a pfft~ object, you can use the gen objects fftinfo , fftfullspect , ffthop , fftoffset , and fftsize to retrieve information about the FFT context in which gen~ is operating. You can also make use of the gen~ constants`FFTFULLSPECT`,`FFTHOP`,`FFTOFFSET`, and`FFTSIZE`.
