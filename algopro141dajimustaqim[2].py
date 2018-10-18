####praktikum 6
####dibuat oleh aji mustaqim L200180141
####kegiatan 1.identitas
##Nama = "Aji mustaqim"
##Nama_panggilan = "Aji"
##Nama_bapak = "Suparsono"
##Nama_ibu = "Sugiyatmi"
##Alamat = "Sanggrahan tunggulrejo jumantono karanganyar"
##Ttl = "18 oktober 2000"
##Hobi = "Memancing"
##Prodi = "informatika"
##Kuliah = "UMS"
##Fakultas = "fki"

####kegiatan 2. akun
##Nama = "Aji mustaqim"
##Ttl = "18 oktober 2000"
##Nama_singkat = Nama[:3]
##Username = Nama[:3] + Ttl[:2]
##Password = Nama[:3] + Ttl[11:]

####kegiatan 3. operator
##Nama = "Aji mustaqim"
##Nim = "L200180141"
##X = "1" + Nim[7:] #angka 1 + 3 digit nim terakhir
##a = int(X) #konversi string ke integer
##b = len(Nama) #jumlah indeks yang ada di nama
##type(a) # a itu data integer
##type(b) #b itu juga integer
##a / b # a di bagi dengan b jawabanya 95 (dalam bil float)
##a // b # a dibagi dengan b jawabanya juga 95 (dalam bil yang dibulatkan)
##10 * (a - 999) # 10 dikali a dikurangi 999 jawabannya 1420
##b ** 2 #b dipangkatkan 2 jawabanya 144
##a % b # a dibagi b tapi jawabnya sisa pembagian a dibagi b
##c = 12.5 #menyimpan data 12.5 di var c
##type(c) # c itu berarti data float
##a / c # a di bagi c jawabannya 91.28 (dalam data float)
##a // c # a dibagi c jawabannya 91 (dalam bil yg dibulatkan)
##a % c # sisa pembagian a dengan c adalah 3.5 (float)
##c > b # apakah c lebih besar dari b jawabannya benar
##type(c > b) # tipe datanya boolean
##a > b and b > c # a lebih besar dari b dan b lebih besar dari c adalah salah
##a > 1100 or b < 10 # a lebih besar dari 1100 atau b kurang dari 10 adalah benar

##kegiatan 4. tipe data
Nama = "Aji mustaqim"
Nim = 141
Tinggi = 1.6
Berat = 42
Tahunlahir = 2000
Aku = (Tahunlahir, Berat, Tinggi, Nim, Nama) #kumpulan data tuple
Data = [Tahunlahir, Berat, Tinggi, Nim, Nama] #kumpulan data list
type(Aku) #tipenya tuple
Aku[0] #indeks pertama adalah tahunlahir
a = Nim % 4; Aku[a] #sisa pembagian nim dibagi 4 dan aku a
type(Aku[a]) # tipenya integer
Aku[a:4] # 42, 1.6, 141
type(Aku[4]) #tipenya string
Aku[0] = "ok" #tidak tahu
type(Data) #tipenya list
type(Data[4]) #tipenya string
Data[4][5] # u
Data[4][a:6] # ji mu
Data[0] = "ok"; Data #ok, 42,1.6, 141, aji mustaqim
Data[-a] #aji mustaqim
range(a) # rangenya [0]
