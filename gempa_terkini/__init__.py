def exstratksi_data():
    """
    Tanggal : 05 Juni 2024
    Waktu : 13:30:20 WIB
    Magnitudo : 4.7
    Kedalaman : 214 km
    Lokasi : LS=8.23 BT=118.00 BT
    Pusat Gempa : Pusat gempa berada di darat 61 Km barat laut Dompu
    Dirasakan : Dirasakan (Skala MMI): II Sumbawa
    :return:
    """
    hasil = dict()
    hasil ['tanggal'] = '05 Juni 2024'
    hasil ['waktu'] = '13:30:20 WIB'
    hasil ['magnitudo'] = 4.0
    hasil ['lokasi'] = {'ls': 8.23, 'bt':118.00}
    hasil ['pusat'] = "Pusat gempa berada di darat 61 Km barat laut Dompu"
    hasil ['dirasakan'] = "Dirasakan (Skala MMI): II Sumbawa"
    return hasil


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi LS ={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")