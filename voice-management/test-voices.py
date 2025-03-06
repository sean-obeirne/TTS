import os
from time import sleep
import sys

def main():
    test_sample = sys.argv[1]
    auto = sys.argv[2] == "auto" if len(sys.argv) > 2 else False
    favored = []

    with open('voices', 'r') as voices_file:
        voices = voices_file.readlines()

    print("Voices")
    print("-------")
    for i, line in enumerate(voices):
        print(f"\t{line.strip()[6:]}")
        os.system(f"edge-playback --text \"{test_sample}\" --voice {line.strip()} > /dev/null 2>&1")
        if not auto:
            if input("Bookmark? [Y/n] ") != "n":
                favored.append(i)
        sleep(1)
    for i in range(len(favored)):
        print(favored[i])



if __name__ == "__main__":
    main()
