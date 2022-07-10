from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def display_entry(request, entry):

    if util.get_entry(entry.capitalize()) != None:

        # TODO
        return

    else:

       return render(request, "encyclopedia/error.html", {
            "entry": entry.capitalize()
       }) 