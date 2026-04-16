n = int(input("Nhap n: ")) # Nhập số nguyên dương n

print(f"Các số hoàn hảo nhỏ hơn {n}: ", end="") # In dòng thông báo ban đầu

# Vòng lặp i chạy từ 1 đến n (i < n)
for i in range(1, n):
    sum = 0 # sum = 0: Khởi tạo lại tổng ước số cho mỗi số i mới
    
    # Vòng lặp j tìm ước số (j chạy từ 1 đến i/2)
    # Trong Python dùng // 2 để lấy số nguyên, +1 vì range không lấy điểm cuối
    for j in range(1, (i // 2) + 1):
        if i % j == 0: # if ( i % j == 0 ): Kiểm tra j có phải là ước của i không
            sum += j   # sum += j: Nếu đúng thì cộng vào tổng
        
        if sum > i: # sum <= i: Nếu tổng đã lớn hơn i thì dừng vòng lặp j (để giảm số vòng lặp)
            break
            
    if sum == i: # if ( sum == i ): Kiểm tra nếu tổng ước bằng chính số đó
        print(i, end=" ") # In số hoàn hảo tìm được trên cùng một hàng

print() # putchar( '\n' ): Xuống dòng khi kết thúc
