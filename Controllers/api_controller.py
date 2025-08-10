from flask import Blueprint, jsonify, session, redirect, url_for,render_template
from Services.payment_service import PaymentService
from flask import Flask, request, render_template, redirect, url_for,session


api_bp = Blueprint('api', __name__)
app = Flask(__name__)
app.secret_key = 'test123'

app.register_blueprint(api_bp)

payment_service = PaymentService()

@app.route('/checkin', methods=['GET'])


@api_bp.route('/data')
def get_data():
    data = payment_service.get_all_payments()
    return jsonify(data)
