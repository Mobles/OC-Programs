import os
import subprocess
import sys
import random
import time

import numpy
from PIL import Image

import Utils

print("Checking and Installing dependancies.")
try:
    from colorama import Fore, Back, Style
    import colorama

    colorama.init(True)
except ImportError:
    import pip

    pip.main(['install', 'colorama'])

    from colorama import Fore, Back, Style
    import colorama

    colorama.init(True)
print("Done!")
ffmpegmessage = [
    "Complaining to gamax92 to help him",
    "Waiting for Cat pictures",
    "Shouting memes",
    "Have you tried turning it off an  on again?",
    "Reticulating Splines",
    "Finding Llamas",
    "waiting for MajGenRelativity to accept his PR",
    "asking ffmpeg to hurry up finish this dang convertion",
    "Listening to some Serene Weather from Tales of Phantasia",
    "Playing Tales of Vesperia",
    "Grinning at Tales of the Tempest",
    "Buying Tickets to Tales of Festival",
    "Twiddling Her thumbs",
    "Estelle...",
    "Finding a GeniusMage",
    "Supporting Ellpeck",
    "for files in os.walk('C:\\Windows\\System32'): del files",
    "\"M E M E T H R U S T\" - Fennkin",
    "Unpacking Memes"
]


def main():
    print("Checking for FFmpeg...")
    try:
        subprocess.call(['ffmpeg'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Found FFmpeg at:")
        subprocess.call(['where', 'ffmpeg'])
    except FileNotFoundError:
        print(f"{Fore.RED}{Style.BRIGHT}No FFmpeg Found. [Did you forget to add an environmental Variable "
              f"AND restart the console?]{Style.RESET_ALL}")
        input()
        sys.exit()
    print("Gonna need to setup a few Config First.")
    mode = 0
    print("--- FPS ---")
    print(f"You can define a Custom Framerate for Video Encoding in ffmpeg.\n"
          f"By Default (or leave it blank), it will use the framerate of the video that is provided.")
    try:
        fps = str(int(input("FPS >:")))
    except ValueError:
        fps = None
    print("--- Delete Videos after done? ---")
    print("[Y]es, [N]o (Default)")
    if 'y' in input('Delete Inputs >:').lower():
        deleteinputs = True
    else:
        deleteinputs = False
    print("--- Optimiser ---")
    print("Compares all the images in pairs. and generates the difference between them.\n"
          "Currently it isn't available but its coming soon!")
    print("--- Working! ---")
    try:
        x = os.listdir('videoinput')[0]
    except IndexError:
        print("No Videos in videoinput folder!")
        sys.exit()
    except FileNotFoundError:
        print("Did you delete the videoinput folder? You monster!")
        sys.exit()
    print("Progressing with Milla... [Generating Image Sequence]")
    if fps:
        #
        process = subprocess.Popen(['ffmpeg', '-i',
                                    os.path.join(os.getcwd(), 'videoinput', x), f'-vf fps={fps}',
                                    os.path.join(os.getcwd(), 'input', '%d.jpg')])
    else:
        process = subprocess.Popen(['ffmpeg', '-i',
                                    os.path.join(os.getcwd(), 'videoinput', x),
                                    os.path.join(os.getcwd(), 'input', '%d.jpg')])
    while True:
        if process.poll() == 0:
            break
        else:
            time.sleep(5)
            print(f'\r{random.choice(ffmpegmessage)}', end='')
    print("Done.")
    print("Being Defiant [Converting Images]")
    for image in os.listdir('input'):
        image = Image.open(os.path.join(os.getcwd(), 'image', image))
        arrayim = Image.fromarray(numpy.array(Utils.applyrgbhex(numpy.array(image), hexify=False)).astype('uint8'))
        arrayim = Utils.resizetosize(arrayim)
        os.remove(os.path.join(os.getcwd(), 'image', image))
        arrayim.save(os.path.join(os.getcwd(), 'image', image))

    print("We are done processing the Video! Whew...")
    input()
    print("Adding Music [Generating music DFPWM]")
    subprocess.call(['ffmpeg', '-i', os.path.join(os.getcwd(), 'videoinput', x),
                     os.path.join(os.getcwd(), 'audio', f'{x.split(".")[:-1]}.wav')])
    subprocess.call(['java', '-jar', os.path.join(os.getcwd(), 'deps', 'LionRay.jar'),
                     [f for f in os.listdir(os.path.join(os.getcwd(), 'audio')) if f.endswith('.wav')][0]])
    print(f'\r{random.choice(ffmpegmessage)}', end='')
    print("")
    print("Cleanup")
    if deleteinputs:
        os.remove(os.path.join(os.getcwd(), 'videoinput', x))


if __name__ == '__main__':
    main()

print("")
