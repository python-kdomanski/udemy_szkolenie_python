class BITException(Exception):
    def __init__(self, text, area):
        super().__init__(text)
        self.area = area

    def __str__(self):
        return "{}, area {}".format(super().__str__(), self.area)

class BITSecuriteException(BITException):
    pass

class BITDataFormatException(BITException):
    pass
try:
    # do something
    #1/0
    #raise BITException("file format is incorect", "Financial data")
    raise BITDataFormatException("file format is incorect", "Financial data")
except BITSecuriteException as e:
    print("Application security error: {}".format(e))
except BITDataFormatException as e:
    print("Application data malformed error: {}".format(e))
except BITException as e:
    #gdy nie zrobiliśmy __str__
    #print("Application error: {}, area {}".format(e, e.area))
    print("Application error: {}".format(e))
except Exception as e:
    print("General error: {}".format(e))

try:
    # do something
    raise BITException("file format is incorect", "Personal information")
except BITException as e:
    #print("Application error: {}, area {}".format(e, e.area))
    print("Application error: {}".format(e))