def k () :
    def add(x, y):
        return x + y


    def subtract (x, y):
        return x - y


    def multiplay (x, y):
        return x * y

    def devide (x, y):
        return x / y


    print("Pilih Oprasi")
    print("1.Jumlah")
    print("2.Kurang")
    print("3.Kali")
    print("4.Bagi")



    choice = input("Masukkan piliha 1/2/3/4 :")
    num1 = int(input("Masukan bilangan pertama:"))
    num2 = int(input("Masukan bilangan kedua:"))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1,num2))
        pilih()

    elif choice == '2' :
        print(num1, "-", num2, "=", subtract(num1,num2))
        pilih()
        
    elif choice == '3':
        print(num1, "*", num2, "=", multiplay(num1,num2))
        pilih()
        
    elif choice == '4':
        print(num1, "/", num2, "=", devide(num1,num2))
        pilih()
        
    else:
        print("Input salah")
        pilih()
        
def pilih():
     pilih = input("\t\nKe menu awal:")
     if pilih == 'y':
         k()
     else :
         exit
    
    
               
        
