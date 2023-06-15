# godot-stex-to-png

This script converts Godot stex files to standard png files. This is mainly used in combination with a tool that unpacks Godot .pck files 
like [godot-unpacker](https://github.com/tehskai/godot-unpacker).

# Requirements
Tested on Python 3 only

# Usage 
move the .stex file in the same directory as script and run:
```
python godot-stex-to-png.py input.stex
```

# More infomation
.stex files are simply .png files with an extra 32 bits of header data, as detailed here:

- [Godot Source Code where .stex files are read](https://github.com/godotengine/godot/blob/master/editor/import/resource_importer_image.cpp#L73)

- [Reddit post asking about .stex files](https://web.archive.org/web/20230615102220/https://old.reddit.com/r/godot/comments/n178h2/convert_stex_back_to_png/gwb9ui3/)

As such, this tool was created to further automate the process by just trimming said 32 bits of data from the .stex file using python

If you wish to run the script on all files in a folder, you could consider using [unix](https://askubuntu.com/questions/1037186/bash-script-to-run-python-script-for-all-images-in-all-subdirectories). 
