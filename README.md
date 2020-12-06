# Real-Time-Pitch-Shifter

Requirement:
Install SoX on your system.
https://pypi.org/project/sox/

Suggestion:
Recoder GUI: https://github.com/hannankhan888/AudioRecorder
To be done: Adding indicators to show which key was pressed.

Key idea:
1. Use a band-pass filter to change the central frequency of input audio signal to 261.625Hz(Middle C). 
(My solution is using the bandpass() method inside a SoX transformer. Result is not ideal!)
2. Change the pitch based on the key pressed.

A440 Rule and chromatic scale:  
https://en.wikipedia.org/wiki/Chromatic_scale

Pianoputer
http://zulko.github.io/blog/2014/03/29/soundstretching-and-pitch-shifting-in-python/

https://www.johndcook.com/blog/2016/02/10/musical-pitch-notation/

https://stackoverflow.com/questions/43963982/python-change-pitch-of-wav-file
