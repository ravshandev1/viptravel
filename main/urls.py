from django.urls import path
from .views import AboutList, AdvantageList, AwardList, ContactList, TourList, LeadCreate

urlpatterns = [
    path('about/', AboutList.as_view()),
    path('advantages/', AdvantageList.as_view()),
    path('contact/', ContactList.as_view()),
    path('tours/', TourList.as_view()),
    path('lead/', LeadCreate.as_view()),
    path('awards/', AwardList.as_view())
]
