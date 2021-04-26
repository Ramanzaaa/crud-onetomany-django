from django.db import models

# Create your models here.

class Author(models.Model):
    nama = models.CharField(max_length = 40, default = 'anonymous')
    def __str__(self):
        return self.nama

class Buku(models.Model):
    judul = models.CharField(max_length = 50)
    gambar = models.ImageField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    email = models.EmailField(blank = True)
    deskripsi = models.TextField(default = 'tanpa deskripsi')
    def __str__(self):
        return self.judul
