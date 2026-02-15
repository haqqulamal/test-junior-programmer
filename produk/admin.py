from django.contrib import admin
from .models import Produk, Kategori, Status

@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ('nama_produk', 'harga', 'kategori', 'status')
    list_filter = ('kategori', 'status')
    search_fields = ('nama_produk',)

admin.site.register(Kategori)
admin.site.register(Status)
