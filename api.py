from main import *


@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({'products': products.get_all_products()})


@app.route('/products/<int:id>', methods=['GET'])
def get_products_by_id(id):
    return_value = products.get_products(id)
    return jsonify(return_value)


@app.route('/products', methods=['POST'])
def add_products():
    request_data = request.get_json()
    products.add_products(request_data["name"], request_data["price"],
                    request_data["quantity"], request_data["quantityOfBuys"])
    response = Response("products added", 201, mimetype='application/json')
    return response


@app.route('/products/<int:id>', methods=['PUT'])
def update_products(id):
    request_data = request.get_json()
    products.update_products(id, request_data['name'], request_data['price'], request_data["quantity"], request_data["quantityOfBuys"])
    response = Response("products Updated", status=200, mimetype='application/json')
    return response


@app.route('/products/<int:id>', methods=['DELETE'])
def remove_products(id):
    products.delete_products(id)
    response = Response("products Deleted", status=200, mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run(port=1234, debug=True)