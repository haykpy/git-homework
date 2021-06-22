from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import NewTask
from .forms import TaskForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def home(request):
	task_list = NewTask.objects.filter(user_id=request.user.id)

	content = {"tasks": task_list}

	return render(request, 'to_do/home.html', content)

@login_required()
def create_task(request):
	form = TaskForm()
	if request.method == "POST":
		form = TaskForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect("home")

	context = {'task_form': form}
	return render(request, 'to_do/create.html', context)


def update_task(request, task_id):
	try:
		task = NewTask.objects.get(id=task_id)
	except:
		return HttpResponse('Object not found')

	form = TaskForm(instance=task)
	if request.method == "POST":
		form = TaskForm(instance=task, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			return HttpResponse('Error')
	return render(request, 'to_do/update.html', {'form': form})


def delete_task(request, task_id):
	try:
		task = NewTask.objects.get(id=task_id)
	except NewTask.DoesNotExist:
		return HttpResponse('Object not found')

	task.delete()
	return redirect('home')


def retrieve_task(request, task_id):
	try:
		task = NewTask.objects.get(id=task_id)
	except NewTask.DoesNotExist:
		return HttpResponse('Object not found')

	return render(request, 'to_do/retrieve.html', {'task': task})

