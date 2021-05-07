ulang = "ya"
while ulang == "ya" :
    pilih = input("Input data Trunk Interface baru :")
    if pilih == "yes" :
        Interface = input("Masukan Hostname Switch : ")
        file = open("db.interface.txt",'a')
        file.write("\n"+"Masukan Hostname Switch :" + Interface)
        Interface = input("Masukan nama interface :")
        file = open("db.interface.txt",'a')
        file.write("\n"+"Masukan nama interface :" + Interface)
    else :
        file = open("db.interface.txt",'r')
        print(file.read())
        break ;