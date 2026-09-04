kho_hang = [
    ("Ban phim", 250000, 10),
    ("Chuot", 150000, 20),
    ("Man hinh", 2500000, 5)
]

# them san pham moi
kho_hang.append(("Tai nghe", 300000, 15))

# xoa mot san pham
kho_hang.remove(("Chuot", 150000, 20))

# hien thi danh sach kho hang
print("DANH SACH KHO HANG:")
for ten, gia, so_luong in kho_hang:
    print(f"{ten:<12} - Gia: {gia:>10,} - SL: {so_luong}")

# tinh tong gia tri kho hang bang vong lap cong don
tong_gia_tri = 0
for ten, gia, so_luong in kho_hang:
    tong_gia_tri = tong_gia_tri + gia * so_luong

print(f"Tong gia tri kho hang: {tong_gia_tri:,} VND")