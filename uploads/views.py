from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import DocumentForm, UserRegisterForm
from .models import Document
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'uploads/home.html')


@login_required
def upload_document(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.uploader = request.user
            document.save()
            print("Form is valid, redirecting...")
            return redirect('document_list')
        else:
            print("Form is not valid", form.errors)
    else:
        form = DocumentForm()
    return render(request, 'uploads/upload.html', {"form": form})


def document_list(request):
    documents = Document.objects.all()
    return render(request, 'uploads/document_list.html', {"documents": documents})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'uploads/register.html', {'form': form})
