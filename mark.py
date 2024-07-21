
try:
	ch = input("Mahu bewarna(y/n)?")
	if ch == "y":
		from colorama import Fore, Style
		print("CODE: colorama dipasang")
	else:
		print("Hitam putih")
except ModuleNotFoundError:
	exit("CODE: colorama tidak dipasang")

try:
	class color:
	   	r = Fore.RED
	   	y = Fore.YELLOW
	   	b = Fore.BLUE
	   	g = Fore.GREEN
	   	res = Style.RESET_ALL
except Exception:
	print('CODE: Class tidak ditetapkan')
print("*"*40)
# Minta bilangan bahagian soalan
bilangan_bahagian = int(input("Masukkan bilangan bahagian soalan: "))

# Senarai untuk menyimpan jumlah soalan dalam setiap bahagian dan markahnya
markah_bahagian = []

# Kira markah setiap bahagian
for i in range(bilangan_bahagian):
    print(f"\nBahagian {i+1}:")
    markah_soalan = []
    while True:
        markah = input("Masukkan markah soalan (biarkan kosong jika siap): ")
        if markah.lower() == '':
            break
        try:
            markah = float(markah)
            markah_soalan.append(markah)
        except ValueError:
            print("Sila masukkan nombor yang sah!")
    
    markah_bahagian.append(markah_soalan)

# Paparkan bilangan bahagian dan bilangan soalan dalam setiap bahagian
print("\nRingkasan:")
for i, markah_soalan in enumerate(markah_bahagian, 1):
    print(f"Bahagian {i}: {len(markah_soalan)} soalan")

# Paparkan jumlah markah setiap bahagian
jumlah_markah = 0
for i, markah_soalan in enumerate(markah_bahagian, 1):
    jumlah_bahagian = sum(markah_soalan)
    print(f"Jumlah markah Bahagian {i}: {color.g}{int(jumlah_bahagian)}{color.res}")
    jumlah_markah += jumlah_bahagian

# Paparkan jumlah keseluruhan markah
print(f"\nJumlah keseluruhan markah: {color.y}{int(jumlah_markah)}{color.res}")
print("*"*40)
