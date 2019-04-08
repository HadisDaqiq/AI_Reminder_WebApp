import remindSite.remind.services.remindService

if __name__ == '__main__':
    my_reminder = remindSite.remind.services.remindService

    while True:
        action = input("[A]dd Reminder, [C]heck Reminder")

        if action == 'A':
           describ = input("description")
           my_reminder.createReminder(describ)

        if action == 'C':
            key = input("which reminder")
            my_reminder.check(key)

        print(my_reminder.uncheckedDic)#Remaining list.



