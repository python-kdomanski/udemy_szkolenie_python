import os

files_to_process = [
    r"d:\Projekty\PyCharm\pythonCourse\skrypt1.py",
    r"d:\Projekty\PyCharm\pythonCourse\skrypt2.py"
]

for file_path in files_to_process:
    with open(file_path, 'r') as f:
        print("File {} ...".format(os.path.basename(file_path)))
        source = f.read()
        exec(source)