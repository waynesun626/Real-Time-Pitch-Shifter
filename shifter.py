import numpy as np
import sox
import pyaudio, struct, wave
import tkinter as Tk

# sample rate in Hz
RATE = 44100
RECORD_SECONDS = 5
BLOCKLEN=800

MAXVALUE = 2**15-1

k=0

# Number of blocks to run for
num_blocks = int(RATE / BLOCKLEN * RECORD_SECONDS)

p = pyaudio.PyAudio()
PA_FORMAT = pyaudio.paInt16
stream = p.open(
        format      = PA_FORMAT,
        channels    = 1,
        rate        = RATE,
        input       = True,
        output      = True,
        frames_per_buffer = 800)

CONTINUE = True
KEYPRESS = False

def my_function(event):
    global CONTINUE
    global KEYPRESS
    global k
    print('You pressed ' + event.char)
    if event.char == 'q':
      print('Good bye')
      CONTINUE = False
    if event .char=='a':
        k=0
    if event .char=='s':
        k=1
    if event .char=='d':
        k=2
    if event .char=='f':
        k=3
    if event .char=='g':
        k=4
    if event .char=='h':
        k=5
    if event .char=='j':
        k=6
    if event .char=='k':
        k=7
    if event .char=='l':
        k=8
    if event .char=='z':
        k=9
    if event .char=='x':
        k=10
    if event .char=='c':
        k=11
    if event .char=='v':
        k=12
    KEYPRESS = True

root = Tk.Tk()
root.bind("<Key>", my_function)


print('Press keys for sound.')
print('Press "q" to quit')

# Start loop
while CONTINUE:
    root.update()

    # Get frames from audio input stream
    # input_bytes = stream.read(BLOCKLEN)       # BLOCKLEN = number of frames read
    input_bytes = stream.read(BLOCKLEN, exception_on_overflow = False)   # BLOCKLEN = number of frames read

    # Convert binary data to tuple of numbers
    input_tuple = struct.unpack('h' * BLOCKLEN, input_bytes)

    data=np.array(input_tuple)

    scaled = np.frombuffer(input_bytes, np.int16)

    # create a transformer
    tfm = sox.Transformer()

    tfm.bandpass(261.625)

    # shift the pitch up by 1 semitones
    tfm.pitch(k)

    y_out=4*tfm.build_array(input_array=scaled, sample_rate_in=RATE)

    y = np.clip(y_out.astype(int), -MAXVALUE, MAXVALUE)     # Clipping

    output_bytes = struct.pack('h' * BLOCKLEN, *y)

    # Write binary data to audio output stream
    stream.write(output_bytes, BLOCKLEN)

print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()



