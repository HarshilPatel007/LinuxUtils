
# All file(s) Operation(s) using python.
# link: https://realpython.com/working-with-files-in-python/


import os
basepath = os.path.dirname(os.path.realpath('__file__'))

# list all the things(folders and files) of a current directory
# for files in os.listdir(basepath):
#     print(files)


# list all files of a directory
# with os.scandir(basepath) as entries:
#     for entry in entries:
#         if entry.is_file():
#             print(entry.name)


# list all the specific files of a current directory
# for files in os.listdir(basepath):
#     if files.endswith('.py'):
#         print(files)

# list all subdirectory
# for entry in os.listdir(basepath):
#     if os.path.isdir(os.path.join(basepath, entry)):
#         print(entry)


# list all files of a subdirectory
# for entry in os.listdir(basepath):
#     if os.path.isdir(os.path.join(basepath, entry)):
#         # print(entry)
#         for files in os.listdir(entry):
#             # print(files)
#             path = os.path.join(entry, files)
#             print(path)
#             # os.startfile(path)
