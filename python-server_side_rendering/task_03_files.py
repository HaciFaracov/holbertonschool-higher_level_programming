import json
import csv
import os
from flask import Flask, render_template, request

app = Flask(__name__)

def get_json_data():
    if not os.path.exists('products.json'):
        return []
    with open('products.json', 'r') as f:
        return json.load(f)

def get_csv_data():
    products = []
    if not os.path.exists('products.csv'):
        return []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def products_route():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        data = get_json_data()
    else:
        data = get_csv_data()

    if product_id is not None:
        data = [p for p in data if p['id'] == product_id]
        if not data:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
