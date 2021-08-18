import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

#GLOBAL
#Inisisalisai pyqt
app = QApplication(sys.argv)
#mengatur style di window menjadi style fusion
app.setStyle("fusion")

#membuat variabel ex yang berisi fungsi QWidget
ex = QWidget()
#variabel self berisi nilai ex yang berarti berisi QWidget
self = ex

#membuat QLineEdit dengan nama variabel pinjaman, waktu, bunga  
self.pinjaman = QLineEdit(self)
self.waktu = QLineEdit(self)
self.bunga = QLineEdit(self)
#membuat sebuah button dengan nama variable cal_button
self.cal_button = QPushButton("Calculate", self)
#membuat sebuah button dengan nama variable hasil
self.hasil = QPushButton("Hasil", self)

#membuat fungsi dengan nama Layout
def Layout():
    #membuat grid layout dengan nama variabel grid
    grid = QGridLayout()
    #mengatur batas pada isi conten layout grid yaitu batas kana,kiri,atas,bawah bernilai 10
    grid.setContentsMargins(10,10,10,10)

    #membuat sebuag QTabWidget dengan nama variabel tab
    tab = QTabWidget(self)
    #mengatur semua isi konten yang ada di tab menjadi tulisan bold berwarna hitam dengan ukuran 15px
    tab.setStyleSheet("font: bold 15px; color: black;")

    #membuat QVBoxLayout dengan nama variabel vbox
    vbox = QVBoxLayout()

    #membuat groupbox 
    group = QGroupBox(self)

    #membuat vbox menjadi layout 
    group.setLayout(vbox)

    #memasukkan group kedalam variabel tab atau QTabWidget
    tab.addTab(group,"Simulasi Peminjaman")

    #memasukkan tab kedalam layout utama grid
    grid.addWidget(tab, 2, 1)

    #------------------------- KELOMPOK 1 -------------------------#
    #membuat label1 dan akan dimasukkan ke dalam layout vbox
    label1 = QLabel(self)
    label1.setText("Masukkan Jumlah Peminjaman:")
    vbox.addWidget(label1)
    
    #mengatur pinjaman dengan border 0.5 px dan berwarna solid black
    self.pinjaman.setStyleSheet("border: 0.5px solid black;")
    #memasukkan volume1 kedalam layout vbox
    vbox.addWidget(self.pinjaman)
    #menambahkan addStretch ke dalam vbox agar tertata rapi
    vbox.addStretch()

    #membuat label1 dan akan dimasukkan ke dalam layout vbox
    label1 = QLabel(self)
    label1.setText("Masukkan Jangka Waktu Peminjaman (Dalam Bulan):")
    vbox.addWidget(label1)
    
    #mengatur waktu dengan border 0.5 px dan berwarna solid black
    self.waktu.setStyleSheet("border: 0.5px solid black;")
    #memasukkan waktu kedalam layout vbox
    vbox.addWidget(self.waktu)
    #menambahkan addStretch ke dalam vbox agar tertata rapi
    vbox.addStretch()

    #membuat label1 dan akan dimasukkan ke dalam layout vbox
    label1 = QLabel(self)
    label1.setText("Masukkan Bunga Peminjaman:")
    vbox.addWidget(label1)
    
    #mengatur bunga dengan border 0.5 px dan berwarna solid black
    self.bunga.setStyleSheet("border: 0.5px solid black;")
    #memasukkan bunga kedalam layout vbox
    vbox.addWidget(self.bunga)
    #menambahkan addStretch ke dalam vbox agar tertata rapi
    vbox.addStretch()

    #mengatur cal_button dengan background berwarna #33f8c7
    self.cal_button.setStyleSheet("background-color: #33f8c7;")
    #memasukkan cal_button kedalam layout vbox
    vbox.addWidget(self.cal_button)
    #menambahkan addStretch ke dalam vbox agar tertata rapi
    vbox.addStretch(1)
    
    ##mengatur hasil dengan font bold dan ukuran 20px dan berwarna hitam
    self.hasil.setStyleSheet("font: bold 20px; color: black")
    #mengatur button hasil dengan setDisabled agar tidak daat diklik
    self.hasil.setDisabled(True)
    #memasukkan button hasil ke dalam layout vbox
    vbox.addWidget(self.hasil)
    #menambahkan addStretch ke dalam vbox4 agar tertata rapi
    vbox.addStretch(1)

    #connect button to fungsi on_click
    self.cal_button.clicked.connect(on_click)
    #------------------------- END OF KELOMPOK 1 -------------------------#
    
    #membuat grid menjadi layout utama di window
    ex.setLayout(grid)

    #Menentukan ukuran window dan title untuk menampilkan
    ex.setGeometry(100,100,500,300)
    #membuat judul window
    ex.setWindowTitle("Simulasi Peminjaman")
    #menampilan isi dari variabel ex
    ex.show()
    #membuat system exit
    sys.exit(app.exec_())

#membuat fungsi on_click yang berisi sistem untuk menghitung nilai Simulasi Pemnjaman
def on_click():   
    #membuat variabel Pinjaman, Waktu, Bunga yang berisi inputan dari pinjaman, waktu, bunga yang akan dirubah menjadi sebuah float
    Pinjaman = float(self.pinjaman.text())
    Waktu = float(self.waktu.text())
    Bunga = (float(self.bunga.text()) / 100)

    Total = Pinjaman + (Pinjaman + Waktu + Bunga)
    #menampilkan nilai simulasi peminjaman pada button hasil
    self.hasil.setText("Nilai Peminjaman yang harus di bayarkan: Rp." + str("%.2f" %Total))


if __name__ == '__main__':
    #memanggil fungsi Layout untuk menampilkan seluruh isi widget
    Layout()
    