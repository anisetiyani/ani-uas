def Penilaian() :

    from texttable import Texttable
    table = Texttable ()
    jawab = "y"
    no = 0
    nama = []
    nim = []
    nilai_tugas = []
    nilai_uts = []
    nilai_uas = []

    while (jawab =="y") :
        nama.append(input("Masukkan Nama : "))
        nim.append(input("Masukkan Nim : "))
        nilai_tugas.append(input("Nilai Tugas : "))
        nilai_uts.append(input("Nilai Uts : "))
        nilai_uas.append(input("Nilai Uas : "))
        jawab = input("Tambah data (y/t)?")
        no +=1
    
    for i in range (no) :
        tugas = int(nilai_tugas[i])
        uts = int(nilai_uts[i])
        uas = int(nilai_uas[i])
        akhir = int(tugas*30/100)+(uts*35/100)+(uas*35/100)
        table.set_cols_dtype(['i','t','t','t','t','t','t'])
        table.add_rows([['No','Nama','Nim','Tugas','Uts','Uas','Akhir'],[i+1,nama[i],nim[i],nilai_tugas[i],nilai_uts[i],nilai_uas[i],akhir]])

    print (table.draw())

