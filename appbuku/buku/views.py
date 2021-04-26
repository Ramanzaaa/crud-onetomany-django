from django.shortcuts import render, redirect, get_object_or_404
from .models import Buku,Author
from .forms import BukuForm, AuthorForm
from django.http import HttpResponse

#Create your views here.
def index(request):
    shelf = Buku.objects.all()
    return render(request, 'buku/library.html', {'shelf': shelf})

def upload(request):
    upload = BukuForm()
    if request.method == 'POST':
        upload = BukuForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""Form salah, retry di sini <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'buku/upload_form.html', {'upload_form':upload})

def tambah_author(request):
    authorabc = AuthorForm()
    if request.method == 'POST':
        authorabc = AuthorForm(request.POST, request.FILES)
        if authorabc.is_valid():
            authorabc.save()
            return redirect('index')
        else:
            return HttpResponse("""Form salah, retry di sini <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'buku/author_form.html', {'author_form':authorabc})

def update_buku(request, buku_id):
    buku_id = int(buku_id)
    try:
        buku_sel = Buku.objects.get(id = buku_id)
    except Buku.DoesNotExist:
        return redirect('index')
    buku_form = BukuForm(request.POST or None, instance = buku_sel)
    if buku_form.is_valid():
       buku_form.save()
       return redirect('index')
    return render(request, 'buku/upload_form.html', {'upload_form':buku_form})

def delete_buku(request, buku_id):
    buku_id = int(buku_id)
    try:
        buku_sel = Buku.objects.get(id = buku_id)
    except Buku.DoesNotExist:
        return redirect('index')
    buku_sel.delete()
    return redirect('index')

# def delete_author(request, author_id):
#     author_id = int(author_id)
#     try:
#         author_sel = Author.objects.get(id = author_id)
#     except Author.DoesNotExist:
#         return redirect('index')
#     buku_sel.delete()
#     return redirect('index')

# #Menggunakan function-based
# from django.contrib.auth.decorators import login_required
#
# @login_required
# def buku_list(request):
#      if request.user.is_superuser:
#          buku = Buku.objects.all()
#      else:
#          buku = Buku.objects.filter(user=request.user)
#      return render(request, 'buku.html', {
#          'object_list': buku
#      })
#
# @login_required
# def buku_create(request):
#      form = BukuCreate(request.POST or None)
#      if form.is_valid():
#          buku = form.save(commit=False)
#          buku.user = request.user
#          buku.save()
#          return redirect('CRUD_FBVs:movies_list')
#      return render(request, 'movies_form.html', {'form': form})
#
#
# def movies_update(request, pk):
#      if request.user.is_superuser:
#          movies = get_object_or_404(Movies, pk=pk)
#      else:
#          movies = get_object_or_404(Movies, pk=pk, user=request.user)
#      form = MoviesForm(request.POST or None, instance=movies)
#      if form.is_valid():
#          form.save()
#          return redirect('CRUD_FBVs:movies_list')
#      return render(request, 'movies_form.html', {'form': form})
#
#
# def movies_delete(request, pk):
#      if request.user.is_superuser:
#          movies = get_object_or_404(Movies, pk=pk)
#      else:
#          movies = get_object_or_404(Movies, pk=pk, user=request.user)
#      if request.method == 'POST':
#          movies.delete()
#          return redirect('CRUD_FBVs:movies_list')
#      return render(request, 'confirm_delete.html', {'object': movies})

# #Menggunakan Class-based
# from django.views.generic import ListView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
#
#  class BukuList(ListView):
#      model = Buku
#
#  class BukuCreate(CreateView):
#      model = Buku
#      fields = '__all__'
#      success_url = reverse_lazy('CRUD_C: buku_list')
#
#  class BukuUpdate(UpdateView):
#      model = Buku
#      fields = '__all__'
#      success_url = reverse_lazy('CRUD_CBVs: buku_list')
#
#  class BukuDelete(DeleteView):
#      model = Buku
#      success_url = reverse_lazy('CRUD_CBVs: buku_list')
