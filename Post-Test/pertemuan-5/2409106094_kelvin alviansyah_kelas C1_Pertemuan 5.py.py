# nama = ["shandy",108,True,3.96]
# matkul = ["apd", "web","jarkon"]
# print (nama)
# print (matkul)
# print (nama[1])
# print (matkul[2])
# print (matkul[-2]) #jika - akan mulai dari belakang

# nama = ["shandy",108,True,3.96]
# matkul = ["apd", 
#           "web",
#           "jarkon",
#           "basdat",
#           "struktur",
#           "pti",
#           "kalkulus",
#           "probas"]
# bisa di susun kebawah utuk membuat list\
# print (matkul[-1])

# nama = ["shandy",108,True
#         ["yuyun",145]3.96,
#         [123,"ALVITO",False,3.66],
#         "rehan"]
# print(nama[4][-2])
#bisa membuat list di dalam list

# makanan = ["bakso","sate","soto","nasi goreng","mie ayam","ayam bakar","cumi bakar"]
# print("sebelum: ")
# print(makanan)

# makanan.append("nasi goreng") #untuk menammba

# print("sesudah: ")
# makanan.clear()   #untuk menghapus semuanya
# print(makanan)

# del makanan[5] #untuk menghapus elemen

# data = makanan.pop(5) #ingin menghapus tapi tidak terhapus sepenuhnya
# print(makanan)
# print(data)

# makanan.insert(2,"nasi goreng") #untuk merubah elemen

# makanan[0] = "nasi goreng"
# makanan[0] = ["ayam","bebek"]

# print(makanan)

# makanan = ["bakso","soto","sate","ikan","bebek"]
# for i in makanan :
#     print (i, end=" ") #end=" ") untuk horizontal

# makanan = ["bakso","soto","sate","ikan","bebek"],["teh","kopi","air"]
# for i in makanan :
#     for j in i :
#         print(j, end=" ")

# makanan = ["ayam","ikam",["bakso","soto","sate","ikan","bebek"],
        #    ["teh","kopi","air"]]

# for i in makanan :
#     if isinstance(i, list):
#        for j in i :
#           print(j)

akuns = [1]

while True:
    print("Halo! selamat datang di aplikasi Catatan")
    print("Silakan pilih 'Daftar akun' jika belum buat akun, dan jika sudah memiliki akun silahkan 'Login'")
    print("1. Daftar akun")
    print("2. Login")
    print("3. Exit")
    print("---------------------------")
    opsi = input("Pilih opsi: ")
    print(" ")

    if opsi == "1":
        print("Halo Pengguna baru! Ayo buat akun dulu")
        Username = input ("Username: ")
        akuna = False
        for akun in akuns:
            if akun[0] == Username: # Memeriksa apakah username sudah ada
                    akuna = True
                    break
            if akuna:
                 print("Nama Sudah Terpakai Untuk Registrasi Stlahkan Coba Lagi")
            else:
                 Password = input("Password: ")
                 akuns.append([Username, Password]) # Simpan username, password, dan catatan (sebagai list kosong)
                 print(f"Akun Anda berhasil terdaftar dengan ID: {Username}")

                 