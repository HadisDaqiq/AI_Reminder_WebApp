from django.urls import path

from . import views
from remind.views import ReminderListView

from remind.models import Reminder


#This is a mapping between URL path expressions to Python functions (our views).
urlpatterns = [
    path('', views.index, name='index'),
    path('reminder_list', ReminderListView.as_view(model=Reminder), name='reminder_list'),
    path('add_reminder', views.add_reminder, name='add_reminder'),
    path('check_reminder', views.check_reminder, name='check_reminder')
]