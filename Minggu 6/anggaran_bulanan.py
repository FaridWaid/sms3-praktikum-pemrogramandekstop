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

#membuat QLineEdit dengan nama variabel anggaran, cal_button, hasil 
self.anggaran = QLineEdit(self)
#membuat sebuah button dengan nama variable cal_button
self.cal_button = QPushButton("Calculate", self)
#membuat sebuah button dengan nama variable hasil4
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
    tab.addTab(group,"Anngaran Bulanan")

    #memasukkan tab kedalam layout utama grid
    grid.addWidget(tab, 2, 1)

    #------------------------- KELOMPOK 1 -------------------------#
    #membuat label1 dan akan dimasukkan ke dalam layout vbox
    label1 = QLabel(self)
    label1.setText("Masukkan Jumlah Pendapatan Anda per Bulan:")
    vbox.addWidget(label1)
    
    #mengatur anggaran dengan border 0.5 px dan berwarna solid black
    self.anggaran.setStyleSheet("border: 0.5px solid black;")
    #memasukkan anggaran kedalam layout vbox
    vbox.addWidget(self.anggaran)
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
    #menambahkan addStretch ke dalam vbox agar tertata rapi
    vbox.addStretch(1)

    #connect button to fungsi on_click
    self.cal_button.clicked.connect(on_click)
    #------------------------- END OF KELOMPOK 1 -------------------------#
    
    #membuat grid menjadi layout utama di window
    ex.setLayout(grid)

    #Menentukan ukuran window dan title untuk menampilkan
    ex.setGeometry(100,100,500,300)
    #membuat judul window
    ex.setWindowTitle("Simulasi Anggaran Bulanan")
    #menampilan isi dari variabel ex
    ex.show()
    #membuat system exit
    #sys.exit(app.exec_())

#membuat fungsi on_click yang berisi sistem untuk menghitung nilai Anggaran
def on_click():   
    #membuat variabel Anggaran yang berisi inputan dari anggaran yang akan dirubah menjadi sebuah float
    Anggaran = float(self.anggaran.text())
    #membuat variabel pokok, cicilan, nabung, lifestyle untuk menghitung nilai Anggaran  
    pokok = Anggaran * 0.5
    cicilan = Anggaran * 0.3
    nabung = Anggaran * 0.15
    lifestyle = Anggaran * 0.05
    #menampilkan nilai Anggaran pada button hasil
    self.hasil.setText("Nilai Anggaran Pokok: Rp." + str("%.2f" %pokok) + "\n Nilai Anggaran Cicilan: Rp." + str("%.2f" %cicilan) + "\n Nilai Anggaran Menabung: Rp." + str("%.2f" %nabung) + "\n Nilai Anggaran Lifestyle: Rp." + str("%.2f" %lifestyle))


if __name__ == '__main__':
    #memanggil fungsi Layout untuk menampilkan seluruh isi widget
    Layout()
    