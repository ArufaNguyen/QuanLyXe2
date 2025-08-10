from flask import Blueprint, jsonify, session, redirect, url_for,render_template
from Services.payment_service import PaymentService
from flask import Flask, request, render_template, redirect, url_for,session


api_bp = Blueprint('api', __name__)
app = Flask(__name__)
app.secret_key = 'test123'

app.register_blueprint(api_bp)

payment_service = PaymentService()

# @app.route('/payment-success')
# def payment_success():
#     if 'username' not in session:
#         return redirect(url_for('login'))

#     username = session['username']
#     money = payment_service.calculate_money(username)
#     id_xe = session.get('ID_xe')
#     plate_image_url = session.get('plate_image_url')

#     payment_service.record_payment(username, money, id_xe, plate_image_url)
#     payment_service.reset_user_status(username)

#     return render_template('success.html')


@api_bp.route('/data')
def get_data():
    data = payment_service.get_all_payments()
    return jsonify(data)
