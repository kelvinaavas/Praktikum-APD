print("masukkan username :")
username = input()
pengulangan = 0
while pengulangan < 3:
    print("masukkan pasword anda :")
    pasword = int(input())
    if pasword == 94:
        print("BERHASIL MASUK")
        print("silahkan masukkan nama anda: ")
        nama = input()
        print("di hari apa anda ingin membeli tiket: ")
        hari = input()
        print("masukkan uang anda: ")
        uang = int(input())
        if hari == "senin":
            if uang >= 40000:
                print("anda bisa membeli tiket di hari tersebut dangan harga Rp 40000")
                break
            else:
                print("uang yang anda masukan tidak cukup untuk membeli tiket di hari tersebut")
                break
        else:
            if hari == "selasa":
                if uang >= 40000:
                    print("anda bisa membeli tiket di hari tersebut dangan harga Rp 40000")
                    break
                else:
                    print("uang yang anda masukan tidak cukup untuk membeli tiket di hari tersebut")
                    break
            else:
                if hari == "rabu":
                    if uang >= 40000:
                        print("anda bisa membeli tiket di hari tersebut dangan harga Rp 40000")
                        break
                    else:
                        print("uang yang anda masukan tidak cukup untuk membeli tiket di hari tersebut")
                        break
                else:
                    if hari == "kamis":
                        if uang >= 40000:
                            print("anda bisa membeli tiket di hari tersebut dangan harga Rp 40000")
                            break
                        else:
                            print("uang yang anda masukan tidak cukup untuk membeli tiket di hari tersebut")
                            break
                    else:
                        if hari == "jumat":
                            if uang >= 45000:
                                print("anda bisa membeli tiket di hari tersebut dangan harga Rp 45000")
                                break
                            else:
                                print("uang yang anda masukan tidak cukup untuk membeli tiket di hari tersebut")
                                break
                        else:
                            if hari == "sabtu":
                                if uang >= 55000:
                                    print("anda bisa membeli tiket di hari tersebut dangan harga Rp 55000")
                                    break
                                else:
                                    print("uang yang anda masukan tidak cukup untuk membeli tiket di hari tersebut")
                            else:
                                if hari == "minggu":
                                    if uang >= 60000:
                                        print("anda bisa membeli tiket di hari tersebut dangan harga Rp 60000")
                                        break
                                    else:
                                        print("uang yang anda masukan tidak cukup untuk membeli tiket di hari tersebut")
                                        break
                                else:
                                    print("tolong tulis hari dengan benar !!!")
                                    break
    else:
        pengulangan = pengulangan + 1
        print("maaf salah silahkan masukkan pasword lagi : ")
        print(pengulangan)