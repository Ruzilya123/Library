from django.shortcuts import render, redirect
from django import views
from . import models, forms


class Home(views.View):
    def get(self, request):
        category = forms.ChoiceCategory(request.GET)
        if category.is_valid():
            filter_category = category.cleaned_data['name']
            books = models.Book.objects.filter(category=filter_category)
        else:
            books = models.Book.objects.all()
        
        book_form = forms.BookForm

        return render(request, 'app/home.html', context={'books': books, 'category_form': category, 'book_form': book_form})

    def post(self, request):
        book_form = forms.BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
        return redirect('home')


class Book(views.View):
    def get(self, request, pk):
        book = models.Book.objects.get(pk=pk)
        book_form = forms.BookForm(instance=book)
        return render(request, 'app/edit.html', context={'form': book_form})
    
    def post(self, request, pk):
        book = models.Book.objects.get(pk=pk)
        book_form = forms.BookForm(request.POST, instance=book)
        book_form.save()
        return redirect('home')


def deleteBook(request, pk):
    book = models.Book.objects.get(pk=pk)
    book.delete()
    return redirect('home')


class OrderFromBook(views.View):
    def get(self, request, pk):
        model_book = models.Book.objects.get(pk=pk)
        model_order = models.OrderBook(book=model_book)
        form = forms.OrderForm(instance=model_order)
        return render(request, 'app/order.html', context={'form': form})


class Order(views.View):
    def get(self, request):
        form = forms.OrderForm()
        return render(request, 'app/order.html', context={'form': form})
    
    def post(self, request):
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/orders/')
        return redirect('')


def orders(request):
    orders = models.OrderBook.objects.all()
    return render(request, 'app/orders.html', context={'orders': orders})
