from django.shortcuts import redirect, render

from .models import Quiestion, Choice


# Create your views here.
def home(request):
    questions = Quiestion.objects.all()
    return render( 
        request, 
        'poll/home.html',
        {
            "questions": questions
         })

def vote(request, q_id):
    q= Quiestion.objects.get(pk=q_id)
    if request.method == "POST":
        try:
            choice_id = request.POST.get('choise')
            choice = q.choice_set.get(pk=choice_id)
            choice.votes += 1
            choice.save()
            return redirect('poll:result', q_id)
        except(KeyError, Choice.DoesNotExist):
            return render(request, 'poll/vote.html', {
                "question": q,
                "error_message": "Debes elegir algo! XD"
            })
    return render(
        request, 
        'poll/vote.html', 
        {
            "question": q
         })

def result(request, q_id):
    try:
        q = Quiestion.objects.get(pk=q_id)
    except Quiestion.DoesNotExist:
        return redirect('poll:home')
    return render(request, 'poll/result.html', {
        "question": q
    })