# echo_via_circular_buffer.py
# Reads a specified wave file (mono) and plays it with an echo.
# This implementation uses a circular buffer.

import pyaudio
import wave
import struct

BLOCKLEN = 4096      # Number of frames per block
WIDTH = 2           # Number of bytes per signal value
CHANNELS = 1        # mono
RATE = 44100        # Frame rate (frames/second)


# Set parameters of delay system
b0 = 1.0            # direct-path gain
G = 0.8             # feed-forward gain
delay_sec = 0.07    # delay in seconds, 50 milliseconds   Try delay_sec = 0.02
N = int( RATE * delay_sec )   # delay in samples

print('The delay of %.3f seconds is %d samples.' %  (delay_sec, N))

# Buffer to store past signal values. Initialize to zero.
BUFFER_LEN = N              # length of buffer
buffer = BUFFER_LEN * [0]   # list of zeros

# Open an output audio stream
p = pyaudio.PyAudio()
stream = p.open(format      = pyaudio.paInt16,
                channels    = 1,
                rate        = RATE,
                input       = True,
                output      = True )


# Initialize buffer index (circular index)
k = 0

print('* Start')

while True:

    # input_bytes = stream.read(BLOCKLEN)       # BLOCKLEN = number of frames read
    input_bytes = stream.read(BLOCKLEN, exception_on_overflow = False)   # BLOCKLEN = number of frames read

    # Convert binary data to tuple of numbers
    x = struct.unpack('h' * BLOCKLEN, input_bytes)    # Compute output value

    y = BLOCKLEN * [0]   # list of zeros

    for i in range(BLOCKLEN):
        # y(n) = b0 x(n) + G x(n-N)
        y[i] = int(b0 * x[i] + G * buffer[k])

        # Update buffer
        buffer[k] = x[i]

        # Increment buffer index
        k = k + 1
        if k >= BUFFER_LEN:
            # The index has reached the end of the buffer. Circle the index back to the front.
            k = 0           

    # Clip and convert output value to binary data
    output_bytes = struct.pack('h' * BLOCKLEN, *y)

    # Write output value to audio stream
    stream.write(output_bytes)
    

print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()

