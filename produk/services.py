import requests
import hashlib
from datetime import datetime
from .models import Produk, Kategori, Status

def get_api_auth():
    # Username from requirement
    username = "tesprogrammer150226C17" 
    
    # Password format: bisacoding-hari-bulan-2digitTahun
    # Current date in context: February 15, 2026
    now = datetime.now()
    day = now.strftime("%d")
    month = now.strftime("%m")
    year = now.strftime("%y")
    
    password_str = f"bisacoding-{day}-{month}-{year}"
    password_md5 = hashlib.md5(password_str.encode()).hexdigest()
    
    return username, password_md5

def fetch_and_save_data():
    username, password = get_api_auth()
    url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"
    
    data = {
        'username': username,
        'password': password
    }
    
    try:
        # Use a session if needed for cookies but post should be fine
        response = requests.post(url, data=data)
        if response.status_code == 200:
            result = response.json()
            # Requirement says "Perhatikan response, header dan cookies"
            # Some APIs might need specific parsing
            
            if result.get('error') == 0:
                products = result.get('data', [])
                count = 0
                for item in products:
                    kategori_obj, _ = Kategori.objects.get_or_create(
                        nama_kategori=item.get('kategori')
                    )
                    status_obj, _ = Status.objects.get_or_create(
                        nama_status=item.get('status')
                    )
                    
                    Produk.objects.update_or_create(
                        id_produk=item.get('id_produk'),
                        defaults={
                            'nama_produk': item.get('nama_produk'),
                            'harga': item.get('harga'),
                            'kategori': kategori_obj,
                            'status': status_obj
                        }
                    )
                    count += 1
                return True, f"Berhasil mengambil {count} data produk."
            else:
                return False, f"API Error: {result.get('ket')}"
        else:
            return False, f"HTTP Error: {response.status_code} - {response.text}"
    except Exception as e:
        return False, str(e)
