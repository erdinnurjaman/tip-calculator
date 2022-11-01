# Project day - 2 : Tip Calculator

# Print judul atau nama project
print('Welcome to tip calculator.')

# Buat fungsi inputan berupa berapa total biaya dalam dollar dan simpan inputan tersebut ke dalam variabel "total_bill"
total_bill = input('What was the total bill? \n$')

# Buat fungsi inputan berupa berapa persen tip yang akan kamu berikan kepada si pelayan dan simpan inputan tersebut ke dalam variable "percentage"
percentage = input('What percentage tip would you like to give? \n')

# Buat fungsi inputan berupa berapa jumlah orang yang akan membayar total biaya tersebut dan simpan inputan tersebut ke dalam variable "split"
split = input('How many people to split the bill? \n')

# Ubah tipe data di variable "total_bill" menjadi float dan simpan di variable baru bernama "total_bill_float"
total_bill_float = float(total_bill)

# Ubah tipe data di variable "percentage" menjadi integer dan simpan di variable baru bernama "percentage_int"
percentage_int = int(percentage)

# ubah tipe data di variable "split" menjadi integer dan simpan di variable baru bernama "split_int"
split_int = int(split)

# Buat operasi matematika untuk menghitung persentase tip dengan menggunakan variable "total_bill_float" dan "percentage_int"
percent = total_bill_float * percentage_int / 100

# Buat operasi matematika untuk menghitung jumlah total biaya yang harus dibayar setelah ditambah dengan biaya tip dan bagi total biaya tersebut dengan berapa jumlah orang yang akan membayar/patungan
# Batasi angka dibelakang koma nya dengan menambahkan parameter di belakang operasi matematikanya
total_bill_after_split = round((total_bill_float + percent) / split_int, 2)

# Print variable "total_biaya_after_split" untuk mrngetahui berapa jumlah uang yang harus dibayarkan oleh masing-masing orang dan tambahkan string keterangannya
print(f'Each person should pay: \n${total_bill_after_split}')

# Done !
