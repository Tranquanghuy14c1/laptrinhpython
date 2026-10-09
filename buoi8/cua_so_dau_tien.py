import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Cửa sổ Tkinter đầu tiên & Frame")
cua_so.geometry("400x300")
cua_so.resizable(False, False)

khung_tren = tk.Frame(cua_so, bg="lightblue", height=100)
khung_tren.pack(fill="x")

khung_duoi = tk.Frame(cua_so, bg="lightyellow")
khung_duoi.pack(fill="both", expand=True)

tk.Label(khung_tren, text="Xin chào Tkinter! (Khu vực tiêu đề)", font=("Arial", 14), bg="lightblue").pack(pady=20)
tk.Label(khung_duoi, text="Khu vực nội dung", font=("Arial", 12), bg="lightyellow").pack(pady=20)

cua_so.mainloop()
