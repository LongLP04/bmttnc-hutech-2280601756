def chiahetcho5(sonhiphan):
    sothapphan = int(sonhiphan, 2)
    return sothapphan % 5 == 0

# Nhập chuỗi số nhị phân từ người dùng
chuoisonhiphan = input("Nhập chuỗi số nhị phân (phân tách bằng dấu phẩy): ")

# Tách chuỗi thành danh sách các số nhị phân
sonhiphanlist = chuoisonhiphan.split(',')

# Lọc ra các số chia hết cho 5
sochiahetcho5 = [so for so in sonhiphanlist if chiahetcho5(so)]

# In kết quả
if sochiahetcho5:
    ketqua = ','.join(sochiahetcho5)
    print("Các số nhị phân chia hết cho 5:", ketqua)
else:
    print("Không có số nhị phân nào chia hết cho 5.")