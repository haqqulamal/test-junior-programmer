from django.db import models

class Kategori(models.Model):
    id_kategori = models.AutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_kategori

    class Meta:
        verbose_name_plural = "Kategori"

class Status(models.Model):
    id_status = models.AutoField(primary_key=True)
    nama_status = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_status

    class Meta:
        verbose_name_plural = "Status"

class Produk(models.Model):
    id_produk = models.AutoField(primary_key=True)
    nama_produk = models.CharField(max_length=255)
    harga = models.DecimalField(max_digits=12, decimal_places=0)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_produk

    class Meta:
        verbose_name_plural = "Produk"
