import requests
from bs4 import BeautifulSoup

def hava_durumu_getir(sehir):
    url = f'https://www.google.com/search?q={sehir}+hava+durumu'

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Verileri ayıklama (bu kısım web sitesinin yapısına göre değişebilir)
        sicaklik = soup.find('span', {'class': 'wob_t'}).text
        aciklama = soup.find('span', {'id': 'wob_dc'}).text
        # ... diğer verileri de benzer şekilde ayıklayabilirsiniz

        print(f"{sehir} için hava durumu:")
        print(f"Sıcaklık: {sicaklik}")
        print(f"Açıklama: {aciklama}")
        # ... diğer verileri de yazdırabilirsiniz

    except requests.exceptions.RequestException as e:
        print(f"Hata: {e}")
    except AttributeError as e:
        print(f"Hata: Beklenmeyen web sitesi yapısı: {e}")

if __name__ == "__main__":
    sehir = input("Hava durumu için bir şehir girin: ")
    hava_durumu_getir(sehir)