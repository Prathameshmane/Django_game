from django.shortcuts import render
from django.http import HttpResponse
import random


words = [
	"python",
	"java",
	"perl",
	"javascript",
	"html",
	"programming",
	"coding",
	"developer",
	"database",
	"function",
	"data",
	"integers",
	"string",
	"django",
	"node",
	"flask",
	"selenium",
	"swing",
	"applets",
	"android",
	"flutter",
	"react",
	"dart",
	"scripting",
	"linux",
]

def rword():
    global jword
    global word
    word = random.choice(words)
    jum = random.sample(word, len(word))
    jword = "".join(jum)


msg = ""
# Create your views here.
def homepage(request):
    rword()
    global jword, msg
    return render(request, 'index.html', {'jum_word': jword, 'msg': msg})

def checkans(request):
    global word, msg, jword
    user_answer = request.GET['answer']
    if user_answer == word:
        msg = "That was a correct one"
        homepage(request)
    else:
        msg = "You Should Try Again"
    return render(request, 'index.html',{'jum_word': jword, 'msg': msg})