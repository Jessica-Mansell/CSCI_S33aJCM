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

def convert(request):
    return render(request, "encyclopedia/info_page.html", {
        "content": markdown2.markdown(util.get_entry), "title": title
    })

def link_page(request):
    TITLE={"entries":title}
    return render(request, "encyclopedia/info_page.html", util.list_entries("entries"))


