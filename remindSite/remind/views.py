from datetime import timezone, datetime
from django.shortcuts import redirect

from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView
from remind.models import Reminder
from django.http import HttpResponse
#import remindService


class ReminderListView(ListView):
    model = Reminder
    paginate_by=20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context

def index(request):
    print('HELLOOOOO')
    #remindService.location()
    # my_reminder = remindSite.remind.services.remindService
    return HttpResponse("Hello, world. You're at the remind index.")

def add_reminder(request):
  if request.GET.get('addReminder'):
    #mypythoncode.mypythonfunction( int(request.GET.get('mytextbox')) )
    new_reminder_text = str(request.GET.get('reminderDescription'))
    print("Test beautiful GREAT ASOM hADIS")
    today_date = datetime.today().strftime('%Y-%m-%d')
    remind = Reminder(reminder_text= new_reminder_text,reminder_date =today_date)
    remind.save()
    #return render(request,'remind/reminder_list.html')
    return redirect('reminder_list')

def check_reminder(request):
  if request.GET.get('checkReminder'):
    #mypythoncode.mypythonfunction( int(request.GET.get('mytextbox')) )
   # reminder_checked = str(request.GET.get('reminderDescription'))#location
   # checked_remind = Reminder(,)
   # checked_remind.save()
    #return render(request,'remind/reminder_list.html')
   # return redirect()
   print("reminder checked")
