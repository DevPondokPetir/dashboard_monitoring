import requests
from bs4 import BeautifulSoup


def exstraksi_data():
    """
    Tanggal : 05 Juni 2024
    Waktu : 13:30:20 WIB
    Magnitudo : 4.7
    Kedalaman : 214 km
    Lokasi : ls=8.23 bt=118.00
    Pusat Gempa : Pusat gempa berada di darat 61 Km barat laut Dompu
    Dirasakan : Dirasakan (Skala MMI): II Sumbawa
    :return:
    """
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        #print(content.text)
        soup = BeautifulSoup(content.text, 'html.parser')
        title = soup.find('title')
        print(title.text)
        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div',{'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        koordinat = None
        lokasi = None
        dirasakan = None

        for res in result:
            print(i, res)
            if i == 1:
                magnitudo = res.text
            if i == 2:
                kedalaman = res.text
            if i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            if i == 4:
                lokasi = res.text
            if i == 5:
                dirasakan = res.text
            i = i + 1
        #print(soup.prettify())

        hasil = dict()
        hasil ['tanggal'] = tanggal
        hasil ['waktu'] = waktu
        hasil ['magnitudo'] = magnitudo
        hasil ['kedalaman'] = kedalaman
        hasil ['koordinat'] = {'ls': ls, 'bt':bt}
        hasil ['lokasi'] = lokasi
        hasil ['dirasakan'] = dirasakan
        return hasil
    else:
        return None


def tampilkan_data(result):
    print('\nGempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Koordinat LS ={result['koordinat']['ls']}, BT={result['koordinat']['bt']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"Dirasakan {result['dirasakan']}")