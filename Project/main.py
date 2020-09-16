import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtTest import *
import sqlite3
import utils

baglanti = sqlite3.connect("veriler.db")
kalem = baglanti.cursor()

baslikFont = QFont("Century Gothic",38)
butonFont = QFont("Century Gothic",26)
yaziFont = QFont("Century Gothic",18)

def ustBolum(mevcutPencere):

    geriButon = QPushButton("<",mevcutPencere)
    geriButon.setFont(baslikFont)
    geriButon.setGeometry(20,20,50,50)
    geriButon.clicked.connect(mevcutPencere.geriDon)

    kapatButon = QPushButton("X",mevcutPencere)
    kapatButon.setFont(baslikFont)
    kapatButon.setGeometry(1500,20,50,50)
    kapatButon.clicked.connect(Pencere.kapat)
class intro(QWidget):
    def __init__(self):
        super().__init__()

        yatay = QHBoxLayout()

        self.yazi = QLabel("Kütüphane V1")

        yatay.addStretch()
        yatay.addWidget(self.yazi)
        yatay.addStretch()

        self.yazi.setFont(baslikFont)

        self.setLayout(yatay)
class yeniKitap(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Yeni Kitap Ekle")

        self.dikey = QVBoxLayout()

        baslik = QLabel("Yeni Kitap Ekle")
        baslik.setFont(butonFont)

        self.kitapismi = QLineEdit()
        self.kitapismi.setPlaceholderText("Kitap ismi giriniz: ")

        kaydet = QPushButton("Kaydet")
        kaydet.clicked.connect(self.kaydet)

        self.dikey.addWidget(baslik)
        self.dikey.addWidget(self.kitapismi)
        self.dikey.addWidget(kaydet)

        self.setLayout(self.dikey)

    def kaydet(self):
        kaydediliyor = QLabel("Kaydediliyor. Lütfen Bekleyin...")
        self.dikey.addWidget(kaydediliyor)
        QTest.qWait(750)
        isim = self.kitapismi.text()
        kalem.execute("INSERT INTO kitaplar  (kitap_ad) VALUES (?)",(isim,))
        baglanti.commit()

        kaydediliyor.setText("Kayıt Başarılı")
        QTest.qWait(500)
        self.close()
class yeniOgrenci(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Yeni Öğrenci Ekle")

        self.dikey = QVBoxLayout()

        baslik = QLabel("Yeni Öğrenci Ekle")
        baslik.setFont(butonFont)

        self.ogreciismi = QLineEdit()
        self.ogreciismi.setPlaceholderText("Öğrenci ismi giriniz: ")

        kaydet = QPushButton("Kaydet")
        kaydet.clicked.connect(self.kaydet)

        self.dikey.addWidget(baslik)
        self.dikey.addWidget(self.ogreciismi)
        self.dikey.addWidget(kaydet)

        self.setLayout(self.dikey)

    def kaydet(self):
        kaydediliyor = QLabel("Kaydediliyor. Lütfen Bekleyin...")
        self.dikey.addWidget(kaydediliyor)
        QTest.qWait(750)
        isim = self.ogreciismi.text()
        kalem.execute("INSERT INTO ogrenciler  (ogrenci_ad) VALUES (?)",(isim,))
        baglanti.commit()

        kaydediliyor.setText("Kayıt Başarılı")
        QTest.qWait(500)
        self.close()
class yeniOdunc(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Yeni Ödünç Alma İşlemi Ekle")

        self.dikey = QVBoxLayout()

        baslik = QLabel("Yeni Ödünç Alma İşlemi Ekle")
        baslik.setFont(butonFont)

        self.ogreciismi = QLineEdit()
        self.ogreciismi.setPlaceholderText("Öğrenci ismi giriniz: ")

        self.kitapismi = QLineEdit()
        self.kitapismi.setPlaceholderText("Öğrenci İsmini Giriniz")

        kaydet = QPushButton("Kaydet")
        kaydet.clicked.connect(self.kaydet)

        self.dikey.addWidget(baslik)
        self.dikey.addWidget(self.ogreciismi)
        self.dikey.addWidget(self.kitapismi)
        self.dikey.addWidget(kaydet)

        self.setLayout(self.dikey)

    def kaydet(self):
        kaydediliyor = QLabel("Kaydediliyor. Lütfen Bekleyin...")
        self.dikey.addWidget(kaydediliyor)
        QTest.qWait(750)
        ogrenciismi = self.ogreciismi.text()
        kitapismi = self.kitapismi.text()
        kalem.execute("INSERT INTO odunc  (ogrenci_ad,kitap_ad) VALUES (?,?)",(ogrenciismi,kitapismi))
        baglanti.commit()

        kaydediliyor.setText("Kayıt Başarılı")
        QTest.qWait(500)
        self.close()
class yeniiade(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Yeni İade İşlemi Ekle")

        self.dikey = QVBoxLayout()

        baslik = QLabel("Yeni İade İşlemi Ekle")
        baslik.setFont(butonFont)

        self.ogreciismi = QLineEdit()
        self.ogreciismi.setPlaceholderText("Öğrenci ismi giriniz: ")

        self.kitapismi = QLineEdit()
        self.kitapismi.setPlaceholderText("Öğrenci İsmini Giriniz")

        kaydet = QPushButton("Kaydet")
        kaydet.clicked.connect(self.kaydet)

        self.dikey.addWidget(baslik)
        self.dikey.addWidget(self.ogreciismi)
        self.dikey.addWidget(self.kitapismi)
        self.dikey.addWidget(kaydet)

        self.setLayout(self.dikey)

    def kaydet(self):
        kaydediliyor = QLabel("Kaydediliyor. Lütfen Bekleyin...")
        self.dikey.addWidget(kaydediliyor)
        QTest.qWait(750)
        ogrenciismi = self.ogreciismi.text()
        kitapismi = self.kitapismi.text()
        kalem.execute("DELETE FROM odunc WHERE ogrenci_ad = ? AND kitap_ad = ?",(ogrenciismi,kitapismi))
        baglanti.commit()

        kaydediliyor.setText("Kayıt Başarılı")
        QTest.qWait(500)
        self.close()
class kitapListesi(QWidget):

    def __init__(self):
        super().__init__()

        ustBolum(self)

        yatay = QHBoxLayout()
        dikey = QVBoxLayout()

        baslik = QLabel("Kitap Listesi")
        baslik.setFont(baslikFont)
        aciklama = QLabel("Durumunu görmek istediğiniz kitabın üzerine tıklayınız")
        liste = QListWidget()
        yeniEkle = QPushButton("Yeni Kitap Ekle")
        yeniEkle.setFont(butonFont)
        yeniEkle.clicked.connect(self.yeniEkle)

        kitaplar = kalem.execute("SELECT * FROM kitaplar")

        for i in kitaplar.fetchall():
            liste.addItem(i[1])

        liste.itemClicked.connect(self.kitapBilgi)

        dikey.addWidget(baslik)
        dikey.addWidget(aciklama)
        dikey.addWidget(liste)
        dikey.addWidget(yeniEkle)

        yatay.addStretch()
        yatay.addLayout(dikey)
        yatay.addStretch()

        self.setLayout(yatay)



    def kitapBilgi(self,item):

        kitapismi = item.text()
        kontrol = kalem.execute("SELECT * FROM kitaplar WHERE kitap_ad = ?", (kitapismi,))
        durum = kontrol.fetchall()[0] [2]

        if(durum==0):
            QMessageBox.information(self,"Kitap Bilgisi",kitapismi + " isimli kitap şu an boşta!")
        else:
            kimde = kalem.execute("SELECT * FROM odunc WHERE kitap_ad = ?",(kitapismi,))
            ogrenci = kimde.fetchall() [0] [1]
            QMessageBox.information(self,"Kitap Bilgisi",kitapismi +" isimli kitap şu anda " + ogrenci +" isimli öğrencide !")

    def yeniEkle(self):
        self.yeni = yeniKitap()
        self.yeni.show()

    def geriDon(self):
        self.close()
class ogrenciListesi(QWidget):
    def __init__(self):
        super().__init__()
        ustBolum(self)

        yatay = QHBoxLayout()
        dikey = QVBoxLayout()

        baslik = QLabel("Kitap Listesi")
        baslik.setFont(baslikFont)
        aciklama = QLabel("Elinde Kitap Olup Olmadığını görmek istediğiniz öğrecinin üzerine tıklayınız")
        liste = QListWidget()
        yeniEkle = QPushButton("Yeni öğrenci Ekle")
        yeniEkle.setFont(butonFont)
        yeniEkle.clicked.connect(self.yeniEkle)

        ogrenciler = kalem.execute("SELECT * FROM ogrenciler")

        for i in ogrenciler.fetchall():
            liste.addItem(i[1])

        liste.itemClicked.connect(self.ogrenciBilgi)

        dikey.addWidget(baslik)
        dikey.addWidget(aciklama)
        dikey.addWidget(liste)
        dikey.addWidget(yeniEkle)

        yatay.addStretch()
        yatay.addLayout(dikey)
        yatay.addStretch()

        self.setLayout(yatay)

    def ogrenciBilgi(self, item):

        ogrenciismi = item.text()
        kontrol = kalem.execute("SELECT * FROM odunc WHERE ogrenci_ad = ?", (ogrenciismi,))
        say = len(kontrol.fetchall())

        if (say == 0):
            QMessageBox.information(self, "Öğrenci Bilgisi", ogrenciismi + " isimli öğrencinin elinde hiç kitap yok!")
        else:
            hangi = kalem.execute("SELECT * FROM odunc WHERE ogrenci_ad = ?", (ogrenciismi,))
            kitap = hangi.fetchall() [0] [2]
            QMessageBox.information(self, "Öğrenci Bilgisi",
                                    ogrenciismi + " isimli öğrencinin elinde şu kitap var: " + kitap)



    def yeniEkle(self):
        self.yeni = yeniOgrenci()
        self.yeni.show()



    def geriDon(self):
        self.close()
class oduncListesi(QWidget):
    def __init__(self):
        super().__init__()
        ustBolum(self)

        yatay = QHBoxLayout()
        dikey = QVBoxLayout()

        baslik = QLabel("Ödünç İşlemler Listesi")
        baslik.setFont(baslikFont)
        liste = QListWidget()
        yeniEkle = QPushButton("Yeni Ödünç Alma İşlemi Ekle")
        iadeEkle = QPushButton("Yeni İade Alma İşlemi Ekle")
        yeniEkle.setFont(butonFont)
        iadeEkle.setFont(butonFont)
        yeniEkle.clicked.connect(self.yeniEkle)
        iadeEkle.clicked.connect(self.iadeEkle)

        oduncler = kalem.execute("SELECT * FROM odunc")

        for i in oduncler.fetchall():
            eklenecek = i [1] + " - " + i [2]
            liste.addItem(eklenecek)



        dikey.addWidget(baslik)

        dikey.addWidget(liste)
        dikey.addWidget(yeniEkle)
        dikey.addWidget(iadeEkle)
        yatay.addStretch()
        yatay.addLayout(dikey)
        yatay.addStretch()

        self.setLayout(yatay)



    def yeniEkle(self):
        self.yeni = yeniOdunc()
        self.yeni.show()

    def iadeEkle(self):
        self.yeni = yeniiade()
        self.yeni.show()



    def geriDon(self):
        self.close()
class yardimHakkimizda(QWidget):
    def __init__(self):
        super().__init__()
        ustBolum(self)

        yatay = QHBoxLayout()
        dikey = QVBoxLayout()

        baslik = QLabel("Yardım - Hakkımızda")
        baslik.setFont(baslikFont)
        yazi = QLabel("Kütüphane Sistemi Projesi sistemi Emre Yılmaz'a aittir.\n"
                      "Twitter : dev_emreyilmaz\n"
                      "Github : emreylmaz")
        yazi.setFont(yaziFont)



        dikey.addWidget(baslik)
        dikey.addStretch()
        dikey.addWidget(yazi)
        dikey.addStretch()

        yatay.addStretch()
        yatay.addLayout(dikey)
        yatay.addStretch()

        self.setLayout(yatay)



    def geriDon(self):
        self.close()
class Pencere(QWidget):

        def __init__(self):
            super().__init__()

            self.giris = intro()
            self.giris.showFullScreen()
            QTest.qWait(4000)

            kapatButon = QPushButton("X", self)
            kapatButon.setFont(baslikFont)
            kapatButon.setGeometry(1500, 20, 50, 50)
            kapatButon.clicked.connect(self.kapat)



            yatay = QHBoxLayout()
            dikey = QVBoxLayout()

            baslik = QLabel("Kütüphane V1")
            baslik.setFont(baslikFont)

            kitapButon = QPushButton("Kitap Listesi")
            ogrenciButon = QPushButton("Öğrenci Listesi")
            islemlerButon = QPushButton("Ödünç İşlemleri")
            yardimButon = QPushButton("Yardım-Hakkımızda")

            kitapButon.setFont(butonFont)
            ogrenciButon.setFont(butonFont)
            islemlerButon.setFont(butonFont)
            yardimButon.setFont(butonFont)


            kitapButon.clicked.connect(self.kitapAc)
            ogrenciButon.clicked.connect(self.ogrenciAc)
            islemlerButon.clicked.connect(self.islemAc)
            yardimButon.clicked.connect(self.yardimAc)



            dikey.addWidget(baslik)
            dikey.addStretch()
            dikey.addWidget(kitapButon)
            dikey.addStretch()
            dikey.addWidget(ogrenciButon)
            dikey.addStretch()
            dikey.addWidget(islemlerButon)
            dikey.addStretch()
            dikey.addWidget(yardimButon)

            yatay.addStretch()
            yatay.addLayout(dikey)
            yatay.addStretch()

            self.setLayout(yatay)




            self.showFullScreen()

        def kitapAc(self):
            self.kitap = kitapListesi()
            self.kitap.showFullScreen()
        def ogrenciAc(self):
            self.ogrenci = ogrenciListesi()
            self.ogrenci.showFullScreen()
        def islemAc(self):
            self.islem = oduncListesi()
            self.islem.showFullScreen()

        def yardimAc(self):
            self.yardim = yardimHakkimizda()
            self.yardim.showFullScreen()

        def kapat(self):
            qApp.quit()



# İlk Proje the end


uygulama = QApplication(sys.argv)
pencere = Pencere()
sys.exit(uygulama.exec())