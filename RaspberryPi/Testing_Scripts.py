### Testing Scripts File ###
# Contains functions for testing and validation

# Import Python libraries
from pathlib import Path
from PIL import Image

# Import custom libraries
from Flag import FLAG

# Find compression codecs discovered in Compressed images folder
def GetCompCodecs(flags: FLAG):
    codecs = [] # Initialize array
    files = sorted([str(x) for x in flags.c.iterdir()]) # Create sorted list of files in compressed folder
    for file in files:
        codec = Image.open(file).format
        if codec not in codecs:
            codecs.append(codec)
    return codecs

# Debugging section
if __name__ == "__main__":
    flags = FLAG()
    codecs = GetCompCodecs(flags)
    print(codecs)