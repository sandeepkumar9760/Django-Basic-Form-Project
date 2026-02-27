from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib import messages
from .models import Note
def lpu(req):
    note = Note.objects.all()
    return render(req, template_name="index.html",context={"notes":note})
def aboutlpu(req):
    return HttpResponse("Yes, its best.'")
# Create your views here.
def saveDataView(req):
    print(req.POST)
    title = req.POST.get("title","")
    description = req.POST.get("description", "")

    if not title or not description:
        messages.error(req,"Fill all details")
        return redirect("/")
    note = Note(title=title, description=description)
    note.save()
    messages.success(req, "Details saved")
    return redirect("/")

def edit_note(request, id):
    note = Note.objects.get(id=id)
    
    if request.method == "POST":
        note.title = request.POST.get("title")
        note.description = request.POST.get("description")
        note.save()
        return redirect("/")   # your home page

    return render(request, "edit-page.html", {"note": note})

def delete_note(req,id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect("/")



