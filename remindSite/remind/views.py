from datetime import timezone, datetime
from django.shortcuts import redirect
from django.views.generic.list import ListView
from remind.models import Reminder, Location
from remind.services import locationService


class ReminderListView(ListView):
    model = Reminder

#add_reminder adds a reminder instance and saves the reminder with its date.
def add_reminder(request):
  if request.GET.get('addReminder'):
    new_reminder_text = str(request.GET.get('reminderDescription'))
    today_date = datetime.today().strftime('%Y-%m-%d')
    remind = Reminder(reminder_text= new_reminder_text,reminder_date =today_date)
    remind.save()
    return redirect('reminder_list')


#check_reminder associates each reminder with a location and save the instance.
def check_reminder(request):
    current_location=locationService.locate()
    location = Location(street=current_location[0], lat=current_location[1], lng=current_location[2])
    location.save()

    current_reminder_id=int(request.GET.get('reminderId'))
    current_reminder=Reminder.objects.get(id=current_reminder_id)
    current_reminder.reminder_location_id=location.id
    current_reminder.save()
    print("reminder checked")
    return redirect('reminder_list')
