from django.shortcuts import render, redirect
from django.contrib import messages
from . import predictor
# Create your views here.
def diagnosis(request):
    if request.method == 'GET':
        return render(request, 'diagnosis.html')

    elif request.method == 'POST':
        symptoms = request.POST['symtoms']
        pred, summary = predictor.predict(symptoms)
        messages.info(request, pred)
        messages.info(request, summary)
        return redirect('diagnosis')
