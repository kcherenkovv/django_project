from django.shortcuts import render
     
# Create your views here.
def index(request):
	return render(request, 'firstapp/index.html')

def about(request):
	return render(request, 'firstapp/about.html')
