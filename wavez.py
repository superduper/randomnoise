import struct
import os
import wave
import base64

from rdoclient_py3 import RandomOrgClient

RANDOM_ORG_API_KEY = os.environ.get('RANDOM_ORG_API_KEY', 'fb6fed7d-4421-4039-91da-d64b8fcb5a46')

RECORD_LENGTH = 3  # duration, max 100
FRAME_RATE = 10000  # samples per second
SAMPLE_WIDTH = 1


random = RandomOrgClient(RANDOM_ORG_API_KEY)

def get_data(seconds):
    rows = random.generate_blobs(seconds, FRAME_RATE*SAMPLE_WIDTH*8)
    return b''.join(map(base64.b64decode,rows))



def write_sound(data):
    CHANNELS = 1
    SAMPLE_WIDTH = 1
    SAMPLE_LEN = FRAME_RATE * RECORD_LENGTH # seconds

    with wave.open('random.wav', 'w') as noise_output:
        noise_output.setparams((CHANNELS, SAMPLE_WIDTH, FRAME_RATE, 0, 'NONE', 'not compressed'))
        noise_output.writeframes(data)

if __name__ == "__main__":
    data = get_data(RECORD_LENGTH)
    write_sound(data)

