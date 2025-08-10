from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from datetime import datetime
from Repositories.sql_server.user_repository import AccountRepository
from Repositories.sql_server.payment_repository import PaymentRepository
from Utils.money_utils import to_money
from Utils.time_utils import to_hours
import pyodbc
from Repositories.sql_server.data_repository import DashboardDataRepository
app = Flask(__name__)
app.secret_key = 'test123'

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
    time_info = to_hours(username)
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

    if role == 'admin':
        return render_template(
            'admin_dashboard.html',
            username=username,
            money=money,
            time_info=time_info,
            so_xe_vao=so_xe_vao,
            so_xe_ra=so_xe_ra,
            slot_trong=slot_trong,
            doanh_thu=doanh_thu,
            most_use_slot=most_use_slot,
            least_use_slot=least_use_slot,
            admin_online=admin_online,
        )    
    else:
        return render_template('dashboard.html', username=username, money=money, time_info=time_info)

@app.route('/payment-success', methods=['POST'])
def payment_success():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    amount = to_money(username)
    car_code = request.form.get('car_code', '') or ''
    plate_image_url = request.form.get('plate_image_url', '') or ''

    payment_repo = PaymentRepository()
    success = payment_repo.add_payment(username, amount, car_code, plate_image_url)
    payment_repo.close()

    if not success:
        return "Thanh toán thất bại", 500

    # Reset trạng thái user nếu cần - bạn gọi repo hoặc service để làm điều này

    return render_template('success.html')

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
if __name__ == '__main__':
    app.run(debug=True)
