# -*- coding: utf-8 -*-
import os
import pandas as pd
from flask import Flask, request, jsonify, render_template
from utils.pos_storage import record_transaction

app = Flask(__name__, template_folder="templates")

DATA_DIR = "data_cache"
LOGO_FILE = "logo_perfect_10px.png"
MENU_CSV = os.path.join("static", "menu.csv")

@app.route('/')
def home():
    return render_template("terminal.html")

@app.route('/api/menu', methods=['GET'])
def get_dynamic_menu():
    """Reads inventory options natively from CSV database stream schema mapping"""
    if not os.path.exists(MENU_CSV):
        return jsonify({"error": "Menu database file not found"}), 404
    
    df = pd.read_csv(MENU_CSV)
    catalog = {}
    for _, row in df.iterrows():
        catalog[row['ItemName']] = {
            "price": float(row['UnitPrice']),
            "icon": row['Icon'],
            "category": row['Category']
        }
    return jsonify(catalog)

@app.route('/logo.png')
def serve_logo():
    if os.path.exists(LOGO_FILE):
        from flask import send_file
        return send_file(LOGO_FILE, mimetype='image/png')
    return "Logo missing", 404

@app.route('/api/checkout', methods=['POST'])
def checkout():
    data = request.json
    try:
        file_saved = record_transaction(
            order_id=data['order_id'], item_name=data['item_name'], modifier=data['modifier'],
            qty=data['qty'], unit_price=data['unit_price'], mod_price=data['mod_price'],
            payment_method=data['payment_method'], storage_dir=DATA_DIR
        )
        return jsonify({"status": "success", "message": f"Appended row to {os.path.basename(file_saved)}"}), 200
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
