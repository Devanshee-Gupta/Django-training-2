
from django.shortcuts import render
from home.serializers import ChoiceSerializer, QuestionSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from home.models import Choice, Question

# Create your views here.
@csrf_exempt
@api_view(['GET'])
def index(request):
    list_of_questions=[]
    questionSerializer = QuestionSerializer(Question.objects.all(),many=True)

    for i in questionSerializer.data:
            choices = Choice.objects.filter(question__id=i['id'])
            choicesSerializer=ChoiceSerializer(choices,many=True)
            i['choices']=choicesSerializer.data
            list_of_questions.append(i)

    return render(request,"home.html",{'list_of_questions':list_of_questions})


