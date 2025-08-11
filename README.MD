# Smart Parking Management System (SPMS)
**Design and Implement a Smart Parking Management System** — Dự án Python Flask + SQL Server   
Quản lý bãi đỗ xe thông minh với phân quyền, thanh toán, báo cáo và nhận diện biển số.

## Mục tiêu 

Assignment này phát triển hệ thống **Python-based Smart Parking Management System** hỗ trợ:
1. **Tương tác dựa trên vai trò**: Admin, Parking Attendant, Developer/Owner.
2. **Quản lý slot bãi xe**, tính phí, và theo dõi thanh toán.
3. **Cập nhật trạng thái slot thời gian thực** và **lưu trữ dữ liệu**.

## Các vai trò và quyền hạn 
### Admin
- Cấu hình bãi đỗ (theo dõi tổng slot, giá theo giờ).
- Thêm, cập nhật, hoặc xóa slot.
- Xem và xuất báo cáo doanh thu.

### Owner
- Cấu hình bãi đỗ (theo dõi tổng slot, giá theo giờ).
- Thêm, cập nhật, hoặc xóa slot.
- Xem và xuất báo cáo doanh thu.
- Thêm/tạo tài khoản khi mở rộng bãi đỗ.

### Parking Attendant
- Check-in/check-out xe.
- Thanh toán trực tuyến.

## Chức năng chính 
1. **Quản lý Slot bãi xe**
   - Thêm, cập nhật, xóa slot.
   - Theo dõi tình trạng slot theo thời gian thực.

2. **Check-in/Check-out xe**
   - Gán slot khi check-in.
   - Giải phóng slot khi check-out & tính phí gửi.

3. **Tính phí gửi**
   - Giá theo giờ.
   - Tính dựa trên thời gian gửi (làm tròn giờ).

4. **Báo cáo & thống kê**
   - Tổng doanh thu (ngày, tuần, tháng).
   - Tỷ lệ lấp đầy (occupancy rate).
   - Slot được dùng nhiều nhất.

5. **Xử lý hình ảnh**
   - Cho phép xem camera dưới quyền admin/owner.
   - Chụp biển số xe và chuyển biển số xe về text.


6. **Lưu trữ dữ liệu**
   - Lưu & tải lại dữ liệu (slots, xe, giao dịch) giữa các phiên.
   - Hỗ trợ export dữ liệu khi cần

## Flowchart 

![Progress 1](image\1.jpg)
![Progress 2](image\2.jpg)
![Progress 3](image\3.jpg)


## Setup
1. **Clone dự án**
```bash
git clone https://github.com/ArufaNguyen/QuanLyXe2.git
cd QuanLyXe2
```
2. **Library yều câu**
```bash
pip install flask pyodbc
pip install import pyodbc
pip install requests
```
4. **Tạo Database**
```bash
create database [QuanLyXeDB]
```
5. **Config**
```bash
Config\QuanLyXeDB.json

------
{

    "DRIVER": "{SQL Server}",
    "SERVER": "localhost,1433",           
    "DATABASE": "QuanLyXeDB",          
    "USERNAME": "sa",                
    "PASSWORD": "Aa123456"     

}
```
## API
```bash
http://localhost:5000/api/users
http://localhost:5000/api/checkin
```
## Demo
![1](image\admin_image.png)
![1](image\attendant_image.png)
![1](image\owner_image.png)


### Assigment E-learning 2 Design and Implement a Smart Parking Management System (SPMS)
## UTH 012012410014 - Ngôn ngữ python - Nhóm 9