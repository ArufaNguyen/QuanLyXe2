from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from datetime import datetime
from Repositories.sql_server.user_repository import AccountRepository
from Repositories.sql_server.payment_repository import PaymentRepository
from Utils.Tong_tien import to_money
from Utils.tong_thoi_gian import to_time
import pyodbc
from Repositories.sql_server.data_repository import DashboardDataRepository
from flask import Blueprint, jsonify, session, redirect, url_for,render_template
from Services.payment_service import PaymentService
from flask import Flask, request, render_template, redirect, url_for,session
app = Flask(__name__)
app.secret_key = 'test123'
payment_service = PaymentService()

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/Auth/Login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
    else:
        username = request.args.get('username')
        password = request.args.get('password')
        if not username or not password:
            return render_template('logintest.html')
    account_repo = AccountRepository()
    if account_repo.authenticate(username, password):
        session['username'] = username
        session['role'] = 'admin' if account_repo.is_admin(username) else 'owner'
        # Bạn có thể load thêm session info tại đây nếu cần
        return redirect(url_for('dashboard'))
    else:
        return render_template('logintest.html', error="Sai tên đăng nhập hoặc mật khẩu"), 401

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    role = session['role']
    money = to_money(username)
    # Lấy các biến bạn cần truyền
    dashboard_data = DashboardDataRepository().load_dashboard_data() 
    so_xe_vao = dashboard_data.get('xe_vao')
    so_xe_ra = dashboard_data.get('xe_ra')
    slot_trong = dashboard_data.get('slot_trong')
    doanh_thu = dashboard_data.get('tien_vao_hom_nay')
    most_use_slot = dashboard_data.get('most_use_slot')
    least_use_slot = dashboard_data.get('least_use_slot')
    admin_online = dashboard_data.get('admin_online')
    # Bạn có thể load các dữ liệu khác phục vụ dashboard tại đây
    dashboard_data = AccountRepository().load_username_data()[0]
    ID_xe = dashboard_data.get('ID_xe')
    qr_code = dashboard_data.get('qr_code')
    Time_used = dashboard_data.get('Time_used')
    Time_started = dashboard_data.get('Time_started')
    Day_started = dashboard_data.get('Day_started')
    Day_Pass = dashboard_data.get('Day_Pass')
    hours= to_time(username)["hours"]
    minutes = to_time(username)["minutes"]
    seconds = to_time(username)["seconds"]
    if role == 'admin':
        return render_template(
            'admin_dashboard.html',
            username=username,
            money=money,
            so_xe_vao=so_xe_vao,
            so_xe_ra=so_xe_ra,
            slot_trong=slot_trong,
            doanh_thu=doanh_thu,
            most_use_slot=most_use_slot,
            least_use_slot=least_use_slot,
            admin_online=admin_online,
        )    
    else:
        return render_template(
            'dashboard.html', 
            username=username, 
            money=money, 
            Time_started=Time_started,
            ID_xe=ID_xe,
            qr_code=qr_code,
            hours=hours,
            minutes=minutes
        )



@app.route('/api/payments')
def api_payments():
    payment_repo = PaymentRepository()
    # Giả sử bạn bổ sung hàm get_all_payments() trả về list dict
    payments = payment_repo.get_all_payments() if hasattr(payment_repo, 'get_all_payments') else []
    payment_repo.close()
    return jsonify(payments)
@app.route('/api/data')
def api_data():
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=localhost,1433;'
        'DATABASE=QuanLyXeDB;'
        'UID=sa;'
        'PWD=Aa123456'
    )
    cursor = conn.cursor()
    cursor = conn.cursor()
    cursor.execute("SELECT id, account, amount, car_code, time, plate_image_url FROM data")
    columns = [column[0] for column in cursor.description]
    # Convert từng Row thành dict
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]

    # cursor.close()
    # conn.close()
    return results  
@app.route('/api/dashboard_data')
def api_dashboard_data():
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=localhost,1433;'
        'DATABASE=QuanLyXeDB;'
        'UID=sa;'
        'PWD=Aa123456'
    )
    cursor = conn.cursor()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dashboard_data")
    columns = [column[0] for column in cursor.description]
    # Convert từng Row thành dict
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    # cursor.close()
    # conn.close()
    return results

@app.route('/payment-success')
def payment_success():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    money = payment_service.calculate_money(username)
    id_xe = session.get('ID_xe')
    plate_image_url = session.get('plate_image_url')

    payment_service.record_payment(username, money, id_xe, plate_image_url)
    payment_service.reset_user_status(username)

    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
