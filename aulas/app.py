from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)

# Modelagem
# User
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=True)

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password
        }
# Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True) 

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description
        }

@app.route('/login', methods=["POST"])
def login():
    data = request.json
    if 'username' in data and 'password' in data:
        user = User.query.filter_by(username=data["username"], password=data["password"]).first()
        if user:
            # return user.to_json()
            return jsonify({"message": "Logado com Sucesso!!"})
    return jsonify({"message": "Credenciais invalidas"}), 401

@app.route('/api/products', methods=["GET"])
def get_products():
    products = Product.query.all()
    if products:
        product_list = []
        for product in products:
            data = {
                "id":product.id,
                "name":product.name, 
                "price": product.price,
                "description": product.description
            }
            product_list.append(data)
        return jsonify(product_list)
    
    return jsonify({"message": "Nenhum produto cadastrado"}), 404

@app.route('/api/products/add', methods=["POST"])
def add_product():
    data = request.json
    if 'name' in data and 'price' in data:
        product = Product(name=data["name"], price=data["price"], description=data.get("description", ""))
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Dados cadastrados com sucesso!"})
    return jsonify({"message": "Dados invalidos para o produto"}), 400

@app.route('/api/products/<int:product_id>', methods=["GET"])
def get_product_details(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "Produto não existe"}), 404
    
    return product.to_json()
    
    # Outro metodo
    # return jsonify({
    #     "id": product.id,
    #     "name": product.name, 
    #     "price": product.price,
    #     "description": product.description
    # })

@app.route('/api/products/update/<int:product_id>', methods=["PUT"])
def update_product(product_id):
    data = request.json
    product = Product.query.get(product_id)
    if product:
        if 'name' in data and 'price' in data:
            product.name = data["name"]
            product.price = data["price"]
            product.description = data.get("description", "")
            db.session.commit()
            return jsonify({"message": "Produto atualizado com sucesso!"})
    return jsonify({"message": "Produto não existe"}), 404                  

@app.route('/api/products/delete/<int:product_id>', methods=["DELETE"])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Produto excluido com sucesso!"})
    return jsonify({"message": "Produto não existe"}), 404

# Definir uma rota raiz (Página inicial) e a função que será executada ao requisitar
@app.route('/')
def hello_world():
    products = Product.query.all()
    return render_template('index.html', products=products)

if __name__ == "__main__":
    app.run(debug=True)