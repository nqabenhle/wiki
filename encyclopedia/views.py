from django.shortcuts import render
from markdown2 import Markdown
from html.parser import HTMLParser

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

class HTMLFilter(HTMLParser):
    text = ""
    def handle_data(self, data):
        self.text += data       

def display_entry(request, entry):

    if util.get_entry(entry.capitalize()) != None:

        markdowner = Markdown()
        data = markdowner.convert(util.get_entry(entry.capitalize()))

        html = HTMLFilter()
        html.feed(data)
        
        body = html.text

        return render(request, "encyclopedia/display.html", {
            "title": entry,
            "body": body
        })

    else:

       return render(request, "encyclopedia/error.html", {
            "entry": entry.capitalize()
       }) 