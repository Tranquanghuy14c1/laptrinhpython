#1
sinh_vien = { 
    "ho_ten": "Tran Quang Huy",
    "nam_sinh": 2006,
    "diem_tb": 7.5
} 

print(sinh_vien["ho_ten"]) 
print(sinh_vien.get("diem_tb")) 
print(sinh_vien.get("lop", "Chua co")) 


sinh_vien["lop"] = "CNTT01" 
sinh_vien["diem_tb"] = 7.0
print(sinh_vien) 

diem_cu = sinh_vien.pop("diem_tb") 
print(sinh_vien, "- diem da xoa:", diem_cu) 

sinh_vien.update({"nam_sinh": 2006, "email": "a@example.com"})
print(sinh_vien)


#2
diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 6.0, "Van": 6.5}

for mon in diem_mon_hoc.keys(): 
    print(mon) 

for diem in diem_mon_hoc.values(): 
    print(diem) 

for mon, diem in diem_mon_hoc.items(): 
    print(f"{mon}: {diem}") 

tong_diem = 0 
for diem in diem_mon_hoc.values(): 
    tong_diem = tong_diem + diem 

print("Diem trung binh:", round(tong_diem / len(diem_mon_hoc), 2))


#3
diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 6.0, "Van": 6.5}

diem_cong_diem = {mon: round(diem + 0.5, 2) for mon, diem in diem_mon_hoc.items()} 
print(diem_cong_diem) 

ten_mon_viet_hoa = {mon.upper(): diem for mon, diem in diem_mon_hoc.items()} 
print(ten_mon_viet_hoa)


mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"} 
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"} 

print(mon_hoc_ky1 & mon_hoc_ky2) 
print(mon_hoc_ky1 | mon_hoc_ky2) 
print(mon_hoc_ky1 - mon_hoc_ky2)