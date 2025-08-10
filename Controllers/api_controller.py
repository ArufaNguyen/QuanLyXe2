from flask import Blueprint, jsonify, session, redirect, url_for,render_template
from Services.payment_service import PaymentService

api_bp = Blueprint('api', __name__)

payment_service = PaymentService()

@api_bp.route('/payment-success')
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


@api_bp.route('/data')
def get_data():
    data = payment_service.get_all_payments()
    return jsonify(data)
