# --- Nhập dữ liệu đầu vào ---
y = int(input("Nhap nam: "))
dow_input = int(input("Nhap thu cho ngay dau tien cua nam: "))
m = int(input("Nhap thang: "))

# --- Tính tổng số ngày từ đầu năm đến hết tháng m ---
s = 0
for i in range(1, m + 1):
    if i in [4, 6, 9, 11]:
        top = 30 # Các tháng có 30 ngày
    elif i == 2:
        # Kiểm tra năm nhuận: chia hết cho 400 hoặc (chia hết cho 4 và không chia hết cho 100)
        # Trong Python, dùng // để đảm bảo kết quả là số nguyên
        if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
            top = 29
        else:
            top = 28
    else:
        top = 31 # Các tháng còn lại 31 ngày
    s += top

s -= top # Trừ lại tháng hiện tại để s là tổng số ngày CỦA CÁC THÁNG TRƯỚC ĐÓ

# --- Xác định người trực đầu tiên của tháng m ---
# p: 0=A, 1=B, 2=C, 3=D, 4=E
p = 0
for i in range(dow_input, s + dow_input):
    if i % 7 != 0: # Nếu không phải Chủ Nhật (thứ 0)
        p = (p + 1) % 5 # Chuyển sang người kế tiếp trong 5 người

# --- Bắt đầu in lịch ---
dow = i % 7 if s > 0 else dow_input # Xác định thứ của ngày mùng 1 tháng m
print("   Sun    Mon    Tue    Wed    Thu    Fri    Sat")

# In khoảng trắng cho các ngày trống đầu tháng
print("       " * dow, end="")

# Vòng lặp in từng ngày trong tháng m
for d in range(1, top + 1):
    print(f"{d:3}", end="") # In số ngày, chiếm 3 khoảng trống

    # Kiểm tra trực nhật
    if (dow + d - 1) % 7 != 0: # Nếu KHÔNG PHẢI Chủ Nhật
        print(f" [{'ABCDE'[p]}]", end="") # In tên người trực
        p = (p + 1) % 5 # Xoay vòng người trực
    else:
        print(" [ ]", end="") # Chủ Nhật để trống

    # Nếu là Thứ Bảy (cuối tuần) thì xuống dòng
    if (dow + d) % 7 == 0:
        print()

# Xuống dòng cuối cùng nếu ngày cuối tháng không phải Thứ Bảy
if (dow + top) % 7 != 0:
    print()
