from turtle import title
from django.shortcuts import render

import markdown2

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def info_page(request):
    context = {"title" : title}
    return render(request, "encyclopedia/info_page.html", context)

def convert(request):
    return render(request, "entries/{title}.md",{
        "content": markdown2.markdown(util.get_entry(title)), "title": title
    })

