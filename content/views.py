from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as authlogin, logout as authlogout
from .models import Content, ContentDetail
from .forms import ContentForm, ContentDetailForm
from django.forms import modelformset_factory


def index(request):
    search_query = request.GET.get('search', '')
    if request.user.is_authenticated:
        if search_query:
            contents = Content.objects.filter(user=request.user, title__icontains=search_query)
        else:
            contents = Content.objects.filter(user=request.user)
    else:
        contents = Content.objects.none()  # Return an empty queryset if the user is not authenticated
    
    paginator = Paginator(contents, 5)  # Show 5 contents per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'index.html', {'contents': page_obj})

@login_required(login_url='login/')
def content_detail(request, pk):
    content = get_object_or_404(Content, pk=pk, user=request.user)
    return render(request, 'content_detail.html', {'content': content})


@login_required(login_url='login')
def content_create(request):
    ContentFormSet = modelformset_factory(ContentDetail, form=ContentDetailForm, extra=1, can_delete=True)
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        formset = ContentFormSet(request.POST, request.FILES, queryset=ContentDetail.objects.none())
        if form.is_valid() and formset.is_valid():
            content = form.save(commit=False)
            content.user = request.user
            content.save()
            for form in formset:
                content_detail = form.save(commit=False)
                content_detail.content = content
                content_detail.save()
            return redirect('index')
    else:
        form = ContentForm()
        formset = ContentFormSet(queryset=ContentDetail.objects.none())
    return render(request, 'content_form.html', {'form': form, 'formset': formset})

@login_required(login_url='login')
def content_update(request, pk):
    content = get_object_or_404(Content, pk=pk, user=request.user)
    ContentFormSet = modelformset_factory(ContentDetail, form=ContentDetailForm, extra=1, can_delete=True)
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES, instance=content)
        formset = ContentFormSet(request.POST, request.FILES, queryset=ContentDetail.objects.filter(content=content))
        if form.is_valid() and formset.is_valid():
            form.save()
            for form in formset:
                content_detail = form.save(commit=False)
                content_detail.content = content
                content_detail.save()
            return redirect('index')
    else:
        form = ContentForm(instance=content)
        formset = ContentFormSet(queryset=ContentDetail.objects.filter(content=content))
    return render(request, 'content_form.html', {'form': form, 'formset': formset})

@login_required(login_url='login')
def content_delete(request, pk):
    content = get_object_or_404(Content, pk=pk, user=request.user)
    content.delete()
    return redirect('index')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            authlogin(request, user)
            return redirect('index')
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            error_message = 'Passwords do not match.'
            return render(request, 'signup.html', {'error_message': error_message})
        
        if User.objects.filter(username=username).exists():
            error_message = 'Username already exists. Please choose a different one.'
            return render(request, 'signup.html', {'error_message': error_message})
        
        user = User.objects.create_user(username=username, password=password)
        return redirect('login')
    
    return render(request, 'signup.html')

def logout(request):
    authlogout(request)
    return redirect('login')

@login_required
def menu(request):
    return render(request, 'menu.html')
