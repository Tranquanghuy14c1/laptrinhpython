danh_sach_sv = [(8.5, "An"), (7.0, "Binh"), (9.2, "Chi"), (6.5, "Dung")]

# them sinh vien moi
danh_sach_sv.append((8.0, "Em"))

# xoa mot sinh vien (biet chinh xac ca diem va ten)
danh_sach_sv.remove((7.0, "Binh"))

# sua diem cho sinh vien o vi tri xac dinh (vi du vi tri 0)
danh_sach_sv[0] = (9.0, danh_sach_sv[0][1])

# kiem tra mot sinh vien co trong danh sach hay khong
print("Chi co trong danh sach khong?", (9.2, "Chi") in danh_sach_sv)

# sap xep theo diem tang dan
danh_sach_sv.sort() 
print("Danh sach sau khi sap xep theo diem tang dan:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")

# sap xep giam dan
danh_sach_sv.sort(reverse=True)
print("Danh sach sau khi sap xep theo diem giam dan:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")