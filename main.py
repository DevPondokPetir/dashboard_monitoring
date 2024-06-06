"""
Aplikasi Deteksi gempa
"""
import gempa_terkini

if __name__=='__main__':
    print('Aplikasi Utama')
    result = gempa_terkini.exstraksi_data()
    gempa_terkini.tampilkan_data(result)