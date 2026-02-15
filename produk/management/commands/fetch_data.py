from django.core.management.base import BaseCommand
from produk.services import fetch_and_save_data

class Command(BaseCommand):
    help = 'Mengambil data produk dari API Fastprint'

    def handle(self, *args, **options):
        self.stdout.write('Memulai pengambilan data...')
        success, message = fetch_and_save_data()
        
        if success:
            self.stdout.write(self.style.SUCCESS(message))
        else:
            self.stdout.write(self.style.ERROR(message))
