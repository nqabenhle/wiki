from django.shortcuts import render
from markdown2 import Markdown
from django import forms
from django.http import HttpResponseRedirect
from random import choice

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

def search(request):
    
    form = request.GET["q"]

    return display_entry(request, entry=form)

class NewEntryForm(forms.Form):
    title = forms.CharField()
    markdown_content = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Write your article here. Use markdown language', 'rows':'3', 'cols':'5'}))

def new_entry(request):

    if request.method == "POST":
        
        form = NewEntryForm(request.POST)

        if form.is_valid():

            title = form.cleaned_data["title"]
            markdown_content = form.cleaned_data["markdown_content"]

            if util.get_entry(title.capitalize()) is None and util.get_entry(title.upper()) is None:
                util.save_entry(title.capitalize(), markdown_content)
                return HttpResponseRedirect("/wiki")

            else:
                return render(request, "encyclopedia/new_entry.html", {
                "form": NewEntryForm(),
                "already_exists": True
            })

        else:
            return render(request, "encyclopedia/new_entry.html", {
            "form": form
        })

    else:

        return render(request, "encyclopedia/new_entry.html", {
            "form": NewEntryForm()
        })

def random_entry(request):

    return HttpResponseRedirect(f"/wiki/{choice(util.list_entries())}")