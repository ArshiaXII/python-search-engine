import tkinter as tk
from googlesearch import search

def google_arama():

    
    # Arama sonuçlarını içerecek liste
    sonuclar = []
    
    # Arama sorgusu metin kutusundan alınır
    sorgu = sorgu_entry.get()

    # Sorgu Google'da aranır ve sonuçlar listeye eklenir
    try:
        for j in search(sorgu, num_results=10):
            sonuclar.append(j)
    except Exception as e:
        sonuclar.append(str(e))

    # Sonuçlar metin kutusuna yazdırılır
    sonuc_text.delete('1.0', tk.END)
    for sonuc in sonuclar:
        sonuc_text.insert(tk.END, sonuc + '\n')

# Tkinter penceresi oluşturulur
root = tk.Tk()

# Sorgu için metin kutusu oluşturulur
sorgu_entry = tk.Entry(root, width=50)
sorgu_entry.pack()

# Arama butonu oluşturulur
arama_button = tk.Button(root, text="Ara", command=google_arama)
arama_button.pack()


# Sonuçları göstermek için metin kutusu oluşturulur
sonuc_text = tk.Text(root, height=20, width=50)
sonuc_text.pack()

# Pencere çalıştırılır
root.mainloop()
