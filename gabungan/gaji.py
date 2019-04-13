def Gaji() :
    from texttable import Texttable

    table = Texttable ()
    jawab = "y"
    no = 0
    nama =[]
    jabatan = []
    gaji = []
    jawab = "y"

    while (jawab == 'y') :
        nama.append(input("\nmasukan nama: "))
        jab = input("\njabatan: ")
        jabatan.append(jab)
        if  (jab == 'programer' ):
            (jabatan == 'programer')
            gaji.append(3000000)
            jawab = input(" \n tambah lagi? ")
            no+=1
        
        elif(jab == 'direkture' ):
            (jabatan == 'direkture')
            gaji.append(5000000)
            jawab = input(" \n tambah lagi? ")
            no+=1

        elif(jab == 'suster' ):
            (jabatan == 'suster')
            gaji.append(2000000)
            jawab = input("\n tambah lagi? ")
            no+=1
            
        else:
            break
            

    for i in range (no) :
       table.add_rows([['No','Nama','Jab','Gaji'],[i+1, nama[i],jabatan[i],gaji[i]]])                      
    print (table.draw())



   
