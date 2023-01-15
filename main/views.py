from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
	tasks = Task.objects.order_by('-id')
	return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
	return render(request, 'main/about.html')


def demand(request):
	return render(request, 'main/demand.html')


def geography(request):
	return render(request, 'main/geography.html')


def skills(request):
	return render(request, 'main/skills.html')


def vacancies(request):
	error = ''
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			error = 'Форма была неверной'

	form = TaskForm()
	context = {
		'form': form,
		'error': error
	}
	return render(request, 'main/vacancies.html', context)
