# Execute all files in subdirectory of a root directory.
# Place script in root directory and run it.

import os
basepath = os.path.dirname(os.path.realpath('__file__'))


# list all files in subdirectory
for entry in os.listdir(basepath):
    if os.path.isdir(os.path.join(basepath, entry)):
        # print(entry)
        for files in os.listdir(entry):
            # print(files)
            filepath = os.path.join(entry, files)
            # print(filepath)
            os.startfile(filepath)
