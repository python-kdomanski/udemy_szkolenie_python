import os

path = r'd:\Projekty\PyCharm\pythonCourse'
search_string = 'Ford'
file_extension = '.py'

for dir_name, subdirs, filenames in os.walk(path):
    #print(dir_name, subdirs, filenames)
    for filename in filenames:
        if filename.endswith(file_extension):
            try:
                fullFileName = os.path.join(dir_name, filename)
                for line in open(fullFileName):
                    if search_string in line:
                        print(filename)
            except Exception as e:
                pass

def generate_files(base_dir, file_extension):
    for dir_name, subdirs, filenames in os.walk(base_dir):
        for filename in filenames:
            if filename.endswith(file_extension):
                try:
                    fullFileName = os.path.join(dir_name, filename)
                    yield fullFileName
                except Exception as e:
                    pass
def grep_files(dearch_string, files):
    for file in files:
        with open(file) as text:
            try:
                if search_string in text.read():
                    yield file
            except Exception as e:
                pass

files_generator = generate_files(path, file_extension)

for file in grep_files(search_string, files_generator):
    print(file)