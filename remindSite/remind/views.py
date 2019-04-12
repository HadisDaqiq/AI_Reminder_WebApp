from datetime import timezone, datetime
from django.shortcuts import redirect

from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView
from remind.models import Reminder, Location
from django.http import HttpResponse
#import remindService
from remind.services import locationService


class ReminderListView(ListView):
    model = Reminder

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     #context['now'] = timezone.now()
    #     return context

def index(request):
    #remindService.location()
    # my_reminder = remindSite.remind.services.remindService
    return HttpResponse("Hello, world. You're at the remind index.")

def add_reminder(request):
  if request.GET.get('addReminder'):
    #mypythoncode.mypythonfunction( int(request.GET.get('mytextbox')) )
    new_reminder_text = str(request.GET.get('reminderDescription'))
    today_date = datetime.today().strftime('%Y-%m-%d')
    remind = Reminder(reminder_text= new_reminder_text,reminder_date =today_date)
    remind.save()
    #return render(request,'remind/reminder_list.html')
    return redirect('reminder_list')

def check_reminder(request):
    # return redirect()
    current_location=locationService.locate()
    location = Location(street=current_location[0], lat=current_location[1], lng=current_location[2])
    location.save()

    current_reminder_id=int(request.GET.get('reminderId'))
    current_reminder=Reminder.objects.get(id=current_reminder_id)
    current_reminder.reminder_location_id=location.id
    #remind = Reminder(reminder_id=current_reminder_id, reminder_location="Test Location")
    current_reminder.save()
    print("reminder checked")
    return redirect('reminder_list')
