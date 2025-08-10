from Utils.time_utils import to_hours

def to_money(username: str, rate_per_hour: int = 14000) -> str:
    """
    Tính tiền dựa trên thời gian sử dụng (giờ chuẩn) nhân với đơn giá.
    Trả về chuỗi có dấu chấm ngăn cách phần nghìn.
    """
    time_info = to_hours(username)
    money = time_info['Perfect_hour'] * rate_per_hour
    return format(round(money), ',').replace(',', '.')
