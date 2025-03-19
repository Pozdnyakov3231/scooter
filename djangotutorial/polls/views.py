from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Question, Choice, Scooter

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# View для отображения списка всех вопросов
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)


# View для отображения деталей конкретного вопроса
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})


# View для голосования за конкретный выбор
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Перенаправление обратно на страницу с ошибкой, если выбор не был сделан
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "Вы не сделали выбор.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # После успешного голосования перенаправляем на результат
        return redirect('results', question_id=question.id)


# View для отображения результатов голосования
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})


# View для управления самокатами
def scooters_management(request):
    all_scooters = Scooter.objects.all().order_by('model')
    context = {'all_scooters': all_scooters}
    return render(request, 'management.html', context)



def change_scooter_status(request, scooter_id):
    scooter = get_object_or_404(Scooter, pk=scooter_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in [status[0] for status in Scooter.STATUS_CHOICES]:
            scooter.status = new_status
            scooter.save()
            return redirect('scooters_management')
    context = {'scooter': scooter}
    return render(request, 'status_change_form.html', context)