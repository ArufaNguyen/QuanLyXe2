from Repositories.sql_server.payment_repository import PaymentRepository
from Repositories.sql_server.user_repository import AccountRepository
import datetime

class PaymentService:
    def __init__(self):
        self.payment_repo = PaymentRepository()
        self.user_repo = AccountRepository()

    def calculate_money(self, username):
        # Tính tiền dựa trên username, gọi utils hoặc repo tính toán
        # Giả sử bạn có utils To_Money(username)
        from Utils.money_utils import To_Money
        return To_Money(username)

    def record_payment(self, username, amount, car_code, plate_image_url):
        # Ghi lại thông tin thanh toán vào database hoặc file
        now = datetime.datetime.now()
        payment_data = {
            "account": username,
            "amount": amount,
            "car_code": car_code,
            "time": now.strftime("%Y-%m-%d %H:%M:%S"),
            "plate_image_url": plate_image_url
        }
        return self.payment_repo.save_payment(payment_data)

    def reset_user_status(self, username):
        # Reset trạng thái user sau khi thanh toán thành công
        return self.user_repo.reset_user_status(username)

    def get_all_payments(self):
        # Lấy toàn bộ dữ liệu thanh toán để trả về API
        return self.payment_repo.get_all_payments()

    def close(self):
        self.payment_repo.close()
        self.user_repo.close()
