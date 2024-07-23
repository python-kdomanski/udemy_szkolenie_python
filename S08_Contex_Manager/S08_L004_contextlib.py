class Door:
    def __init__(self, where):
        self.where = where

    def open(self):
        print("Opening door to the {}".format(self.where))

    def close(self):
        print("Closing door to the {}".format(self.where))

# door1 = Door('hell')
# door2 = Door("future")
# door1.open()
# door1.close()

from contextlib import contextmanager
# @contextmanager
# def OpenAndClose(obj):
#     obj.open()
#     yield obj #tu się funkcja zamrociła i czeka na __exit__
#     obj.close()
#
# with OpenAndClose(Door("next room")) as door:
#     print("the dore is to the {}".format(door.where))

@contextmanager
def OnlyClose(obj):
    yield obj #tu się funkcja zamrociła i czeka na __exit__
    obj.close()


with OnlyClose(Door("next room")) as door:
    door.open()
    print("the dore is to the {}".format(door.where))

from urllib.request import urlopen
from contextlib import closing

with closing(urlopen('http://www.kursyonline24.eu')) as page:
    for line in page:
        print(line)

import os
from contextlib import suppress
with suppress(FileNotFoundError):
    os.remove(r'c:\temp\not_used_file.txt')

from contextlib import redirect_stdout
f = open(r'D:\Projekty\PyCharm\pythonCourse\S08_Contex_Manager\log.txt', 'w')
with redirect_stdout(f): #zapisywanie wyniku na dysk (do otwartego pliku do zapisu) wyświetlane na standardowym wyjściu
    print('Hello')
    d = Door('EXIT')
    d.open()
    d.close()
