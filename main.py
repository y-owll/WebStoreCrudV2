from settings import *
import json

db = SQLAlchemy(app)


class products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    quantityOfBuys = db.Column(db.Integer, nullable=False)

    def json(self):
        return {'id': self.id, 'name': self.name,
                'price': self.price, 'quantity': self.quantity, 'quantityOfBuys': self.quantityOfBuys}

    def add_products(_name, _price, _quantity, _quantityOfBuys):
        new_products = products(name=_name, price=_price, quantity=_quantity, quantityOfBuys = _quantityOfBuys)
        db.session.add(new_products)
        db.session.commit()

    def get_all_products():
        return [products.json(products) for products in products.query.all()]

    def get_products(_id):
        return [products.json(products.query.filter_by(id=_id).first())]

    def update_products(_id, _name, _price, _quantity, _quantityOfBuys):
        products_to_update = products.query.filter_by(id=_id).first()
        products_to_update.name = _name
        products_to_update.price = _price
        products_to_update.quantity = _quantity
        products_to_update.quantityOfBuys = _quantityOfBuys
        db.session.commit()

    def delete_products(_id):
        products.query.filter_by(id=_id).delete()
        db.session.commit()
