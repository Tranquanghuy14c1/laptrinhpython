# =======================================================
# ĐỒ ÁN: QUẢN LÝ THƯ VIỆN MƯỢN/TRẢ SÁCH (CONSOLE APP)
# =======================================================

# 1. Khởi tạo dữ liệu ban đầu
danh_sach_sach = [
    {"ma_sach": "B101", "ten_sach": "Lap trinh Python", "the_loai": "Cong nghe", "tong_so_luong": 5, "so_luong_con": 5},
    {"ma_sach": "B102", "ten_sach": "Cau truc du lieu", "the_loai": "Giao trinh", "tong_so_luong": 3,
     "so_luong_con": 3},
    {"ma_sach": "B103", "ten_sach": "Tri tue nhan tao", "the_loai": "Cong nghe", "tong_so_luong": 4, "so_luong_con": 4},
    {"ma_sach": "B104", "ten_sach": "Dac nhan tam", "the_loai": "Ky nang", "tong_so_luong": 6, "so_luong_con": 6},
]

lich_su_muon_tra = []


# 2. Hàm hỗ trợ nhập liệu an toàn
def nhap_so_nguyen(loi_nhac):
    """Bắt buộc nhập số nguyên dương, dùng try-except để chống crash chương trình."""
    while True:
        try:
            gia_tri = int(input(loi_nhac))
            if gia_tri > 0:
                return gia_tri
            print("-> So luong phai lon hon 0, vui long nhap lai.")
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so nguyen.")


# 3. Các hàm tra cứu và hiển thị
def tim_sach_theo_ma(ma_sach):
    """Tìm và trả về dictionary của cuốn sách theo mã."""
    for sach in danh_sach_sach:
        if sach["ma_sach"].upper() == ma_sach.upper():
            return sach
    return None


def hien_thi_danh_sach_sach():
    """Hiển thị toàn bộ kho sách theo dạng bảng."""
    print("\n" + "=" * 75)
    print(f"{'Ma sach':<10}{'Ten sach':<26}{'The loai':<15}{'Tong SL':<12}{'Con lai':<12}")
    print("-" * 75)
    for sach in danh_sach_sach:
        print(f"{sach['ma_sach']:<10}{sach['ten_sach']:<26}{sach['the_loai']:<15}"
              f"{sach['tong_so_luong']:<12}{sach['so_luong_con']:<12}")
    print("=" * 75)


def xem_sach_san_co():
    """Lọc và hiển thị các sách có số lượng còn lại > 0."""
    sach_co_san = [s for s in danh_sach_sach if s["so_luong_con"] > 0]
    if len(sach_co_san) == 0:
        print("-> Hien tai thu vien da het sach de muon.")
        return

    print("\nCAC DAU SACH DANG SAN CO TRONG KHO:")
    for sach in sach_co_san:
        print(f" {sach['ma_sach']} - {sach['ten_sach']} ({sach['the_loai']}) - Con: {sach['so_luong_con']} cuon")


# 4. Các hàm nghiệp vụ (Thêm, Mượn, Trả)
def them_sach(ma_sach, ten_sach, the_loai, so_luong):
    """Thêm đầu sách mới vào hệ thống."""
    if tim_sach_theo_ma(ma_sach) is not None:
        print(f"-> Ma sach {ma_sach} da ton tai trong thu vien, khong the them.")
        return

    danh_sach_sach.append({
        "ma_sach": ma_sach,
        "ten_sach": ten_sach,
        "the_loai": the_loai,
        "tong_so_luong": so_luong,
        "so_luong_con": so_luong
    })
    print(f"-> Da them sach '{ten_sach}' ({ma_sach}) thanh cong.")


def muon_sach(ma_sach, ten_doc_gia, so_luong):
    """Xử lý mượn sách, giảm tồn kho và ghi lịch sử."""
    sach = tim_sach_theo_ma(ma_sach)

    if sach is None:
        print(f"-> Khong tim thay ma sach {ma_sach}.")
        return

    if sach["so_luong_con"] == 0:
        print(f"-> Sach '{sach['ten_sach']}' hien da het trong kho, khong the muon.")
        return

    if so_luong > sach["so_luong_con"]:
        print(f"-> Thu vien chi con {sach['so_luong_con']} cuon, khong du so luong yeu cau.")
        return

    sach["so_luong_con"] -= so_luong
    lich_su_muon_tra.append({
        "ma_sach": sach["ma_sach"],
        "ten_sach": sach["ten_sach"],
        "ten_doc_gia": ten_doc_gia,
        "hanh_dong": "Muon",
        "so_luong": so_luong
    })
    print(f"-> Cho doc gia {ten_doc_gia} muon {so_luong} cuon '{sach['ten_sach']}' thanh cong.")


def tra_sach(ma_sach, ten_doc_gia, so_luong):
    """Xử lý nhận trả sách, tăng tồn kho và ghi lịch sử."""
    sach = tim_sach_theo_ma(ma_sach)

    if sach is None:
        print(f"-> Khong tim thay ma sach {ma_sach}.")
        return

    sach_dang_muon = sach["tong_so_luong"] - sach["so_luong_con"]

    if sach_dang_muon == 0:
        print(f"-> Toan bo sach '{sach['ten_sach']}' da co o thu vien, khong co sach nao dang duoc muon.")
        return

    if so_luong > sach_dang_muon:
        print(f"-> So luong tra ({so_luong}) vuot qua so sach dang duoc muon ngoai thu vien ({sach_dang_muon} cuon).")
        return

    sach["so_luong_con"] += so_luong
    lich_su_muon_tra.append({
        "ma_sach": sach["ma_sach"],
        "ten_sach": sach["ten_sach"],
        "ten_doc_gia": ten_doc_gia,
        "hanh_dong": "Tra",
        "so_luong": so_luong
    })
    print(f"-> Nhan tra {so_luong} cuon '{sach['ten_sach']}' tu doc gia {ten_doc_gia} thanh cong.")


# 5. Hàm thống kê hoạt động
def thong_ke_hoat_dong():
    """Liệt kê toàn bộ lịch sử giao dịch và thống kê sách ngoài thư viện."""
    if len(lich_su_muon_tra) == 0:
        print("-> Chua co giao dich muon/tra nao.")
        return

    print("\nLICH SU GIAO DICH MUON / TRA:")
    for gd in lich_su_muon_tra:
        print(f" [{gd['hanh_dong']}] Doc gia: {gd['ten_doc_gia']:<15} - "
              f"Sach: {gd['ten_sach']:<22} ({gd['ma_sach']}) - SL: {gd['so_luong']}")

    tong_dang_muon = sum(s["tong_so_luong"] - s["so_luong_con"] for s in danh_sach_sach)
    print(f"\n>>> TONG SO SACH DANG DUOC MUON NGOAI THU VIEN: {tong_dang_muon} cuon")


# 6. Điều hướng Console
def hien_thi_menu():
    print("\n===== QUAN LY THU VIEN MUON/TRA SACH =====")
    print("1. Hien thi danh sach tat ca sach")
    print("2. Xem cac sach dang co san trong kho")
    print("3. Them sach moi")
    print("4. Muon sach cho doc gia")
    print("5. Tra sach vao kho")
    print("6. Thong ke hoat dong muon/tra")
    print("0. Thoat chuong trinh")


def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban: ").strip()

        if lua_chon == "1":
            hien_thi_danh_sach_sach()

        elif lua_chon == "2":
            xem_sach_san_co()

        elif lua_chon == "3":
            print("\n--- THEM SACH MOI ---")
            ma_sach = input("Nhap ma sach moi: ").strip().upper()
            ten_sach = input("Nhap ten sach: ").strip().title()
            the_loai = input("Nhap the loai: ").strip().title()
            so_luong = nhap_so_nguyen("Nhap so luong sach: ")
            them_sach(ma_sach, ten_sach, the_loai, so_luong)

        elif lua_chon == "4":
            print("\n--- MUON SACH ---")
            ma_sach = input("Nhap ma sach can muon: ").strip().upper()
            ten_doc_gia = input("Nhap ten doc gia: ").strip().title()
            so_luong = nhap_so_nguyen("Nhap so luong can muon: ")
            muon_sach(ma_sach, ten_doc_gia, so_luong)

        elif lua_chon == "5":
            print("\n--- TRA SACH ---")
            ma_sach = input("Nhap ma sach can tra: ").strip().upper()
            ten_doc_gia = input("Nhap ten doc gia tra sach: ").strip().title()
            so_luong = nhap_so_nguyen("Nhap so luong tra: ")
            tra_sach(ma_sach, ten_doc_gia, so_luong)

        elif lua_chon == "6":
            thong_ke_hoat_dong()

        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break

        else:
            print("-> Lua chon khong hop le, vui long chon lai tu 0 den 6.")


# Khởi chạy ứng dụng
if __name__ == "__main__":
    chay_chuong_trinh()