from django.urls import path

from . import views
from remind.views import ReminderListView

urlpatterns = [
    path('', views.index, name='index'),
    path('reminder_list', ReminderListView.as_view(), name='reminder_list'),
    path('add_reminder', views.add_reminder, name='add_reminder')

]