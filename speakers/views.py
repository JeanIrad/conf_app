from django.shortcuts import render
from django.http import HttpResponse
from django import forms
class NewSpeaker(forms.Form):
    name = forms.CharField(label='Name')

spks = [
    'speaker 1',
    'speaker 2',
    'speaker 3',
    'speaker 4',
]
# Create your views here.

def index(request):
    return render(request, 'home.html', {
        'speakers': spks
    })

def create(request):
    if request.method == "POST":
        speaker = NewSpeaker(request.POST)
        if speaker.is_valid():
            cleaned_speaker = speaker.cleaned_data()
            spks.append(cleaned_data)

    return render(request, 'create.html', {
        'name': NewSpeaker()
    })
def update(req):
    return render(req, 'update.html')

def delete(req):
    return render(req, 'delete.html')