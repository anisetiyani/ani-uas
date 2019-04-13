def pembayaran () :
        
        print("...........PROGRAM PEMBAYARAN MAHASISWA...........")
        print("1. PROGRAM PEMBAYARAN UTS")
        print("2. PROGRAM PEMBAYARAN UAS")
        ani = input ('Mau bayaran y atau t ?')
        if ani == 'y' :
                print('YES')
                pembayaran()
        elif ani == 't':
                    print (' Eror ')
                    exit
        elif ani == '' :
                    exit
        else :
                    print('ANDA SALAH')
                    exit

def pembayaran() :       
    pilihan = input("\nMASUKAN PILIHAN PEMBAYARAN : ")
    if   pilihan == '1' :
        uts() 
    elif pilihan == '2' :
        uas()
    else :
        exit()
   
        
        
def uts():
        from texttable import Texttable
        table = Texttable()
        jawab = "y"

        no = 0
        nama =[]
        nim = []
        kelas = []
        jum_matkul_uts_bayar = []
        bulan_bayar = []
        bayar_seminar = []
        bayar_kas = []
        print("PEMBAYARAN UTS")
        
        while(jawab == "y") :
            nama.append(input(" Nama  : "))
            nim.append(input(" NIM    : "))
            kelas.append(input(" Kelas : "))
            jum_matkul_uts_bayar.append(input(" ............MATA KULIAH YANG AKAN DI BAYAR UTS............. : "))
            bulan_bayar.append(input("......................JUMLAH BULAN BIAYA YANG AKAN DI BAYAR.......... : "))
            
            pilih = input("Apakah ingin bayar kas (y/t) ?  ")
            if pilih == 'y' :
                    bayar_kas = 20000
            else :
                    bayar_kas = 0
                    
            pilih = input("Apakah ingin bayar seminar (y/t) ?  ")
            if pilih == 'y' :
                    bayar_seminar = 100000
            else :
                    bayar_seminar = 0
                
            jawab = input("Ingin Bayar Lagi (y/t) ? ")
            no += 1
        
        for i in range (no):
            bayar_uts = int(jum_matkul_uts_bayar[i])*90000
            bayar_spp = int(bulan_bayar[i])*500000
            admin = int(5000)
            akhir = bayar_uts + bayar_spp + bayar_seminar+ bayar_kas + admin
            table.set_cols_dtype(['i','t','t','t','t','t','t','t','t','t'])
            table.set_cols_align(['i','c','c','c','c','c','c','c','c','c',])
            table.add_rows([['No','NAMA',' NIM ','KELAS','BIAYA UTS','BIAYA SPP','SEMINAR','KAS','ADMIN','TOTAL'],
                        [i+1, nama[i],nim[i],kelas[i],bayar_uts,bayar_spp,bayar_seminar,bayar_kas,admin,akhir]])
        print (table.draw())

        ani()

def uas():
        from texttable import Texttable
        table = Texttable()
        jawab = "y"
        no = 0
        nama =[]
        nim = []
        kelas = []
        jum_matkul_uas_bayar = []
        bulan_bayar = []
        bayar_seminar = []
        bayar_kas = []
        print("KATEGORI PEMBAYARAN : UAS")
        while(jawab == "y") :
            nama.append(input(" NAMA ANDA  : "))
            nim.append(input(" NIM ANDA    : "))
            kelas.append(input("  KELAS ANDA  : "))
            jum_matkul_uas_bayar.append(input(" ...............MATA KULIAH YANG AKAN DI BAYAR UAS............ : "))
            bulan_bayar.append(input(".........................JUMLAH BULAN BIAYA YANG AKAN DIBAYAR.......... : "))
            pilih = input("Apakah ingin bayar kas (y/t) ?  ")
            if pilih == 'y' :
                    bayar_kas = 20000
            else :
                    bayar_kas = 0
                    
            pilih = input("Apakah ingin bayar seminar (y/t) ?  ")
            if pilih == 'y' :
                    bayar_seminar = 100000
            else :
                    bayar_seminar = 0
                
            
            jawab = input("Ingin Bayar Lagi (y/t) ? ")
            no += 1
        
        for i in range (no):
            bayar_uas = int(jum_matkul_uas_bayar[i])*50000
            bayar_spp = int(bulan_bayar[i])*500000
            admin = int("5000")
            akhir = bayar_uas + bayar_spp + bayar_seminar + bayar_kas + admin
            table.set_cols_dtype(['i','t','t','t','t','t','t','t','t','t'])
            table.set_cols_align(['i','c','c','c','c','c','c','c','c','c',])
            table.add_rows([['No','NAMA','NIM','KELAS','BIAYA UAS','BIAYA SPP','SEMINAR','KAS','ADMIN','TOTAL'],
                        [i+1, nama[i],nim[i],kelas[i],bayar_uas,bayar_spp,bayar_seminar,bayar_kas,admin,akhir]])
        print (table.draw())
        
def ani():
    tanya = input("\nKEMBALI LAGI KE HALAMAN AWAL (y/t)?")
    
    if tanya == "y":
        print("~~~~~~~~PROGRAM PEMBAYARAN MAHASISWA~~~~~~~~~")
        print("1. PROGRAM PEMBAYARAN UTS")
        print("2. PROGRAM PEMBAYARAN UAS")
        pembayaran()
    else :
            print("\n\tSALAHHHHHHHHHHHHH...........!!!")
            exit
            



pembayaran()
