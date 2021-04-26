from django.urls import path
from . import views
from appbuku.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-buku'),
    path('tambah_author/', views.tambah_author, name = 'tambah-author'),
    path('update/<int:buku_id>', views.update_buku),
    path('delete/<int:buku_id>', views.delete_buku)
]
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
