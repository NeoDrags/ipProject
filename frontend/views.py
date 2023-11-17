from django.shortcuts import render
from .models import Question

def page_view(request):
    current_value = request.session.get('counter', 0)
    current_value += 1
    request.session['counter'] = current_value
    if current_value >= 5:
        request.session['counter'] = 0
    [QNo, Qs, A1, A2, A3] = Question.cardValues()
    context = {
        "Qno": QNo[current_value - 1],
        "Qs": Qs[current_value - 1],
        "A1": A1[current_value - 1],
        "A2": A2[current_value - 1],
        "A3": A3[current_value - 1],
        'counter': current_value
    }
    return render(request, 'frontend/page.html', context)