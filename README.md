# Real-Time-Pitch-Shifter

Requirement:
Install SoX on your system.
https://pypi.org/project/sox/

Suggestion:
Recoder GUI: https://github.com/hannankhan888/AudioRecorder
To be done: Adding indicators to show which key was pressed.

Key idea:
1. Use a band-pass filter to change the central frequency of input audio signal to 440Hz. 
(My solution is using the bandpass() method inside a SoX transformer. Result is not ideal!)
2. Change the pitch based on the key pressed.

A440 Rule and chromatic scale:  
https://en.wikipedia.org/wiki/Chromatic_scale
