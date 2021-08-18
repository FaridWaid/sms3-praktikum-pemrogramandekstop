import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtSql
import sqlite3
import MySQLdb as mdb
import pymysql.cursors

class Film(QWidget):
   #Membuat fungsi init untuk inisialisasi class Mahasiswa
    def __init__(self):
        #untuk mengembalikan semua atribut dan method yang ada
        super().__init__()
        #membuka database
        self.OpenDatabase()
        #memanggil fungsi Layout yang sudah dibuat agar ditampilkan hasilnya
        self.Layout()
        

    def OpenDatabase(self):
        try:
            self.db = mdb.connect('kprikaryasehat.site', 'kprikary_kuliah', 'unijoyo2020', 'kprikary_resto')
            QMessageBox.about(self, 'Connection', 'Database Connected Successfully')
 
        except mdb.Error as e:
            QMessageBox.about(self, 'Connection', 'Failed To Connect Database')

    def Layout(self):
        #Membuat Grid Layout
        grid = QGridLayout()

        add_data = QLabel("Tambah Data:")
        grid.addWidget(add_data,0,0)

        menu = QLabel("Nama Menu:")
        grid.addWidget(menu,2,0)

        self.Menu = QLineEdit(self)
        grid.addWidget(self.Menu,2,1,1,2)
        self.Menu.setStyleSheet("background-color: #f6f6f6;")

        keterangan = QLabel("Keterangan:")
        grid.addWidget(keterangan,3,0)

        self.Keterangan = QLineEdit(self)
        grid.addWidget(self.Keterangan,3,1,1,2)
        self.Keterangan.setStyleSheet("background-color: #f6f6f6;")

        harga = QLabel("Harga:")
        grid.addWidget(harga,4,0)

        self.Harga = QLineEdit(self)
        grid.addWidget(self.Harga,4,1,1,2)
        self.Harga.setStyleSheet("background-color: #f6f6f6;")

        satuan = QLabel("Satuan:")
        grid.addWidget(satuan,5,0)

        self.Satuan = QLineEdit(self)
        grid.addWidget(self.Satuan,5,1,1,2)
        self.Satuan.setStyleSheet("background-color: #f6f6f6;")
        
        add_button = QPushButton("Tambah Data")
        grid.addWidget(add_button,6,0,1,0)
        add_button.setStyleSheet("background-color: #ffc7c7;")

        edit_button = QPushButton("Edit Data")
        grid.addWidget(edit_button,7,0,1,1)
        edit_button.setStyleSheet("background-color: #ffc7c7;")

        update_button = QPushButton("Update Data")
        grid.addWidget(update_button,7,1,1,2)
        update_button.setStyleSheet("background-color: #ffc7c7;")

        search = QLabel("Cari Data:")
        grid.addWidget(search,8,0)
        
        self.Cari = QLineEdit(self)
        grid.addWidget(self.Cari,8,1)
        self.Cari.setStyleSheet("background-color: #f6f6f6;")

        search_button = QPushButton("Cari")
        grid.addWidget(search_button,8,2)
        search_button.setStyleSheet("background-color: #ffc7c7;")

        delete_button = QPushButton("Delete Data")
        grid.addWidget(delete_button,9,0,1,0)
        delete_button.setStyleSheet("background-color: #ffc7c7;")

        #Membuat widget table widget yang diberi nama "Data" dan akan dimasukkan ke dalam layout Grid
        self.tablewidget = QTableWidget(self)
        self.tablewidget.setObjectName("Data")
        self.tablewidget.setStyleSheet("background-color: #f6f6f6;")
        grid.addWidget(self.tampilData(),11,0,5,0)
        
        #Ketika button di klik akan memanggi fungsi masing - masing
        add_button.clicked.connect(self.tambahData)
        search_button.clicked.connect(self.filterData)
        edit_button.clicked.connect(self.editData)
        update_button.clicked.connect(self.updateData)
        delete_button.clicked.connect(self.deleteData)

        #Layout grid di jadikan layout utama
        self.setLayout(grid)

    #Fungsi menampilkan Data menu1 ke dalam tabelwidget
    def tampilData(self):
        # Membuat Cursor
        cur = self.db.cursor()
        # Mengeksekusi perintah sql
        cur.execute("SELECT * FROM menu1")
        # Mengambil Semua Data
        data = cur.fetchall()
        # Menjadikan Data bentuk list
        record = list(data)
        # Membuat Baris Yang Akan Ditampilkan DI table
        self.tablewidget.setRowCount(len(record)+1)
        # Membuat Kolom yang akan ditampilkan di table
        self.tablewidget.setColumnCount(8)
        # Membuat Header
        self.tablewidget.setItem(0, 0, QTableWidgetItem("ID Menu"))
        self.tablewidget.setItem(0, 1, QTableWidgetItem("ID Menu Kat"))
        self.tablewidget.setItem(0, 2, QTableWidgetItem("ID Resto"))
        self.tablewidget.setItem(0, 3, QTableWidgetItem("Nama Menu"))
        self.tablewidget.setItem(0, 4, QTableWidgetItem("Keterangan"))
        self.tablewidget.setItem(0, 5, QTableWidgetItem("Gambar"))
        self.tablewidget.setItem(0, 6, QTableWidgetItem("Harga"))
        self.tablewidget.setItem(0, 7, QTableWidgetItem("Satuan"))
        # Menampilkan Data Yang Diambil Dari SQL
        for i in range(len(record)):
            baris = i + 1
            self.tablewidget.setItem(baris, 0, QTableWidgetItem(str(record[i][0])))
            self.tablewidget.setItem(baris, 1, QTableWidgetItem(str(record[i][1])))
            self.tablewidget.setItem(baris, 2, QTableWidgetItem(str(record[i][2])))
            self.tablewidget.setItem(baris, 3, QTableWidgetItem(str(record[i][3])))
            self.tablewidget.setItem(baris, 4, QTableWidgetItem(str(record[i][4])))
            self.tablewidget.setItem(baris, 5, QTableWidgetItem(str(record[i][5])))
            self.tablewidget.setItem(baris, 6, QTableWidgetItem(str(record[i][6])))
            self.tablewidget.setItem(baris, 7, QTableWidgetItem(str(record[i][7])))
        # Membuat Agar Table Strech
        self.tablewidget.horizontalHeader().setStretchLastSection(True)
        self.tablewidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        cur.close()
        return self.tablewidget

    #Fungsi tambah Data ke dalam tabel menu1
    def tambahData(self):
        # Mengambil Text inputan
        menu = str(self.Menu.text())
        keterangan = str(self.Keterangan.text())
        harga = int(self.Harga.text())
        satuan = str(self.Satuan.text())
        # Mendefinisikan Cursor
        cur = self.db.cursor()
        id = self.db.cursor()
        # Menjalankan Perintah SQL
        id.execute("SELECT idmenu FROM menu1 ORDER BY idmenu DESC LIMIT 1")
        # Mengambil Satu Data
        idMenu = id.fetchone()
        # Membuat Id Auto Increment
        idMenu = idMenu[0] + 1
        # Menuliskan Perintah SQL
        sql = "INSERT INTO menu1(idmenu,idmenukat,idresto,namamenu,keterangan,filegambar,harga,satuan) VALUES ('%d','%d','%d','%s','%s','%s','%d','%s')" % (idMenu, 1, 5,menu,keterangan,'https://img-global.cpcdn.com/recipes/84fae0149dbe9168/751x532cq70/telor-balado-foto-resep-utama.jpg',harga,satuan)
        # MenjalanKan Perintah Try
        try:
            # Eksekusi Perintah SQL
            cur.execute(sql)
            # Mengcommit agar perubahan Tersimpan
            self.db.commit()
            # Membuat Notifikasi Berhasil Tambah Data
            QMessageBox.about(self, 'Berhasil', 'Berhasil Menambah Data')
            # Mengubah Inputan Agar Menjadi Kosong
            self.Menu.setText("")
            self.Keterangan.setText("")
            self.Harga.setText("")
            self.Satuan.setText("")
            # Menampilkan Data
            self.tampilData()
            id.close()
            cur.close()
        # Jika Terjadi Error
        except:
            # Merollback data
            self.db.rollback()
            print("Gagal")
     #Fungsi edit Data tabel menu1   
    def editData(self):
        # Mengambil Data Yang DIpilih
        index = self.tablewidget.selectedIndexes()[0]
        id = self.tablewidget.model().data(index)
        # Membuat Cursor
        cur = self.db.cursor()
        # Perintah Mencari Data Bedasarkan ID
        sql = "SELECT * FROM menu1 WHERE idmenu = '%s' " % (id)
        # Eksekusi Perintah SQL
        cur.execute(sql)
        # Mengambil Satu Data
        data = cur.fetchone()
        # Menyimpan Data Id Di variabel idEdit
        self.idEdit = data[0]
        # Menampilkan Data Ke Textbox
        self.Menu.setText(data[3])
        self.Keterangan.setText(data[4])
        self.Harga.setText(str(data[6]))
        self.Satuan.setText(data[7])

    # Fungsi Update Data menu1
    def updateData(self):
        # Mengambil Data Dari Inputan
        menu = str(self.Menu.text())
        keterangan = str(self.Keterangan.text())
        harga = int(self.Harga.text())
        satuan = str(self.Satuan.text())
        # Membuat Cursor
        cur = self.db.cursor()
        # Perintah SQL Update
        sql = "UPDATE menu1 SET namamenu = '%s', keterangan = '%s', harga = '%d', satuan = '%s' WHERE idmenu = '%d'" % (menu,keterangan,harga,satuan,self.idEdit)
        try:
            # Eksekusi Perintah SQL
            cur.execute(sql)
            # Commit DB Agar Terjadi Perubahan DI database
            self.db.commit()
            # Membuat Message Box
            QMessageBox.about(self, 'Berhasil', 'Berhasil Update Data')
            self.Menu.setText("")
            self.Keterangan.setText("")
            self.Harga.setText("")
            self.Satuan.setText("")
            self.tampilData()
            print("Berhasil")
        except:
            self.db.rollback()
            print("Gagal")

    # Fungsi Hapus Data pada table menu1
    def deleteData(self):
        # Mengambil Data Yang Di pilih
        index = self.tablewidget.selectedIndexes()[0]
        id = self.tablewidget.model().data(index)
        # Membuat Cursor
        cur = self.db.cursor()
        # Perintah SQL Untuk Menghapus Data
        sql = "DELETE FROM menu1 WHERE idmenu = '%s' " % (id)
        try:
            # Eksekusi Perintah SQL
            cur.execute(sql)
            # Commit Ke Database Agar Perubahan Tersimpan
            self.db.commit()
            # Menampilkan Data
            self.tampilData()
            print("Berhasil")
        except:
            # Merollback data
            self.db.rollback()
            print("Gagal")

    #Fungsi serching Data yang ada di dalam tabel menu1
    def filterData(self):
        # Membuat Cursor
        cur = self.db.cursor()
        filter_search = str(self.Cari.text())
        # Mengeksekusi perintah sql
        cur.execute("SELECT * FROM menu1 WHERE namamenu LIKE '%"+str(filter_search)+"%' OR keterangan LIKE '%"+str(filter_search)+"%' OR harga LIKE '%"+str(filter_search)+"%' OR satuan LIKE '%"+str(filter_search)+"%'")
        # Mengambil Semua Data
        data = cur.fetchall()
        # Menjadikan Data bentuk list
        record = list(data)
        # Membuat Baris Yang Akan Ditampilkan DI table
        self.tablewidget.setRowCount(len(record)+1)
        # Membuat Kolom yang akan ditampilkan di table
        self.tablewidget.setColumnCount(8)
        # Membuat Header
        self.tablewidget.setItem(0, 0, QTableWidgetItem("ID Menu"))
        self.tablewidget.setItem(0, 1, QTableWidgetItem("ID Menu Kat"))
        self.tablewidget.setItem(0, 2, QTableWidgetItem("ID Resto"))
        self.tablewidget.setItem(0, 3, QTableWidgetItem("Nama Menu"))
        self.tablewidget.setItem(0, 4, QTableWidgetItem("Keterangan"))
        self.tablewidget.setItem(0, 5, QTableWidgetItem("Gambar"))
        self.tablewidget.setItem(0, 6, QTableWidgetItem("Harga"))
        self.tablewidget.setItem(0, 7, QTableWidgetItem("Satuan"))
        # Menampilkan Data Yang Diambil Dari SQL
        for i in range(len(record)):
            baris = i + 1
            self.tablewidget.setItem(baris, 0, QTableWidgetItem(str(record[i][0])))
            self.tablewidget.setItem(baris, 1, QTableWidgetItem(str(record[i][1])))
            self.tablewidget.setItem(baris, 2, QTableWidgetItem(str(record[i][2])))
            self.tablewidget.setItem(baris, 3, QTableWidgetItem(str(record[i][3])))
            self.tablewidget.setItem(baris, 4, QTableWidgetItem(str(record[i][4])))
            self.tablewidget.setItem(baris, 5, QTableWidgetItem(str(record[i][5])))
            self.tablewidget.setItem(baris, 6, QTableWidgetItem(str(record[i][6])))
            self.tablewidget.setItem(baris, 7, QTableWidgetItem(str(record[i][7])))
        # Membuat Agar Table Strech
        self.tablewidget.horizontalHeader().setStretchLastSection(True)
        self.tablewidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        cur.close()
        return self.tablewidget

if __name__ == '__main__':
    #Inisisalisai pyqt
    app = QApplication(sys.argv)
    #mengatur style di window menjadi style fusion
    app.setStyle("fusion")
    #membuat variabel ex yang berisi class FormulaMath
    ex = Film()
    ex.setStyleSheet("background-color: #fcf1f1;")
    ye = QPushButton()
    

    #Menentukan ukuran window dan title untuk menampilkan
    ex.setGeometry(100,100,800,600)
    #membuat judul window
    ex.setWindowTitle("Database Mysql in Pyqt5")
    #menampilan isi dari variabel ex
    ex.show()
    #membuat system exit
    sys.exit(app.exec_())