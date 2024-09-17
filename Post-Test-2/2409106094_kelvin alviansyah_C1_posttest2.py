nama = input("masukan nama lengkap anda: ")
nim = input("masukkan nim: ")

print(F"halo {nama} dengan nim {nim} gula yang tersedia dengan harga 21.000/KL dari merek gulaku, manis kita, gunung madu")
HargaGula = float(input("masukkan harga gula perkilo yang ingin di beli untuk melihat diskon nya: "))

diskon_gulaku = HargaGula * 0.07
gulaku_setelah_diskon = HargaGula - diskon_gulaku

print("jika memilih merek gulaku mendapat 7% diskon")
print(f"dan harga setelah diskon adalah Rp{gulaku_setelah_diskon}")

diskon_manis_kita = HargaGula * 0.11
manis_kita_setelah_diskon = HargaGula - diskon_manis_kita

print("jika memilih merek manis kita mendapat 11% diskon")
print(f"dan harga setelah diskon Rp{manis_kita_setelah_diskon}")

diskon_gunung_madu = HargaGula * 0.13
gunung_madu_setelah_diskon = HargaGula - diskon_gunung_madu

print("jika memilih merek gunung madu mendapat 13% diskon")
print(f"dan harga setelah diskon Rp{gulaku_setelah_diskon}")
