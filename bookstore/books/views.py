from django.shortcuts import render, redirect
from .models import Book, Sold, Seller
from django.db.models import Q
from .forms import CreateForm, SignupForm, SigninForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse



# Create your views here.
def ListView(request):
    books = Book.objects.all()
    query = request.GET.get('q')
    if query:
        books = books.filter(
            Q(name__icontains=query)|
            Q(condition__icontains=query)|
            Q(author_name__icontains=query)
        ).distinct()

    context = {
        'books':books
    }

    return render(request, 'list.html', context)

def DetailView(request, book_id):
    books = Book.objects.get(id=book_id)

    context = {
        'book':books
    }

    return render(request, 'detail.html', context)

def CreateView(request):
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')

    context = {
        'form':form
    }

    return render(request, 'create.html', context)

def BuyView(request,book_id):
    books = Book.objects.get(id=book_id)

    seller, create = Seller.objects.get_or_create(salesman=books.owner)

    if create:
        x = Seller.objects.get(salesman=books.owner)
    else:
        x = seller

    buy = Sold.objects.create(buyer= request.user,book = books, seller=x)

    return HttpResponse(request)

def BuyListView(request):
    sbooks = Sold.objects.all()
    books = Book.objects.select_related(sbooks.book )

    context = {
        'books':books
    }

    return render(request, 'buylist.html', context)



def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("book-list")
    context = {
        "form":form,
    }
    return render(request, 'signup.html', context)

def signin(request):
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('book-list')
    context = {
        "form":form
    }
    return render(request, 'signin.html', context)

def signout(request):
    logout(request)
    return redirect("signin")

    