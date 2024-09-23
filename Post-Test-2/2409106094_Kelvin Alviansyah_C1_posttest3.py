nama = (input("masukan nama anda: "))
hari = (input("di hari apa anda ingin membeli tiket: "))
uang = int(input("masukkan uang anda: "))

if hari == "senin":
    if uang >= 40000:
        print("anda bisa membeli tiket di hari tersebut dangan harga Rp 40000")
    else:
        print("uang yang anda masukan tidak cukup untuk membeli tiket di hari tersebut")
else:
    if hari == "selasa":
        if uang >= 40000:
            print("anda bisa membeli tiket di hari tersebut dangan harga Rp 40000")
        else:
            print("uang yang anda masukan tidak cukup untuk membeli tiket di hari tersebut")
    else:
        if hari == "rabu":
            if uang >= 40000:
                print("anda bisa membeli tiket di hari tersebut dangan harga Rp 40000")
            else:
                print("uang yang anda masukan tidak cukup untuk membeli tiket di hari tersebut")
        else:
            if hari == "kamis":
                if uang >= 40000:
                    print("anda bisa membeli tiket di hari tersebut dangan harga Rp 40000")
                else:
                    print("uang yang anda masukan tidak cukup untuk membeli tiket di hari tersebut")
            else:
                if hari == "jumat":
                    if uang >= 45000:
                        print("anda bisa membeli tiket di hari tersebut dangan harga Rp 45000")
                    else:
                        print("uang yang anda masukan tidak cukup untuk membeli tiket di hari tersebut")
                else:
                    if hari == "sabtu":
                        if uang >= 55000:
                            print("anda bisa membeli tiket di hari tersebut dangan harga Rp 55000")
                        else:
                            print("uang yang anda masukan tidak cukup untuk membeli tiket di hari tersebut")
                    else:
                        if hari == "minggu":
                            if uang >= 60000:
                                print("anda bisa membeli tiket di hari tersebut dangan harga Rp 60000")
                            else:
                                print("uang yang anda masukan tidak cukup untuk membeli tiket di hari tersebut")
