from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306211660',
        'name': 'Clarissa Indriana',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
