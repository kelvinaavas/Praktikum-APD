akun = {}
status_login = False
current_user = None

def tampilkan_menu():
    print("                ")
    print("😍 halo selamat datang di catatan bias kesayanganmu 😍")
    print("                ")
    print("Silakan pilih buat profil jika belum memiliki akun")
    print("buat profil")
    print("masuk")
    print("                ")
    print("♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎")
    print("                ")

def buat_profil(akun):
    global current_user  
    print("😍 silahkan buat profil dulu 😍")
    Username = input("Username: ")
    if Username in akun:
        print("🫨 Username sudah ada, silahkan buat yang lain 🫨")
    else:
        Password = input("Password: ")
        akun[Username] = {"Password": Password, "Catatan": []}
        current_user = Username
        print(f"🥳 Anda berhasil membuat akun {Username} 🥳")

def masuk():
    global status_login, current_user
    print("⚙️ Kamu bisa login ya ⚙️")
    Username = input("Username: ")
    Password = input("Password: ")
    
    if Username in akun and akun[Username]["Password"] == Password:
        current_user = Username
        status_login = True
        print(f"Selamat datang {Username} 🥳")
    else:
        print("Username atau Password salah")

def tambah_catatan(Username):
    nama = input("Nama: ")
    nama_grub = input("Nama Grub: ")
    tahun_debut = input("Tahun Debut: ")
    generasi = input("Generasi: ")
    
    akun[Username]["Catatan"].append({
        "Nama": nama,
        "Nama Grub": nama_grub,
        "Tahun Debut": tahun_debut,
        "Generasi": generasi
    })
    print("✅ Catatan sudah disimpan")

def lihat_catatan():
    if akun[current_user]["Catatan"]:
        for indeks, note in enumerate(akun[current_user]["Catatan"]):
            print(f"{indeks+1}. Nama: {note['Nama']}\n   Nama Grub: {note['Nama Grub']}\n   Tahun Debut: {note['Tahun Debut']}\n   Generasi: {note['Generasi']}\n")
    else:
        print("🙃 sepertinya anda belum memiliki catatan, buat dulu gih 🙃")

def edit_catatan(Username):
    if not akun[Username]["Catatan"]:
        print("                ❌")
        print("Tidak ada yang bisa diganti")
    else:
        edit = int(input("Catatan nomor berapa yang ingin diganti: ")) - 1
        if 0 <= edit < len(akun[Username]["Catatan"]):
            nama_baru = input("Masukkan nama yang baru: ")
            nama_grub_baru = input("Masukkan nama grub yang baru: ")
            tahun_debut_baru = input("Masukkan tahun debut yang baru: ")
            generasi_baru = input("Masukkan generasi yang baru: ")
            print("Apa kamu yakin ingin mengedit catatan?")
            memastikan_edit = input("Iya/Tidak: ")
            if memastikan_edit == "iya":
                akun[Username]["Catatan"][edit] = {
                    "Nama": nama_baru,
                    "Nama Grub": nama_grub_baru,
                    "Tahun Debut": tahun_debut_baru,
                    "Generasi": generasi_baru
                }
                print("Berhasil mengedit ✅")
            else:
                print("Pengeditan dibatalkan")
        else:
            print("Tidak ada catatan yang dimaksud, silakan masukkan lagi")

while True:
    tampilkan_menu()
    pilihan = input("😄 silahkan pilih dengan menuliskan kembali kata yang anda pilih 😄 : ")
    print("                ")

    if pilihan == "buat profil":
        buat_profil(akun)

    elif pilihan == "masuk":
        masuk()
        while status_login:
            print("silahkan pilih yang ingin anda lakukan")
            print("1. menambah biodata bias anda")
            print("2. lihat bias anda")
            print("3. edit catatan")
            print("4. Hapus catatan")
            print("5. keluar")
            print("                ")

            status = input("Pilih pilihan: ")
            print(" ")

            if status == "1":
                tambah_catatan(current_user)

            elif status == "2":
                lihat_catatan()

            elif status == "3":
                edit_catatan(current_user)

            elif status == "4":
                if not akun[current_user]["Catatan"]:
                    print("Tidak ada yang bisa dihapus 😤")
                else:
                    hapus = int(input("😄 Nomor berapa yang ingin dihapus: ")) - 1
                    if 0 <= hapus < len(akun[current_user]["Catatan"]):
                        memastikan_hapus = input("Yakin ingin menghapus? Iya/Tidak: ")
                        if memastikan_hapus == "iya":
                            del akun[current_user]["Catatan"][hapus]
                            print("Berhasil dihapus")
                        else:
                            print("Dibatalkan")
                    else:
                        print("Tidak ada nomor catatan yang dimaksud, silakan input ulang")

            elif status == "5":
                status_login = False
                print("Anda sudah keluar")
