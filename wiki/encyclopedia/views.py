from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    }),

def css(request):
    return render(request, "css.html"),

def django(request):
    return render(request, "django.html"),

def git(request):
    return render(request, "git.html"),

def html(request):
    return render(request, "html.html"),

def python(request):
    return render(request, "python.html")