#Example 1
import tkinter
import tkinter.messagebox
top = tkinter.Tk()
def halloCallBack():
    tkinter.messagebox.showinfo("Hello Python!", "Hello Bitches")
B = tkinter.Button(top, text ="Hello", command = halloCallBack)
B.pack()
top.mainloop()

#Example 2
import tkinter as tk
from tkinter import messagebox

top = tk.Tk()
L1 = tk.Label(top, text="User Name")
L1.pack(side=tk.LEFT)
E1 = tk.Entry(top, bd=5)
E1.pack(side=tk.RIGHT)
top.mainloop()

#Example 3
import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
bottomframe = tk.Frame(root)
bottomframe.pack(side=tk.BOTTOM)
redbutton = tk.Button(frame, text="Red", fg="red")
redbutton.pack(side=tk.LEFT)
greenbutton = tk.Button(frame, text="Brown", fg="brown")
greenbutton.pack(side=tk.LEFT)
bluebutton = tk.Button(frame, text="Blue", fg="blue")
bluebutton.pack(side=tk.LEFT)
blackbutton = tk.Button(bottomframe, text="Black", fg="black")
blackbutton.pack(side=tk.BOTTOM)
root.mainloop()
 
#Example 4
import tkinter as tk

root = tk.Tk()
var = tk.StringVar()
label = tk.Label(root, textvariable=var, relief=tk.RAISED)
var.set("Hey!? How are you doing?")
label.pack()

root.mainloop()

#Example 5
import tkinter as tk
from tkinter import messagebox
top = tk.Tk()
Lb1 = tk.Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
Lb1.pack()
top.mainloop()

#Example 6
import tkinter as tk
from tkinter import messagebox

top = tk.Tk()
mb = tk.Menubutton(top, text="condiments", relief=tk.RAISED)
mb.grid()
mb.menu = tk.Menu(mb, tearoff=0)
mb["menu"] = mb.menu
mayoVar = tk.IntVar()
ketchVar = tk.IntVar()
mb.menu.add_checkbutton(label="mayo", variable=mayoVar)
mb.menu.add_checkbutton(label="ketchup", variable=ketchVar)

mb.pack()
top.mainloop()

#Example 7
import tkinter as tk

root = tk.Tk()

var = tk.StringVar()
label = tk.Message(root, textvariable=var, relief=tk.RAISED)

var.set("Hey!? How are you doing?")
label.pack()
root.mainloop()

#Example 8
import tkinter as tk

def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text=selection)
root = tk.Tk()
var = tk.IntVar()
R1 = tk.Radiobutton(root, text="Option 1", variable=var, value=1, command=sel)
R1.pack(anchor=tk.W)
R2 = tk.Radiobutton(root, text="Option 2", variable=var, value=2, command=sel)
R2.pack(anchor=tk.W)
R3 = tk.Radiobutton(root, text="Option 3", variable=var, value=3, command=sel)
R3.pack(anchor=tk.W)
label = tk.Label(root)
label.pack()
root.mainloop()

#Example 9
import tkinter as tk

def sel():
    selection = "Value = " + str(var.get())
    label.config(text=selection)

root = tk.Tk()
var = tk.DoubleVar()
scale = tk.Scale(root, variable=var)
scale.pack(anchor=tk.CENTER)

button = tk.Button(root, text="Get Scale Value", command=sel)
button.pack(anchor=tk.CENTER)

label = tk.Label(root)
label.pack()
root.mainloop()

#Example 10
import tkinter as tk

root = tk.Tk()
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

mylist = tk.Listbox(root, yscrollcommand=scrollbar.set)
for line in range(100):
    mylist.insert(tk.END, "This is line number " + str(line))

mylist.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=mylist.yview)

root.mainloop()

#Praktikum
import tkinter as tk 
#Import Tkinter: Mengimpor modul Tkinter untuk membuat GU

def hasil_prediksi():
    # Fungsi ini akan dipanggil ketika tombol "Hasil Prediksi" diklik. Fungsi ini akan mengubah teks pada label 
    # hasil menjadi "Prodi Pilihan: Teknologi Informasi".
    hasil_label.config(text="Prodi Pilihan: Teknologi Informasi")

# Membuat jendela utama : Membuat jendela utama aplikasi dengan judul "Aplikasi Prediksi Prodi Pilihan
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

# Label Judul : Menambahkan label judul di bagian atas jendela.
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
judul_label.grid(row=0, column=0, columnspan=2, pady=10)

# Input nilai mata pelajaran : Menggunakan loop untuk membuat 10 label dan entry untuk input nilai mata pelajaran.
mata_pelajaran_labels = []
mata_pelajaran_entries = []
for i in range(1, 11):
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {i}:")
    label.grid(row=i, column=0, padx=5, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=5, pady=5)
    
    mata_pelajaran_labels.append(label)
    mata_pelajaran_entries.append(entry)

# Button untuk hasil prediksi : Tombol ini akan memanggil fungsi hasil_prediksi saat diklik.
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.grid(row=11, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil prediksi : Label untuk menampilkan hasil prediksi, yang awalnya kosong.
hasil_label = tk.Label(root, text="", font=("Arial", 14))
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi : Memanggil mainloop() untuk menjalankan aplikasi.
root.mainloop()
