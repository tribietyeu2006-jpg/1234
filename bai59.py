# Khai báo thư viện vào/ra chuẩn
#include <stdio.h>

# Hàm main – chương trình bắt đầu chạy từ đây
int main() {

 # Khai báo biến n để lưu năm dương lịch
 int n;

 # Mảng CAN gồm 10 phần tử (chu kỳ 10 năm)
 char can[][5] = {"Canh", "Tan", "Nham", "Quy", "Giap",
                  "At", "Binh", "Dinh", "Mau", "Ky"};

 # Mảng CHI gồm 12 phần tử (chu kỳ 12 năm)
 char chi[][5] = {"Than", "Dau", "Tuat", "Hoi", "Ty", "Suu",
                  "Dan", "Meo", "Thin", "Ty", "Ngo", "Mui"};

 # In ra thông báo yêu cầu nhập năm
 printf("Nhap nam: ");

 # Nhập năm dương lịch từ bàn phím
 scanf("%d", &n);

 # Xuất năm dương lịch kèm tên năm âm lịch (Can Chi)
 printf("%d - %s %s\n", n, can[(n + 60) % 10], chi[(n % 12)]);

 # Kết thúc chương trình
 return 0;
}
``
