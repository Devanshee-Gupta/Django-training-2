from django.urls import path

from home import views

urlpatterns = [
    path("", views.getAllRecords, name="getAllRecords"),
    path("addNewQuestion", views.addNewQuestion, name="addNewQuestion"),
    path("vote/<int:questionId>/<int:choiceId>",views.vote, name="vote")
]