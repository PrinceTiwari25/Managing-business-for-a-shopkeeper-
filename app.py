from flask import Flask, render_template_string, request

app = Flask(__name__)
inventory = []

html_code = open('index.html', 'r', encoding='utf-8').read()

@app.route('/')
def home():
    inventory_table = ""
    total_purchase = 0
    total_sale = 0

    for item in inventory:
        inventory_table += f"<tr><td>{item['date']}</td><td>{item['name']}</td><td>{item['purchase_price']}</td><td>{item['selling_price']}</td><td>{item['quantity']}</td></tr>"
        total_purchase += int(item['purchase_price']) * int(item['quantity'])
        total_sale += int(item['selling_price']) * int(item['quantity'])

    profit = total_sale - total_purchase

    page = html_code
    page = page.replace('<!-- Items will be shown here -->', inventory_table)
    page = page.replace('<!--purchase-->', str(total_purchase))
    page = page.replace('<!--sale-->', str(total_sale))
    page = page.replace('<!--profit-->', str(profit))

    return render_template_string(page)

@app.route('/add_item', methods=['POST'])
def add_item():
    date = request.form['date']
    name = request.form['item_name']
    purchase_price = request.form['purchase_price']
    selling_price = request.form['selling_price']
    quantity = request.form['quantity']
    inventory.append({
        'date': date,
        'name': name,
        'purchase_price': purchase_price,
        'selling_price': selling_price,
        'quantity': quantity
    })
    return home()

if __name__ == '__main__':
    app.run(debug=True)
