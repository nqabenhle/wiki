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
            entry = entry.capitalize()

        except TypeError:
            data = markdowner.convert(util.get_entry(entry.upper()))
            entry = entry.upper()

        return render(request, "encyclopedia/display.html", {
            "title": entry,
            "body": data
        })

    else:

<<<<<<< HEAD
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

def random_entry():

    return HttpResponseRedirect(f"/wiki/{choice(util.list_entries())}")

class EditEntryForm(forms.Form):
    def __init__(self, *args, **kwargs):
        try:
            self.title = kwargs.pop("title")
            self.content = kwargs.pop("content")
            super(EditEntryForm, self).__init__(*args, **kwargs)
            self.fields["Title"].widget = forms.TextInput(attrs={"value": self.title})
            self.fields["Content"].widget = forms.Textarea()
            self.fields["Content"].initial = self.content
        except KeyError:
            super(EditEntryForm, self).__init__(*args, **kwargs)
            self.fields["Title"].widget = forms.TextInput()
            self.fields["Content"].widget = forms.Textarea()

    Title = forms.CharField()
    Content = forms.CharField()

def edit_entry(request, title):

    if request.method == "POST":
        form = EditEntryForm(request.POST)

        if form.is_valid():

            title = form.cleaned_data["Title"]
            markdown_content = form.cleaned_data["Content"]
            util.save_entry(title, markdown_content)
            
            return HttpResponseRedirect(f"/wiki/{title}")

        else:
            return render(request, "encyclopedia/edit_entry.html", {
                "form": form,
                "title": title
            })

        
    else:

        markdown_content = util.get_entry(title)
        
        return render(request, "encyclopedia/edit_entry.html", {
            "form": EditEntryForm(title=title, content=markdown_content),
            "title": title
        })
=======
        entries = util.list_entries()
        similar_entries = []

        for i in range(len(entries)):
            if entry.lower() in entries[i].lower():
                similar_entries.append(entries[i])

        print(f"similar_entries: {similar_entries}")


        return render(request, "encyclopedia/error.html", {
                "entry": entry.upper(),
                "similar_entries": similar_entries
        }) 
>>>>>>> index
