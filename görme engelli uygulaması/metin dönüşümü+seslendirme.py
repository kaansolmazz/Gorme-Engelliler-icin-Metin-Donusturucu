
import tkinter as tk
from tkinter import scrolledtext
from gtts import gTTS
import os
from io import BytesIO
import pygame
import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import json
from translate import Translator
from langdetect import detect





class GormeEngelli:
    def __init__(self, root):
        self.root = root
        root.title("Görme Engelli Uygulama")
        self.url_entry = tk.Entry(root, width=40)
        self.url_entry.pack(pady=10)

        self.button = tk.Button(root, text="Konuş", command=self.convert_and_play)
        self.button.pack(pady=10)

    def convert_and_play(self):
        try:
            url = self.url_entry.get()
            response = requests.get(url)
            response.raise_for_status()
            html = response.text

            soup = BeautifulSoup(html, 'html.parser')

            self.text_areas = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'img'])
            self.img_areas = soup.find_all('img')

            total_text = " "
            kacinci_resim = 0
            resimler = self.resim()
            print(resimler)
            for text_area in self.text_areas:
                if text_area.name == 'img':
                    if resimler[kacinci_resim]!='99999':
                        total_text = total_text + " burada " + resimler[kacinci_resim] + " görseli bulunmaktadır "
                    else:
                        total_text = total_text + " " + resimler[kacinci_resim]
                    print(resimler[kacinci_resim])
                    kacinci_resim = kacinci_resim + 1
                else:
                    total_text = total_text + " " + str(text_area.get_text())


            print(total_text)


            # Metni ses dosyasına çevirdiğimiz kısım
            cikti = gTTS(text=total_text, lang='tr', slow=False)

            ses_buffer = BytesIO()
            cikti.write_to_fp(ses_buffer)

            ses_buffer.seek(0)

            pygame.mixer.init()
            pygame.mixer.music.load(ses_buffer)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue

        except requests.exceptions.RequestException as e:
            hata = f"Hata: {e}"
            print(hata)

    def resim(self):
        print("çalıştı resim")
        resimler = []
        for img_tag in self.img_areas:
            img_url = img_tag.get('src')
            if img_url:
                try:
                    img_response = requests.get(img_url)
                    if img_response.status_code == 200:
                        image_bytes = BytesIO(img_response.content)

                        metin1 = self.donus(image_bytes)
                        metin2 = self.cevir_text(metin1)
                        resimler.append(metin2)

                except Exception as genel_hata:
                    print(genel_hata)
                    resimler.append("99999")

        if 0 < len(resimler):
            print("resimler gönderildi")
            return resimler
        else:
            print("Hatalı indeks. Geçerli bir indeks giriniz.")
            return None

    def cevir_text(self,text, dest_lang='tr'):
        source_lang = detect(text)
        translator = Translator(to_lang=dest_lang, from_lang=source_lang)
        translation = translator.translate(text)
        return translation
    def donus(self, imgdata):
        api_key = 'b365ef8ad4e14b1a99c7ae8cdf169001'
        api_endpoint = 'https://hkextensionvision.cognitiveservices.azure.com/vision/v3.2'
        headers = {
            "Ocp-Apim-Subscription-Key": api_key,
            "Content-Type": "application/octet-stream"
        }

        params = {
            "visualFeatures": "Description",
            "language": "en",
            "model-version": "latest"
        }

        try:
            response = requests.post(
                f"{api_endpoint}/analyze",
                headers=headers,
                params=params,
                data=imgdata
            )

            response.raise_for_status()
            data = json.loads(response.text)
            text = data["description"]["captions"][0]["text"]
            return text
        except requests.exceptions.RequestException as e:
            print(f"Hata: {e}")
            return None

if __name__ == "__main__":
    root = tk.Tk()
    ge = GormeEngelli(root)
    root.mainloop()


