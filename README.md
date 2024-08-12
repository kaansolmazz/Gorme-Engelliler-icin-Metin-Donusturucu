Görme Engelliler İçin Web İçerik Seslendirme Uygulaması
Bu proje, görme engelli bireylerin web sitelerindeki metinleri ve görselleri sesli olarak dinlemelerini sağlamak amacıyla geliştirilmiş bir uygulamadır. Uygulama, bir web sitesinin metin içeriğini alır ve bu içeriği Türkçe olarak seslendirir. Ayrıca, web sitesinde yer alan görselleri betimleyerek sesli bir şekilde kullanıcıya aktarır.

Özellikler
Metin Seslendirme: Web sitesindeki metin içerikleri, Google Text-to-Speech (gTTS) kütüphanesi kullanılarak seslendirilmektedir.
Görsel Betimleme: Web sitesindeki görsellerin betimlenmesi için Microsoft Azure Cognitive Services API'si kullanılmaktadır.
Çok Dilli Destek: Metinler, otomatik olarak algılanan dilden Türkçeye çevrilip seslendirilmektedir.
Kurulum
Bu projeyi yerel makinenize klonlayın:

bash
Kodu kopyala
git clone https://github.com/kullaniciadi/projeadi.git
Gerekli Python kütüphanelerini yükleyin:

bash
Kodu kopyala
pip install -r requirements.txt
Not: requirements.txt dosyasına aşağıdaki kütüphaneleri eklemeyi unutmayın:

tkinter
gTTS
pygame
requests
beautifulsoup4
googletrans
langdetect
translate
Uygulamayı çalıştırın:

bash
Kodu kopyala
python gorme_engelli.py
Kullanım
Uygulama açıldığında, seslendirmek istediğiniz web sitesinin URL'sini metin kutusuna girin.
"Konuş" butonuna tıklayın.
Uygulama, web sitesindeki metinleri ve görselleri seslendirerek size aktaracaktır.
Katkıda Bulunma
Katkılarınızı memnuniyetle karşılıyoruz! Eğer bu projeyi geliştirmek isterseniz, lütfen bir pull request gönderin veya bir konu açın.

Lisans
Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına göz atın.
