from django.http import HttpResponse
from django.shortcuts import render
import string
def index(res):
    return render(res,"index.html")

def contact(res):
    return render(res, "contact.html")
    #return HttpResponse('''<html><a href="https://www.youtube.com">YOUTUBE</a></html>''')
def analyze(res):

    text = res.POST.get("text","default")

    if text =="default" or text=="":

        return HttpResponse('''<a href="/">Enter Some text</a>''')
    else:
        analyzedpunc= res.POST.get("analyzedpunc", "off")
        analyzednew = res.POST.get("analyzednew", "off")
        analyzedcap = res.POST.get("analyzedcap", "off")
        print(analyzednew,analyzedcap,analyzedpunc)
        which_effect="NORMAL TEXT"
        if analyzedpunc !="off":
            text = removepunc(text)
            which_effect = "ANALYZED TEXT"
        if  analyzedcap !="off":
            text = fullcap(text)
            which_effect = "ANALYZED TEXT"
        if analyzednew != "off":
            text = newline(text)
            which_effect = "ANALYZED TEXT"

        params={"WHAT":which_effect,"analyzed":text}
        return render(res,"analyzed.html",params)
    #else:
      #      return HttpResponse('''<a href="/">Please select some options.</a>''')

def removepunc(text):
    punct=list(string.punctuation)
    output=""
    for letter in text:
        if letter not in punct:
            output+=letter
    return output


def newline(text):
    output=""
    for char in text:
        if char!='\n' and char !="\r":
            output+=char
    return output

def fullcap(text):
    output=text.upper()
    return output
