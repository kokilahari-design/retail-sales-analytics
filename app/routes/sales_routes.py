# API Routes

# request gives access to read incoming data from the client. Eg., read JSON body (request.get_json())
# jsonify() - Converts Python dictionaries/lists into proper JSON HTTP responses and send back to the client. JSON is the standard format for sending structured data over HTTP.

from flask import Blueprint, request, jsonify
from app.services.sales_service import insert_sale_record
from app.utils.validator import validate_sale_data

# route() function of the Flask class is a decorator. route() decorator is used to bind URL(API endpoind) to a function(record_sale).
# POST - Send/submit data (your sale event) to server. Here POST method used to create a new resource


sales_blueprint = Blueprint("sales", __name__)

@sales_blueprint.route("/testing", methods=["POST"])
def create_sale():
    data = request.json    # .get_json() method reads the JSON sent by the client and turns it into a Python dictionary.
    valid, message_err = validate_sale_data(data)
    if not valid:
        return jsonify({"error": message_err}), 400                 # jsonify({"msg": "error msg returned to client"}), 400 (Status code - Bad Request due to invalid or missing data)
      
    try:
        sale_id = insert_sale_record(data)
        return jsonify({"message": "Sale recorded Successfully", "id": sale_id}), 201

    except Exception:
        return jsonify({"error": "Internal Server Error"}), 500
