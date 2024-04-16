
from urllib import request
from django.contrib import messages
from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import redirect, render
from home.serializers import ChoiceSerializer, QuestionSerializer
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view
from home.models import Choice, Question

# Create your views here.

def getAllRecords(request):
    list_of_questions=[]
    questionSerializer = QuestionSerializer(Question.objects.all(),many=True)

    for i in questionSerializer.data:
            choices = Choice.objects.filter(question__id=i['id'])
            choicesSerializer=ChoiceSerializer(choices,many=True)
            i['choices']=choicesSerializer.data
            list_of_questions.append(i)
    print(list_of_questions)
    return render(request,"home.html",{'list_of_questions':list_of_questions,'votes':29})

def vote(request,questionId,choiceId):
        
    question = Question.objects.filter(id=questionId)
    if(question):
            choice = Choice.objects.filter(id=choiceId)

            if(choice):
                if(question[0].id != choice[0].question.id):
                    return redirect("/")  
                
                else:    
                    choice[0].votes+=1
                    question[0].total_votes+=1
                    question[0].save()
                    choice[0].save()
                    messages.success(request,"Voted Successfully");
                    return redirect("/")  
            else:
                return redirect("/")  
    else:  
        return redirect("/")  

@csrf_exempt
def addNewQuestion(request):
    
    data = request.POST
    question_text = data['question_text']
    choice_text_1 = data['choice_text_1']
    choice_text_2 = data['choice_text_2']
    choice_text_3 = data['choice_text_3']
    correct_ans = data['correct_ans']

    if(correct_ans>'3' or correct_ans<'0'):
        messages.error(request,"enter valid correct answer")
        return redirect("/")

    q = Question.objects.create(question_text=question_text)
    if(choice_text_1):
        if(correct_ans=='1'):
            ch1 = Choice.objects.create(choice_text=choice_text_1,question=q,is_correct=True)
        else: 
            ch1 = Choice.objects.create(choice_text=choice_text_1,question=q,is_correct=False)

    if(choice_text_2):
        if(correct_ans=='2'):
            ch2 = Choice.objects.create(choice_text=choice_text_2,question=q,is_correct=True)
        else: 
            ch2 = Choice.objects.create(choice_text=choice_text_2,question=q,is_correct=False)

    if(choice_text_3):
        if(correct_ans=='3'):
            ch3 = Choice.objects.create(choice_text=choice_text_3,question=q,is_correct=True)
        else: 
            ch3 = Choice.objects.create(choice_text=choice_text_3,question=q,is_correct=False)

    return redirect("/")


    
