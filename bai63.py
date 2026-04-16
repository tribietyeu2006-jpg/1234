#include <stdio.h>      # Thư viện chuẩn cho vào ra
#include <stdlib.h>     # Thư viện cấp phát bộ nhớ, rand, srand
#include <time.h>       # Thư viện xử lý thời gian
#include <math.h>       # Thư viện toán học (dùng hàm abs)
#define MAX 100         # Hằng số MAX = 100, kích thước tối đa của mảng

int main() {            # Hàm main – chương trình bắt đầu chạy
    int a[MAX], n, i, c;# Mảng a, số phần tử n, biến lặp i, biến đếm c

    srand(time(NULL));  # Khởi tạo seed cho hàm rand dựa vào thời gian
    printf("Nhap n [1, %d]: ", MAX - 1); # Xuất thông báo nhập n
    do                # Vòng lặp kiểm tra điều kiện nhập
        scanf("%d", &n); # Nhập số phần tử mảng
    while (n < 1 || n > MAX - 1); # Đảm bảo 1 ≤ n ≤ MAX-1

    for (i = 0; i < n; i++) # Vòng lặp tạo giá trị ngẫu nhiên cho mảng
        printf("%d ", a[i] = rand() % 201 - 100); # Random [-100, 100]

    for (i = c = 0; i < n; i++) # Duyệt mảng và khởi tạo biến đếm
        if (a[i] % 4 == 0 && abs(a[i]) % 10 == 6) c++; # Đếm số chia hết cho 4, tận cùng 6

    printf("\nCo %d phan tu chia het cho 4, tan cung 6\n", c); # In kết quả đếm

    printf("Nhan doi phan tu le:\n"); # Thông báo nhân đôi số lẻ
    for (i = 0; i < n; i++) # Duyệt mảng
        if (a[i] % 2) a[i] *= 2; # Nếu phần tử lẻ thì nhân đôi

    for (i = 0; i < n; i++) # In mảng sau khi xử lý
        printf("%d ", a[i]); # Xuất từng phần tử

    putchar('\n');          # Xuống dòng
    return 0;               # Kết thúc chương trình
}
``
