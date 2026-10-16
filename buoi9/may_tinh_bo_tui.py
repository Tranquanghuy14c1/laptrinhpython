import tkinter as tk

def bam_nut(ky_tu):
    hien_tai = bien_bieu_thuc.get()
    bien_bieu_thuc.set(hien_tai + str(ky_tu))

def tinh_toan():
    try:
        bieu_thuc = bien_bieu_thuc.get()
        ket_qua = eval(bieu_thuc)
        bien_bieu_thuc.set(str(ket_qua))
    except ZeroDivisionError:
        bien_bieu_thuc.set("Loi: Chia cho 0")
    except Exception:
        bien_bieu_thuc.set("Loi")

def xoa():
    bien_bieu_thuc.set("")

cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("300x380")
cua_so.resizable(False, False)

bien_bieu_thuc = tk.StringVar()

# O hien thi bieu thuc / ket qua
entry_man_hinh = tk.Entry(cua_so, textvariable=bien_bieu_thuc, font=("Arial", 16), justify="right", bd=10)
entry_man_hinh.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="we")

# Danh sach cac nut ban phim so va phep tinh: 0-9, + - * /, C, =
cac_nut = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (ky_tu, dong, cot) in cac_nut:
    if ky_tu == '=':
        cmd = tinh_toan
    elif ky_tu == 'C':
        cmd = xoa
    else:
        cmd = lambda k=ky_tu: bam_nut(k)
    tk.Button(cua_so, text=ky_tu, font=("Arial", 14), width=5, height=2, command=cmd).grid(row=dong, column=cot, padx=5, pady=5)

if __name__ == "__main__":
    cua_so.mainloop()
