from rest_framework.response import Response
from django.shortcuts import render
from home.serializers import ChoiceSerializer, QuestionSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from home.models import Choice, Question

# Create your views here.
@csrf_exempt
@api_view(['GET'])
def getAllRecords(request):
    list_of_questions=[]
    questionSerializer = QuestionSerializer(Question.objects.all(),many=True)

    for i in questionSerializer.data:
            choices = Choice.objects.filter(question__question_id=i['question_id'])
            choicesSerializer=ChoiceSerializer(choices,many=True)
            i['choices']=choicesSerializer.data
            list_of_questions.append(i)
    return render(request,"home.html",{'list_of_questions':list_of_questions,'votes':29})


@csrf_exempt
@api_view(['POST'])
def vote(request,questionId,choiceId):

    question = Question.objects.filter(question_id=questionId)
    if(question):
        choice = Choice.objects.filter(choice_id=choiceId)
        if(choice):
            choice[0].votes+=1
            question[0].total_votes+=1
            question[0].save()
            choice[0].save()
            return Response("Voted",status=201)
        else:
            return Response("Not Valid Choice",status=400)   
    else:  
        return Response("Not Valid Question Id",status=400)

