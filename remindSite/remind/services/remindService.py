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


def createReminder(description="ss"):
    ide = generateId()
   # side is referring to ide self.gener refers to its class.
    uncheckedDic[ide] = description
    #save data into database/tables.

def generateId(size=6, chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars) for _ in range(size))

def location():
    uncheckedDic
    # l=Location(street="test1", lat=33, lng=81)
    # l.save()

    print("location associated")
    #save the reminder in a list...
    #if it becomes check

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


