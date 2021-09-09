from django.contrib import messages
from django.shortcuts import redirect, render
import bcrypt
from .decorators import login_required
from .models import Authors, Books, Reviews, User


@login_required
def index(request):
    #    libros= Books.objects.all()[:5]
    reviews=Reviews.objects.all().order_by('-created_at')[:5]
    context = {
        'saludo': 'Hola',
        "reviews":reviews
    }
    return render(request, 'index.html', context)


@login_required
def revision(request):
    if request.method=='GET':
        authors = Authors.objects.all()
        context = {
            'authors': authors
        }
        return render(request, 'new_revision.html', context)
    if request.method=='POST':
        book_title=request.POST['book_title']
        #si viene algo en el new_author tomamos ese...si no usamos el author_id
        if request.POST['new_author'] !='':
            #creamos uno nuevo
            autor=Authors.objects.create(name=request.POST['new_author'] ) 
        else:
            autor=Authors.objects.get(id=request.POST['author_id'])
        # aca deberíamos revisar que no hayan dos libros con el mismo nombre.
        libro= Books.objects.create(title=book_title, author=autor)
        #crear la review
        texto=request.POST['comment']
        user=User.objects.get(id=request.session['user']['id'])
        Reviews.objects.create(text=texto, book=libro, user=user)
        messages.success(request, "Review creada exitosamente!")
        return redirect('/index')
