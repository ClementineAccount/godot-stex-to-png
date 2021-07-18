# godot-stex-to-png.py
# https://github.com/ClementineAccount/godot-stex-to-png

import sys
if len(sys.argv) > 1:
    filename = sys.argv[1]
    inputFile = open(filename, 'rb')
    outputFile = open(filename + '-output.png', 'wb')

    # 32 bits is based off the .stex header which are primmed for png
    inputFile.seek(32)

    while 1:
        #read by char
        char = inputFile.read(1)
        outputFile.write(char)
        
        if not char:
            break

    inputFile.close()
    outputFile.close()
else:
    print("Usage: python godot-stex-to-png.py input.stex")

