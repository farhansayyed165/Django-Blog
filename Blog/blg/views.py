from django.shortcuts import render, HttpResponse



# Create your views here.
def home(request):
    context = {'posts': 'Farhan'}
    # return HttpResponse('halo')
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse('Bhalo')