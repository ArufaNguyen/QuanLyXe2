from Utils.tong_thoi_gian import to_time
def to_money(username1):
    time = to_time(username1)
    money = time['Perfect_hour'] * 14000
    return format(round(money), ',').replace(',', '.')