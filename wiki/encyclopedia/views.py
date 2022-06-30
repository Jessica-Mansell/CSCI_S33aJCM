from turtle import title
from django.shortcuts import render
import markdown2

from markdown2 import Markdown

markdowner = Markdown()

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


