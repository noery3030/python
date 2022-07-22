nama = input("Input Your Name : ")
nim = input("Input NIM \t: ")

print("............................................")
print(".Welcome to \t ", nama)
print(".Wiht Your NIM \t ", nim)
print("............................................")

print("Question No.1")
print("Diketahui sisi = 6, sebutkan Nama dan Hitunglah luas Bangun Datar Tersebut !")
persegi = input("nama bangun datar : ")

s1 = float(input("sisi : "))
s2 = float(input("sisi : "))

hasil = s1 * s2 

print("Bangun datar tersebut adalah ", persegi, " dan luas bangun datar tersebut adalah " , hasil ,"\n" )
# soal no 2
print("Question No.2")
print("Diketahui alas = 7, tinggi = 8 sebutkan Nama dan Hitunglah luas Bangun Datar Tersebut !")
segitiga = input("nama bangun datar : ")

a = float(input("Alas : "))
t = float(input("Tinggi : "))

hasil_segitiga = 0.5*a*t

print("Bangun datar tersebut adalah ", segitiga , "dan luas bangun datar tersebut adalah" , hasil_segitiga,"\n")
# soal no 3
print("Question No.3")
print("Diketahui panjang = 4, lebar = 9 sebutkan nama dan hitunglah Bangun Datar Tersebut !")
persegi_panjang = input("nama bangun datar : ")

p = float(input("Panjang : "))
l = float(input("Lebar : "))

hasil_persegiPanjang = p * l 

print("Bangun datar tersebut adalah" , persegi_panjang, "dan luas bangun datar tersebut adalah" , hasil_persegiPanjang,"\n")
# soal no 4 lingkaran
print("Question No.4")
print("Diketahui jari-jari = 56, sebutkan Nama da Hitunglah luas Bangun Datar Tersebut !")
lingkaran = input("nama bangun datar : ")

phi = float(input("phi: "))
r = float(input("r : "))
l = phi*r*r

print("Bangun datar tersebut adalah" ,lingkaran, "dan luas bangun datar tersebut adalah" ,l,"\n")
#soal no 5

print("Question No.5")
print("Diketahui diagonal I = 4, diagonal II = 8 sebutkan Nama da Hitunglah luas Bangun Datar Tersebut !")
belah_ketupat = input("nama bangun datar : ")

d1 = float(input("Diagonal I: "))
d2= float(input("Diagobal II : "))
ktpt = 0.5*(d1 * d2) 

print("Bangun datar tersebut adalah" ,belah_ketupat, "dan luas bangun datar tersebut adalah" ,ktpt,"\n")


# soal no 6 
print("Question No.6")
print("Diketahui sisi AB dan CD sejajar , sisi AB = 6, sisi CD = 8,  tinggi = 3 sebutkan nama  dan Hitunglah luas Bangun Datar Tersebut !")
trapesium = input("nama bangun datar : ")

ab= float(input("sisi AB: "))
cd = float(input("sisi CD : "))
t = float(input("tinggi :"))
tra = (ab+cd)*t/2

print("Bangun datar tersebut adalah ", trapesium ,"dan luas bangun datar tersebut adalah" ,tra,"\n")

#soal no 7
print("Question No.7")
print("Diketahui sebuah Jajar Genjang dengan alas = 9, tinggi = 7 Hitunglah luas Bangun Datar Tersebut !")

alas = float(input("Alas : "))
tinggi = float(input("Tinggi : "))
hsl = alas * tinggi

print("Luas Jajar Genjang  adalah" ,hsl,"\n")

print("............................................")
print(".\t \t \t \t \t   .")
print(".  'Thank You Very Much For You Attention' .")
print(".\t \t \t \t \t   .")
print("............................................")