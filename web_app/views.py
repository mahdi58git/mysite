from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from web_app.forms import ContactForm
from django.contrib import messages


def home(request):
    return render(request,"index.html")
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.add_message(request,messages.SUCCESS,'Thank you for contacting us !!')
            form.save()
        else:
            messages.add_message(request, messages.ERROR, 'tiket didnt!!')
    else:
        pass
    form = ContactForm()
    return render(request,"contact.html",{"form":form})
def about(request):
    return render(request,"about.html")
