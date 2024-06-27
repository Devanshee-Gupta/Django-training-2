from email import message
from django.contrib import messages
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import redirect, render
from home.serializers import ChoiceSerializer, QuestionSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from home.models import Choice, Question

# Create your views here.

def getAllRecords(request):
    list_of_questions=[]
    questions = Question.objects.all().order_by('id')
    questionSerializer = QuestionSerializer(questions,many=True)

    for i in questionSerializer.data:
            choices = Choice.objects.filter(question__id=i['id'])
            choicesSerializer=ChoiceSerializer(choices,many=True)
            i['choices']=choicesSerializer.data
            list_of_questions.append(i)
    return render(request,"Home.html",{'list_of_questions':list_of_questions})

def vote(request,questionId,choiceId):
    showCorrect=""
    question = Question.objects.filter(id=questionId)
    if(question):
            choice = Choice.objects.filter(id=choiceId)

            if(choice):
                if(question[0].id != choice[0].question.id):
                    return redirect("/#H{}".format(questionId))  
                
                else:    
                    if(choice[0].is_correct):
                        showCorrect=True
                    else:
                        showCorrect=False

                    choice[0].votes+=1
                    question[0].total_votes+=1
                    question[0].save()
                    choice[0].save()
                    messages.success(request,"Voted Successfully");
                    return redirect("/#H{0}".format(questionId))  
            else:
                return redirect("/#H{}".format(questionId))  
    else:  
        return redirect("/#H{}".format(questionId))  

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


def delete(request,questionId):
    question = Question.objects.filter(id=questionId)
    if(question):
            messages.success(request,"Deleted Successfully !")
            Choice.objects.filter(question=question[0]).delete()
            question.delete()
            return redirect('/')
    else: 
        return redirect('/')


def getDataForEditQuestion(request, questionId):
    question = Question.objects.filter(id=questionId).first()
    choices = Choice.objects.filter(question=question)
    choiceSerializer = ChoiceSerializer(choices,many=True)
    questionSerializer = QuestionSerializer(question)

    return JsonResponse({
        "question": questionSerializer.data,
        "choices": choiceSerializer.data,
    }, status=200)

@csrf_exempt
def updateQuestion(request,questionId):
    
    if request.method=='POST':
        data = request.POST
        question_text = data['edit_question_text']
        choice_texts = [data.get(f'edit_choice_text_{i}') for i in range(1, 4)]
        correct_ans = data.get('edit_correct_ans')

        # Validate correct answer
        if correct_ans not in ['1', '2', '3']:
            messages.error(request, "Please select a valid correct answer.")
            return redirect("/")

        q = Question.objects.filter(id=questionId).first()

        # Update question text
        q.question_text = question_text
        q.save()
        print(type(q))
        choices = Choice.objects.filter(question=q)
        # Update choices
        
        for i, choice_text in enumerate(choice_texts):
            choice = choices[i]
            choice.choice_text = choice_text
            choice.is_correct = (correct_ans == str(i + 1))
            choice.save()

        messages.success(request, "Question updated successfully.")
        return redirect("/")
    else:
        # If the request method is not POST, return a bad request response
        return HttpResponseBadRequest("Invalid request method")

@api_view(['GET']) 
def test(request):
    return Response({"status" : 200})