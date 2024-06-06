"""
Aplikasi Deteksi gempa
"""
from gempa_terkini import exstratksi_data, tampilkan_data

if __name__=='__main__':
    print('Aplikasi Utama')
    result = exstratksi_data()
    tampilkan_data(result)