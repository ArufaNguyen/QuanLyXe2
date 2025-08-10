import datetime
import json

def get_day_pass(username: str) -> int:
    """
    Tính số ngày đã trôi qua từ ngày bắt đầu sử dụng trong users.json.
    """
    with open('static/users.json', encoding='utf-8') as f:
        users = json.load(f)

    day_str = None
    for user in users:
        if user.get('username') == username:
            day_str = user.get('Day_started')
            break

    if not day_str or day_str == "NULL":
        return 0

    year, month, day = map(int, day_str.split('-'))
    start_date = datetime.date(year, month, day)
    today = datetime.date.today()
    delta = today - start_date
    return max(delta.days, 0)

def update_day_pass(username: str):
    """
    Cập nhật trường Day_Pass trong users.json cho username.
    """
    days_passed = get_day_pass(username)

    with open('static/users.json', 'r', encoding='utf-8') as f:
        users = json.load(f)

    for user in users:
        if user.get('username') == username:
            user['Day_Pass'] = days_passed
            break

    with open('static/users.json', 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=4, ensure_ascii=False)

def to_hours(username: str) -> dict:
    """
    Tính tổng số giờ đã sử dụng, bao gồm cả ngày đã trôi qua.
    Trả về dict với keys: hours, minutes, seconds, Perfect_hour.
    """
    update_day_pass(username)

    with open('static/users.json', encoding='utf-8') as f:
        users = json.load(f)

    time_str = None
    day_pass = 0
    for user in users:
        if user.get('username') == username:
            time_str = user.get('Time_started')
            day_pass = user.get('Day_Pass', 0)
            break

    if not time_str or time_str == "NULL":
        return {'hours': 0, 'minutes': 0, 'seconds': 0, 'Perfect_hour': 0.0}

    hours, minutes, seconds = map(int, time_str.split(':'))

    total_seconds = hours * 3600 + minutes * 60 + seconds + day_pass * 24 * 3600
    perfect_hour = round(total_seconds / 3600, 2)

    return {
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
        'Perfect_hour': perfect_hour
    }
