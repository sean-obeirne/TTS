import os
import sys

test_sample = sys.argv[1]


with open('voices', 'r') as voices_file:
    for line in voices_file.readlines():
        os.system(f"edge-playback --text \"{test_sample}\" --voice {line.strip()}")
        if input("Continue? [Y/n] ") == "n":
            break

