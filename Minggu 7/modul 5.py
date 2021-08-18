import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtSql
import sqlite3

class Film(QWidget):
   #Membuat fungsi init untuk inisialisasi class Mahasiswa
    def __init__(self):
        #untuk mengembalikan semua atribut dan method yang ada
        super().__init__()
        #membuka database
        self.OpenDatabase()
        self.createTabel()
        #memanggil fungsi Layout yang sudah dibuat agar ditampilkan hasilnya
        self.Layout()
        

    def OpenDatabase(self):
        #Mendeklarasikan database
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        #Membuat nama database
        db.setDatabaseName('test.db')
        #Mengecek Database Apakah sudah terkoneksi atau belum
        if db.open():
            print('Berhasil membuka Database')
        else:
            print('Gagal membuka Database!')

    def createTabel(self): 
        query = QtSql.QSqlQuery() 
        query.exec_("create table listfilm(" "id integer primary key AUTOINCREMENT, " 
        "judul varchar(20), tahun_rilis int(10), genre varchar(20), review varchar(100), rating varchar(20))") 
        print ("True")

    def Layout(self):
        #Membuat Grid Layout
        grid = QGridLayout()

        #Membuat label, Line Edit, dan Button yang akan dimasukkan ke dalam layout Grid
        open_database = QLabel("Buka Database")
        grid.addWidget(open_database,0,0)

        open_button = QPushButton("Open Database")
        grid.addWidget(open_button,0,1,1,2)
        open_button.setStyleSheet("background-color: #ffc7c7;")

        add_data = QLabel("Tambah Data:")
        grid.addWidget(add_data,1,0,1,0)

        add_id = QLabel("ID:")
        grid.addWidget(add_id,2,0)

        self.Id = QLineEdit(self)
        grid.addWidget(self.Id,2,1,1,2)
        self.Id.setStyleSheet("background-color: #f6f6f6;")

        add_judul = QLabel("Judul:")
        grid.addWidget(add_judul,3,0)

        self.Judul = QLineEdit(self)
        grid.addWidget(self.Judul,3,1,1,2)
        self.Judul.setStyleSheet("background-color: #f6f6f6;")

        tahun_rilis = QLabel("Tahun Rilis FIlm:")
        grid.addWidget(tahun_rilis,4,0)

        self.Tahun = QLineEdit(self)
        grid.addWidget(self.Tahun,4,1,1,2)
        self.Tahun.setStyleSheet("background-color: #f6f6f6;")

        add_genre = QLabel("Genre:")
        grid.addWidget(add_genre,5,0)

        self.Genre = QLineEdit(self)
        grid.addWidget(self.Genre,5,1,1,2)
        self.Genre.setStyleSheet("background-color: #f6f6f6;")

        add_review = QLabel("Review:")
        grid.addWidget(add_review,6,0)

        self.Review = QTextEdit(self)
        grid.addWidget(self.Review,6,1,1,2)
        self.Review.setStyleSheet("background-color: #f6f6f6;")

        add_rating = QLabel("Rating:")
        grid.addWidget(add_rating,7,0)

        self.Rating = QLineEdit(self)
        grid.addWidget(self.Rating,7,1,1,2)
        self.Rating.setStyleSheet("background-color: #f6f6f6;")
        
        add_button = QPushButton("Tambah Data")
        grid.addWidget(add_button,8,0,1,0)
        add_button.setStyleSheet("background-color: #ffc7c7;")

        search = QLabel("Cari Data:")
        grid.addWidget(search,9,0)
        
        self.Cari = QLineEdit(self)
        grid.addWidget(self.Cari,9,1)
        self.Cari.setStyleSheet("background-color: #f6f6f6;")

        search_button = QPushButton("Cari")
        grid.addWidget(search_button,9,2)
        search_button.setStyleSheet("background-color: #ffc7c7;")

        #Membuat widget table view yang diberi nama "Data" dan akan dimasukkan ke dalam layout Grid
        self.tableview = QTableView(self)
        self.tableview.setObjectName("Data")
        grid.addWidget(self.tableview,10,0,1,0)
        self.tableview.setStyleSheet("background-color: #f6f6f6;")
        
        #Ketika button di klik akan memanggi fungsi masing - masing
        open_button.clicked.connect(self.tampilData)
        add_button.clicked.connect(self.tambahData)
        search_button.clicked.connect(self.filterData)

        #Layout grid di jadikan layout utama
        self.setLayout(grid)

    #Fungsi untuk menampilankan data di dalam table
    def tampilData(self):
        #Membuat Model
        model = QSqlQueryModel()
        #Mendefinisikan sql
        sql = "SELECT * FROM listfilm"
        #Mengeksekusi Model Query
        model.setQuery(sql)
        #Mengeset Data Model Ke table view
        self.tableview.setModel(model)
        #self.tableview.setWindowTitle(title)
        return self.tableview

    #Fungsi tambah Data ke dalam tabel mahasiswa
    def tambahData(self):
        #Mengambil Text inputan
        Id = str(self.Id.text())
        Judul = str(self.Judul.text())
        Tahun = str(self.Tahun.text())
        Genre = str(self.Genre.text())
        Review = str(self.Review.toPlainText())
        Rating = str(self.Rating.text())
        #Mendefinisikan Query
        query = QtSql.QSqlQuery() 
        #Menjalankan Perintah Sql
        query.prepare("INSERT INTO listfilm VALUES ('" + Id + "','" + Judul + "', '" + Tahun + "', '" + Genre + "', '" + Review + "', '" + Rating + "')")
        #Mengecek apakah query berjalan dengan baik
        if query.exec_():
            self.Id.setText("")
            self.Judul.setText("")
            self.Tahun.setText("")
            self.Genre.setText("")
            self.Review.setText("")
            self.Rating.setText("")
            #Menampilkan Data
            self.tampilData()
        else:
            #Apabila error akan menampilkan errornya ke dalam terminal
            print("Insert Error: ", query.lastError().text())
        
    #Fungsi Filter Data
    def filterData(self):
        #Membuat Model
        model = QSqlQueryModel()
        #Mengambil Inputan filter
        filter_search = str(self.Cari.text())
        sql = "SELECT * FROM listfilm WHERE id LIKE '%"+str(filter_search)+"%' OR judul LIKE '%"+str(filter_search)+"%' OR tahun_rilis LIKE '%"+str(filter_search)+"%' OR genre LIKE '%"+str(filter_search)+"%'"
        self.Cari.setText("")
        #Mengeksekusi Model Query
        model.setQuery(sql)
        #Mengeset Data Model Ke table view
        self.tableview.setModel(model)
        #mengembalikan nilai table view
        return self.tableview

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
    ex.setWindowTitle("Database Sqlite in Pyqt5")
    #menampilan isi dari variabel ex
    ex.show()
    #membuat system exit
    sys.exit(app.exec_())