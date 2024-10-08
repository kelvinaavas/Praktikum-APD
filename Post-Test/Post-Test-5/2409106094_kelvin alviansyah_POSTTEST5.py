akun = []
while True:
    print("                ")
    print("               😍 halo selamat datang di catatan bias ke sayangan mu 😍")
    print("                ")
    print("                   Silakan pilih buat profil jika belum memiliki akun")
    print("                ")
    print("buat profil")
    print("masuk")

    print("                ")
    print("♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥")
    print("                ")
    
    pilihan = input("😄 silahkan pilih dengan menuliskan kembali kata yang anda pilih 😄 : ")
    print("                ")

    if pilihan == "buat profil":
        print("😍 silahkan buat profil dulu 😍")
        Username = input("Username: ")
        akunn = False
        for akun in akun:
            if akun[0] == Username:  
                akunn = True
                break
        if akunn:
            print("🫨 namanya sudah ada silahkan buat yang lain 🫨")
        else:
            Password = input("Password: ")
            akun.append([Username, Password, []]) 
            print("                ") 
            print(f"🥳 anda berhasil membuat akun {Username} 🥳")

    elif pilihan == "masuk":
        print("⚙️ kamu bisa login ya ⚙️")
        Username = input("Username: ")
        Password = input("Password: ")
        for akun in akun:
            if akun[0] == Username and akun[1] == Password:  
                while True:
                    print("                ")
                    print(f"Selamat datang {Username} 🥳")
                    print("silahkan pilih yang ingin anda lakukan")
                    print("1. menambah biodata bias anda")
                    print("2. lihat bias anda")
                    print("3. edit catatan")
                    print("4. Hapus catatan")
                    print("5. keluar")
                    print("                ")
                    print("♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥")
                    print("                ")

                    status = input("Pilih pilihan: ")
                    print(" ")

                    if status == "1":
                        nama = input("Nama: ")
                        nama_grub = input("Nama Grub: ")
                        tahun_debut = input("Tahun Debut: ")
                        generasi = input("Generasi: ")
                        akun[2].append([nama, nama_grub, tahun_debut, generasi])
                        print("                ")
                        print("          ✅")
                        print("catatan sudah di simpan")

                    elif status == "2":
                        for indeks, note in enumerate(akun[2]): 
                            print(f"{indeks}. Nama:{note[0]} Nama Grub:{note[1]} Tahun Debut:{note[2]} Generasi:{note[3]}")
                        if not akun[2]:
                            print("🙃 sepertinya anda belum memiliki, catatan buata dulu gih 🙃")

                    elif status == "3":
                        if not akun[2]:
                            print("                ❌")
                            print("ga ada yang bisa di ganti")
                        else:
                            edit = int(input("catatan no berapa yang ingin di ganti : ")) - 1
                            if 0 <= edit < len(akun[2]):
                                nama_baru = input("Masukkan nama yang baru: ")
                                nama_grub_baru = input("Masukkan nama grub yang baru: ")
                                tahun_debut_baru = input("Masukkan tahun debut yang baru: ")
                                generasi_baru = input("Masukkan generasi yang baru: ")
                                print("Apa kamu yakin ingin mengedit catatan ?")
                                print("Iya")
                                print("Tidak")
                                memastikan_edit = input("Pilih: ")
                                if memastikan_edit == "iya":
                                    akun[2][edit] = [nama_baru, nama_grub_baru, tahun_debut_baru, generasi_baru]  
                                    print("berhasil mengedit ✅")
                                elif memastikan_edit == "tidak":
                                    print("pengeditan di batalkan")
                                else:
                                    print("Mohon pilih '1' atau '2'")
                            else:
                                print("tidak ada catatan yang di maksud, sialahkan masukkan lagi")
                    
                    elif status == "4":
                        if not akun[2]:
                            print("tidak ada yang bisa di hapus 😤")
                        else:
                            hapus = int(input("😄 nomor berapa yang ingin dihapus: ")) - 1
                            if 0 <= hapus < len(akun[2]):
                                print(f"yakin ingin menghapus")
                                print("Iya")
                                print("Tidak")
                                memastikan_hapus = input("Pilih: ")
                                if memastikan_hapus == "iya":
                                    del akun[2][hapus]
                                    print("berhasil di hapus")
                                elif memastikan_hapus == "tidak":
                                    print("dibatalkan")
                                else:
                                    print("Mohon pilih 'iya' atau 'tidak'")
                            else:
                                print("Tidak ada nomor catatan yang kamu maksud, silahkan input ulang")
                                
                    elif status == "5":
                      print("anda sudah keluar")
                    break