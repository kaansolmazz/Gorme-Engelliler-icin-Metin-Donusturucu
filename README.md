<h1>Görme Engelliler İçin Web İçerik Seslendirme Uygulaması</h1>

<p>Bu proje, görme engelli bireylerin web sitelerindeki metinleri ve görselleri sesli olarak dinlemelerini sağlamak amacıyla geliştirilmiş bir uygulamadır. Uygulama, bir web sitesinin metin içeriğini alır ve bu içeriği Türkçe olarak seslendirir. Ayrıca, web sitesinde yer alan görselleri betimleyerek sesli bir şekilde kullanıcıya aktarır.</p>

<h2>Özellikler</h2>
<ul>
    <li><strong>Metin Seslendirme:</strong> Web sitesindeki metin içerikleri, Google Text-to-Speech (gTTS) kütüphanesi kullanılarak seslendirilmektedir.</li>
    <li><strong>Görsel Betimleme:</strong> Web sitesindeki görsellerin betimlenmesi için Microsoft Azure Cognitive Services API'si kullanılmaktadır.</li>
    <li><strong>Çok Dilli Destek:</strong> Metinler, otomatik olarak algılanan dilden Türkçeye çevrilip seslendirilmektedir.</li>
</ul>

<h2>Kurulum</h2>
<ol>
    <li>Bu projeyi yerel makinenize klonlayın:</li>
    <pre><code>git clone https://github.com/kullaniciadi/projeadi.git</code></pre>

    <li>Gerekli Python kütüphanelerini yükleyin:</li>
    <pre><code>pip install -r requirements.txt</code></pre>

    <p><strong>Not:</strong> <code>requirements.txt</code> dosyasına aşağıdaki kütüphaneleri eklemeyi unutmayın:</p>
    <ul>
        <li>tkinter</li>
        <li>gTTS</li>
        <li>pygame</li>
        <li>requests</li>
        <li>beautifulsoup4</li>
        <li>googletrans</li>
        <li>langdetect</li>
        <li>translate</li>
    </ul>

    <li>Uygulamayı çalıştırın:</li>
    <pre><code>python gorme_engelli.py</code></pre>
</ol>

<h2>Kullanım</h2>
<ol>
    <li>Uygulama açıldığında, seslendirmek istediğiniz web sitesinin URL'sini metin kutusuna girin.</li>
    <li>"Konuş" butonuna tıklayın.</li>
    <li>Uygulama, web sitesindeki metinleri ve görselleri seslendirerek size aktaracaktır.</li>
</ol>

<h2>Katkıda Bulunma</h2>
<p>Katkılarınızı memnuniyetle karşılıyoruz! Eğer bu projeyi geliştirmek isterseniz, lütfen bir pull request gönderin veya bir konu açın.</p>

<h2>Lisans</h2>
<p>Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için <code>LICENSE</code> dosyasına göz atın.</p>
