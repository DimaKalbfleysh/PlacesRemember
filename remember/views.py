from django.shortcuts import render

# Create your views here.
def remember_list(request):
	return render(request, 'remember/remember_list.html')