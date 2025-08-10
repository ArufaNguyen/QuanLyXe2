from flask import Blueprint, render_template, session, redirect, url_for
from Services.user_service import UserService
from Utils.Tong_tien import To_Money
from Utils.tong_thoi_gian import To_time

dashboard_bp = Blueprint('dashboard', __name__)

user_service = UserService()

@dashboard_bp.route('/')
def dashboard_view():
    if 'username' not in session:
        return redirect(url_for('auth.login'))

    username = session['username']
    role = session['role']

    # Lấy dữ liệu tính tiền và thời gian
    money = To_Money(username)
    time_info = To_time(username)

    # Lấy thông tin khác từ session (hoặc gọi service để cập nhật)
    qr_code = session.get('qr_code')
    plate_image_url = session.get('plate_image_url')

    if role == 'admin':
        # Nếu có dashboard data, bạn có thể load từ service hoặc session
        dashboard_data = user_service.get_dashboard_data()  # Giả sử service trả dict

        return render_template('admin_dashboard.html',
                               username=username,
                               Time_started=session.get('Time_started'),
                               ID_xe=session.get('ID_xe'),
                               MOney=money,
                               hours=time_info['hours'],
                               minutes=time_info['minutes'],
                               seconds=time_info['seconds'],
                               qr_code=qr_code,
                               so_xe_vao=dashboard_data.get('xe_vao'),
                               so_xe_ra=dashboard_data.get('xe_ra'),
                               slot_trong=dashboard_data.get('slot_trong'),
                               doanh_thu=dashboard_data.get('tien_vao_hom_nay'),
                               most_use_slot=dashboard_data.get('most_use_slot'),
                               least_use_slot=dashboard_data.get('least_use_slot'),
                               admin_online=dashboard_data.get('admin_online'))
    else:
        return render_template('dashboard.html',
                               username=username,
                               Time_started=session.get('Time_started'),
                               ID_xe=session.get('ID_xe'),
                               MOney=money,
                               hours=time_info['hours'],
                               minutes=time_info['minutes'],
                               seconds=time_info['seconds'],
                               qr_code=qr_code)
