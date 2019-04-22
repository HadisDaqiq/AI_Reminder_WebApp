import random
import string
from datetime import timezone

import locationService
from remind.models import Location

uncheckedDic = {}
checkedDic = {}
ide=""

def __init__(descrip =""):
    descrip = descrip

#createReminder creates reminder with description based on user's request.
def createReminder(description="ss"):
    ide = generateId()
    uncheckedDic[ide] = description

#generates random Id for testing reminders.
def generateId(size=6, chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars) for _ in range(size))

#location association for testing on console.
def location():
    uncheckedDic
    print("location associated")
    #if it becomes check return location is associated.
    if ide in uncheckedDic:
        print("location is saved")

def check(key):
    if key in uncheckedDic.keys():
        print("key is in the uncheckedDic")
        checkedDic[key] = uncheckedDic[key]
        del uncheckedDic[key] #delete the checked reminder from the unchecked Dic.

        #print(l.locate())  #location address
        checkedDic["address"] = locationService.locate()
        print(checkedDic)
        print("checked list^")
        #print(self.uncheckedDic)
    else:
        print("reminder isn't present")


