from flask import Blueprint, request, render_template, redirect, url_for, session
from Services.user_service import UserService

auth_bp = Blueprint('auth', __name__)

user_service = UserService()

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
    else:
        username = request.args.get('username')
        password = request.args.get('password')
        if not username or not password:
            return render_template('logintest.html')

    user = user_service.authenticate(username, password)
    if user:
        # Lưu thông tin user vào session
        session['username'] = user.username
        session['role'] = user.role
        session['Time_started'] = user.time_started
        session['ID_xe'] = user.id_xe
        session['qr_code'] = user.qr_code
        session['plate_image_url'] = user.plate_image_url

        return redirect(url_for('dashboard.dashboard_view'))
    else:
        return render_template('logintest.html', error="Sai tên đăng nhập hoặc mật khẩu"), 401

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
