from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Produk, Status
from .forms import ProdukForm

class ProdukListView(ListView):
    model = Produk
    template_name = 'produk/list.html'
    context_object_name = 'produk_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        status_filter = self.request.GET.get('status')
        if status_filter == 'bisa_dijual':
            # Filtering menggunakan QuerySet
            queryset = queryset.filter(status__nama_status='bisa dijual')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_filter'] = self.request.GET.get('status')
        return context

class ProdukCreateView(CreateView):
    model = Produk
    form_class = ProdukForm
    template_name = 'produk/form.html'
    success_url = reverse_lazy('produk:list')

    def form_valid(self, form):
        messages.success(self.request, "Produk berhasil ditambahkan.")
        return super().form_valid(form)

class ProdukUpdateView(UpdateView):
    model = Produk
    form_class = ProdukForm
    template_name = 'produk/form.html'
    success_url = reverse_lazy('produk:list')

    def form_valid(self, form):
        messages.success(self.request, "Produk berhasil diubah.")
        return super().form_valid(form)

class ProdukDeleteView(DeleteView):
    model = Produk
    template_name = 'produk/confirm_delete.html'
    success_url = reverse_lazy('produk:list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Produk berhasil dihapus.")
        return super().delete(request, *args, **kwargs)
