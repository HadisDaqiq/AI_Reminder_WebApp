import random
import string

import remind.services.locationService

uncheckedDic = {}
checkedDic = {}
ide=""

def __init__(descrip =""):
    descrip = descrip
   #self.check = check



def createReminder(description="ss"):
    ide = generateId()
    #self.ide is referring to ide self.gener refers to its class.
    uncheckedDic[ide] = description
    #save data into database/tables.

    print("this is a saved")

def generateId(size=6, chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars) for _ in range(size))

def location():
    uncheckedDic
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
        checkedDic["address"] = remind.services.locationService.locate()
        print(checkedDic)
        print("checked list^")
        #print(self.uncheckedDic)
    else:
        print("reminder isn't present")


