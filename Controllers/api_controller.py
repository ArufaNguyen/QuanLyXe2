from flask import Blueprint, jsonify, session, redirect, url_for,render_template
from Services.payment_service import PaymentService
from flask import Flask, request, render_template, redirect, url_for,session
from Utils.Capture import CaptureID
from Utils.image_OCR import OCR_image
from Services import VehicleService
from Services import DashboardDataService
api_bp = Blueprint('api', __name__)

payment_service = PaymentService()

@api_bp.route('/api/checkin', methods=['GET'])
def checkin():
    ID_xe = OCR_image()
    plate_image_url = CaptureID()
    VehicleService().register_vehicle(ID_xe, plate_image_url)
    DashboardDataService().increment_element("xe_vao",1)
    DashboardDataService().close()
    return jsonify({
        "status": "success",
        "message": f"Xe {ID_xe} đã check-in",
        "plate_image": plate_image_url
    })    

# @api_bp.route('/data')
# def get_data():
#     data = payment_service.get_all_payments()
#     return jsonify(data)
