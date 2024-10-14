from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
from flask_login import UserMixin, login_user, logout_user, LoginManager, login_required, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = "minha_chave_123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

login_manager = LoginManager()
db = SQLAlchemy(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
#CORS(app)

# Modelagem
# User
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=True)
    cart = db.relationship('CartItem', backref='user', lazy=True)

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
    
# Cart
class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

# Autenticação
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=["POST"])
def login():
    data = request.json
    if 'username' in data and 'password' in data:
        user = User.query.filter_by(username=data["username"], password=data["password"]).first()
        if user:
            login_user(user)
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
@login_required
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
@login_required
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
@login_required
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Produto excluido com sucesso!"})
    return jsonify({"message": "Produto não existe"}), 404

@app.route('/logout', methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Usuario deslogado"})

# CHECKOUT
@app.route('/api/cart/add/<int:product_id>', methods=["POST"])
@login_required
def add_to_cart(product_id):
    # Usuario
    user = User.query.get(current_user.id)
    # Produto
    product = Product.query.get(product_id)

    if user and product:
        cart_item = CartItem(user_id=user.id, product_id=product.id)
        db.session.add(cart_item)
        db.session.commit()
        return jsonify({"message": "Produto adicionado com sucesso no carrinho!"})
    
    return jsonify({"message": "Usuario ou Produto não identificado!"}), 401

@app.route('/api/cart/remove/<int:product_id>', methods=["DELETE"])
@login_required
def remove_item_from_cart(product_id):
    cart_item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
        return jsonify({"message": "Produto removido do carrinho!"})
    
    return jsonify({"message": "Produto não existe no carinho"}), 404

@app.route('/api/cart', methods=["GET"])
@login_required
def view_cart():
    user = User.query.get(int(current_user.id))
    cart_items = user.cart

    items = []
    for item in cart_items:
        product = Product.query.get(item.product_id)
        data = {
            "id":item.id,
            "product":product.name, 
            "price": product.price
        }
        items.append(data)

    return jsonify(items)

@app.route('/api/cart/checkout', methods=["POST"])
@login_required
def checkout():
    user = User.query.get(int(current_user.id))
    cart_items = user.cart
    for item in cart_items:
        db.session.delete(item)
    db.session.commit()
    
    return jsonify({"message": "Carrinho removido com sucesso"})

# Definir uma rota raiz (Página inicial) e a função que será executada ao requisitar
@app.route('/')
def hello_world():
    products = Product.query.all()
    return render_template('index.html', products=products)

if __name__ == "__main__":
    app.run(debug=True)