from django.shortcuts import render
from markdown2 import Markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def display_entry(request, entry):

    if (util.get_entry(entry.capitalize()) != None or util.get_entry(entry.upper()) != None):

        markdowner = Markdown()

        try:
            data = markdowner.convert(util.get_entry(entry.capitalize()))

        except TypeError:
            data = markdowner.convert(util.get_entry(entry.upper()))

        return render(request, "encyclopedia/display.html", {
            "title": entry,
            "body": data
        })

    else:

       return render(request, "encyclopedia/error.html", {
            "entry": entry.upper()
       }) 