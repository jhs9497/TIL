from django.shortcuts import render

# Create your views here.
def index(request):
    import random
    numbers = random.sample(range(1, 46), 6)
    context = {
        'numbers' = numbers,
    }
    return render(request, 'index.html', context)