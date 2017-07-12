# Written by Zac Patel on 7/12/17
# encodes and decodes files

from pathlib import Path
import encoder import readFile

def encode(filename):
    filepath = Path(filename)

    # checking to see if the file we have been given is valid
    if not filepath.is_file():
        print("Error, cannot find file: " + filename)
        return

    # calling the parser to decode the file
    file_str, frequency = readFile(filename)

    
