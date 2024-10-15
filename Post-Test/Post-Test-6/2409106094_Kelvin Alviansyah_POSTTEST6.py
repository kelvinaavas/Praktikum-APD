akun = {}

while True:
    print("                ")
    print("😍 halo selamat datang di catatan bias kesayanganmu 😍")
    print("                ")
    print("Silakan pilih buat profil jika belum memiliki akun")
    print("buat profil")
    print("masuk")
    print("                ")
    print("♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎")
    print("                ")

    pilihan = input("😄 silahkan pilih dengan menuliskan kembali kata yang anda pilih 😄 : ")
    print("                ")

    if pilihan == "buat profil":
        print("😍 silahkan buat profil dulu 😍")
        Username = input("Username: ")
        if Username in akun:
            print("🫨 Username sudah ada, silahkan buat yang lain 🫨")
        else:
            Password = input("Password: ")
            akun[Username] = {"Password": Password, "Catatan": []}
            print(f"🥳 Anda berhasil membuat akun {Username} 🥳")

    elif pilihan == "masuk":
        print("⚙️ Kamu bisa login ya ⚙️")
        Username = input("Username: ")
        Password = input("Password: ")

        if Username in akun and akun[Username]["Password"] == Password:
            while True:
                print(f"Selamat datang {Username} 🥳")
                print("silahkan pilih yang ingin anda lakukan")
                print("1. menambah biodata bias anda")
                print("2. lihat bias anda")
                print("3. edit catatan")
                print("4. Hapus catatan")
                print("5. keluar")
                print("                ")
                print("♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎")
                print("                ")

                status = input("Pilih pilihan: ")
                print(" ")

                if status == "1":
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
                    print("          ✅")
                    print("Catatan sudah disimpan")

                elif status == "2":
                    if akun[Username]["Catatan"]:
                        for indeks, note in enumerate(akun[Username]["Catatan"]):
                            print(f"{indeks+1}. Nama: {note['Nama']}   Nama Grub: {note['Nama Grub']}   Tahun Debut: {note['Tahun Debut']}   Generasi: {note['Generasi']}")
                    else:
                        print("🙃 sepertinya anda belum memiliki catatan, buat dulu gih 🙃")

                elif status == "3":
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
                            memastikan_edit = input("Iya/Tidak: ").lower()
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

                elif status == "4":
                    if not akun[Username]["Catatan"]:
                        print("Tidak ada yang bisa dihapus 😤")
                    else:
                        hapus = int(input("😄 Nomor berapa yang ingin dihapus: ")) - 1
                        if 0 <= hapus < len(akun[Username]["Catatan"]):
                            memastikan_hapus = input("Yakin ingin menghapus? Iya/Tidak: ").lower()
                            if memastikan_hapus == "iya":
                                del akun[Username]["Catatan"][hapus]
                                print("Berhasil dihapus")
                            else:
                                print("Dibatalkan")
                        else:
                            print("Tidak ada nomor catatan yang dimaksud, silakan input ulang")

                elif status == "5":
                    print("Anda sudah keluar")
                    break
        else:
            print("Username atau Password salah")
