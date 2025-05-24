"""
Kyle Parsotan
May 5th, 2025
lab 13 Flask App
"""

from email import header
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from datetime import timedelta
import os

### python anywhere

import sys
import os

# Add your project directory to the sys.path
project_home = '/home/SWEdev12/my_flask_app'
if project_home not in sys.path:
    sys.path.append(project_home)

# Set the Flask app
# from app import app as application

### python anywhere

app = Flask(__name__)

app.secret_key = os.urandom(24).hex()
app.config["SECRET_KEY"] = app.secret_key

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:0000@localhost/ecommerceDB"
app.config["SESSION_PERMANENT"] = False  # ✅ Prevent session persistence beyond logout
app.config["SESSION_TYPE"] = "filesystem"  # ✅ Store sessions securely
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=60)
SESSION_TIMEOUT = 900  # Logout after 15 minutes (900 seconds)
app.config["REMEMBER_COOKIE_DURATION"] = timedelta(days=7)  # ✅ Keep users logged in for 7 days

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

login_manager.session_protection = "strong"

# from flask_mail import Mail, Message

# app.config["MAIL_SERVER"] = "smtp.gmail.com"  # Change if using another provider
# app.config["MAIL_PORT"] = 587
# app.config["MAIL_USE_TLS"] = True
# app.config["MAIL_USERNAME"] = "your-email@gmail.com"
# app.config["MAIL_PASSWORD"] = "your-email-password"

# mail = Mail(app)

############ class model ############
class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    
    messages = db.relationship("Message", back_populates="user", lazy="dynamic")  # ✅ Allows fetching all messages
    
    username = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=False)

    reviews = db.relationship("Review", back_populates="user", lazy="dynamic")  # ✅ Optimized lazy loading
    cart_items = db.relationship("Cart", back_populates="user", lazy="dynamic")
    wishlist_items = db.relationship("Wishlist", back_populates="user", lazy="dynamic")
    orders = db.relationship("Order", back_populates="user", lazy="dynamic")

from datetime import datetime
class Review(db.Model):
    __tablename__ = "reviews"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow) 

    user = db.relationship("User", back_populates="reviews")
    product = db.relationship("Product", back_populates="reviews")
class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    new_items = db.Column(db.Boolean, default=False)
    image_url = db.Column(db.String(255))
    featured = db.Column(db.Boolean, default=False)  # ✅ Ensure featured column exists
    discount = db.Column(db.Numeric(10,2), default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # ✅ Auto timestamps new products
    
    images = db.relationship("ProductImage", back_populates="product", cascade="all, delete-orphan")  # ✅ Establishes image relationship

    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)  # ✅ Adds foreign key
    category = db.relationship("Category", back_populates="products")  # ✅ Establishes relationship

    reviews = db.relationship("Review", back_populates="product", cascade="all, delete-orphan")
    
class ProductImage(db.Model):
    __tablename__ = "product_images"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)  # ✅ Links image to product
    image_url = db.Column(db.String(255), nullable=False)  # ✅ Stores image path
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # ✅ Timestamp for image uploads

    product = db.relationship("Product", back_populates="images")  # ✅ Establishes relationship

class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    products = db.relationship("Product", back_populates="category", cascade="all, delete-orphan")  # ✅ Establishes relationship

class Cart(db.Model):
    __tablename__ = "cart"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    quantity = db.Column(db.Integer, default=1)

    user = db.relationship("User", back_populates="cart_items")
    product = db.relationship("Product")

class Wishlist(db.Model):
    __tablename__ = "wishlist"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))

    user = db.relationship("User", back_populates="wishlist_items")
    product = db.relationship("Product")

class Order(db.Model):
    __tablename__ = "orders"
    
    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String(20), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default="Processing")

    user = db.relationship("User", back_populates="orders")
class Message(db.Model):
    __tablename__ = "messages"
    
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship("User", back_populates="messages") 
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    subject = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    user = db.relationship("User")
    
############ class model ############


############ route ############

# home route
@app.route("/")
def home():
    try:
        # ✅ Fetch products and categories from the database
        featured_products = Product.query.filter_by(featured=True).limit(6).all()
        new_arrival = Product.query.filter_by(new_items=True).order_by(Product.created_at.desc()).limit(6).all()
        sale_products = Product.query.filter(Product.discount > 0).limit(6).all()
        categories = Category.query.all()

        if not featured_products:
            flash("No featured products found!", "warning")
        
        if not sale_products:
            flash("No sale products available!", "warning")
            
        if not new_arrival:
            flash("No new items products available!", "warning")
        
        if not categories:
            flash("No categories available!", "warning")

        return render_template(
            "index.html",
            featured_products=featured_products,
            new_arrival=new_arrival,
            sale_products=sale_products,
            categories=categories
        )

    except Exception as e:
        db.session.rollback()  # ✅ Rolls back the database transaction if needed
        app.logger.error(f"Error loading home page: {str(e)}") 
        flash("Something went wrong. Please try again later.", "danger") 
        return render_template("error.html", error_message=str(e))

# error route
@app.route("/error")
def error():
    return render_template("error.html")

# login route
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

@app.route("/login", methods=["GET", "POST"])
def login():
    try:
        if request.method == "POST":
            email = request.form.get("email")  # ✅ Use .get() to prevent KeyError
            password = request.form.get("password")

            if not email or not password:
                flash("Email and password are required!", "warning")
                return redirect(url_for("login"))

            user = User.query.filter_by(email=email).first()

            if user and check_password_hash(user.password, password):
                login_user(user)
                flash("Login successful!", "success")
                return redirect(url_for("dashboard"))
            else:
                flash("Invalid email or password.", "danger")  # ✅ Correct placement
                return redirect(url_for("login"))

        return render_template("login.html")

    except Exception as e:
        app.logger.error(f"Login error: {str(e)}")  # ✅ Logs error for debugging
        flash("An unexpected error occurred. Please try again later.", "danger")
        return redirect(url_for("login"))  # ✅ Prevents app crash
    
# signup route
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        email = request.form.get("email")
        password = generate_password_hash(request.form.get("password"), method="pbkdf2:sha256")
        username = request.form.get("username", f"user_{random.randint(1000, 9999)}")
        address = request.form.get("address", "Not Provided")

        # ✅ Check if email or username already exists
        existing_user = User.query.filter_by(email=email).first()
        existing_username = User.query.filter_by(username=username).first()

        if existing_user:
            flash("Email already exists! Please sign in.", "warning")
            return redirect(url_for("login"))

        if existing_username:
            flash("Username is already taken! Try another.", "warning")
            return redirect(url_for("signup"))

        # ✅ If validation passes, create a new user
        try:
            new_user = User(fname=fname, lname=lname, email=email, password=password, username=username, address=address)
            db.session.add(new_user)
            db.session.commit()
            flash("Signup successful! You can now log in.", "success")
            return redirect(url_for("login"))
        except Exception as e:
            db.session.rollback()
            app.logger.error(f"Signup failed: {str(e)}")
            flash("An unexpected error occurred. Please try again later.", "danger")
            return redirect(url_for("signup"))

    return render_template("signup.html")

# dashboard route
@app.route("/dashboard")
@login_required  # ✅ Requires user to be logged in
def dashboard():
    try:
        flash(f"Welcome {current_user.fname}, you're logged in!", "success")
        return render_template("dashboard.html", user=current_user)  # ✅ Render page instead of redirecting

    except Exception as e:
        app.logger.error(f"Error loading dashboard: {str(e)}")  # ✅ Logs the error
        flash("An unexpected error occurred. Please try again later.", "danger")  # ✅ Friendly error message
        return redirect(url_for("index"))  # ✅ Redirect to home if dashboard fails
    
# logout route
@app.route("/logout")
@login_required
def logout():
    logout_user()  # ✅ Logs out the user
    session.clear()  # ✅ Clears all session data
    flash("You have been logged out successfully, and your session has been cleared.", "info")
    return redirect(url_for("login"))  # ✅ Redirect to login page

@app.route("/products")
def products():
    category_filter = request.args.get("category")  # ✅ Get category from URL query
    
    sale_filter = request.args.get("sale")  # ✅ Check if user wants sale items
    min_price = request.args.get("min_price", type=float)
    max_price = request.args.get("max_price", type=float)
    rating_filter = request.args.get("rating", type=float)

    # ✅ Start with all products
    query = Product.query
    products = query.all()
    categories = Category.query.all()

    # ✅ Apply filters based on user input
    if category_filter:
        query = query.filter(Product.category.has(name=category_filter))
    if sale_filter:
        query = query.filter(Product.discount > 0)
    if min_price and max_price:
        query = query.filter(Product.price.between(min_price, max_price))
    if rating_filter:
        query = query.filter(Product.average_rating >= rating_filter)

    query = Product.query
    if category_filter:
        query = query.filter(Product.category.has(name=category_filter))  # ✅ Filter by category

    products = query.all()
    categories = Category.query.all()

    return render_template("products.html", products=products, categories=categories)

from sqlalchemy.orm import joinedload

# product route
@app.route("/product/<int:product_id>")
def product_detail(product_id):
    try:
        product = Product.query.get_or_404(product_id)
        images = ProductImage.query.filter_by(product_id=product_id).all()
        reviews = Review.query.filter_by(product_id=product_id).all()
        average_rating = db.session.query(db.func.avg(Review.rating)).filter(Review.product_id == product_id).scalar()

        # ✅ Fetch recommended products (similar category)
        recommended_items = Product.query.filter(
            Product.category_id == product.category_id,
            Product.id != product_id
        ).limit(4).all()

        return render_template(
            "product.html",
            product=product,
            images=images,
            reviews=reviews,
            recommended_items=recommended_items,
            average_rating=average_rating
        )

    except Exception as e:
        app.logger.error(f"Error loading product page: {str(e)}")
        flash("Something went wrong while loading the product.", "danger")
        return render_template("error.html", error_message=str(e))

login_manager = LoginManager(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# add cart
@app.route("/add_to_cart/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    cart = session.get("cart", {})
    product = Product.query.get(product_id)

    if not product:
        flash("Product not found!", "danger")
        return redirect(url_for("home"))

    # ✅ Apply sale price if a discount exists, otherwise use original price
    final_price = float(product.price) - float(product.discount) if product.discount > 0 else float(product.price)
    
    

    if str(product_id) in cart:
        cart[str(product_id)]["quantity"] += 1
    else:
        cart[str(product_id)] = {
        "name": product.name,
        "original_price": float(product.price),  # ✅ Ensure original price is stored
        "discount": float(product.discount),
        "final_price": float(product.price) - float(product.discount) if product.discount > 0 else float(product.price),
        "quantity": 1
    }

    session["cart"] = cart
    session["cart_count"] = sum(item["quantity"] for item in cart.values())  # ✅ Updates cart count

    flash("Item added to cart!", "success")
    return redirect(url_for("cart"))

# update cart
@app.route("/update_quantity/<int:product_id>", methods=["POST"])
def update_quantity(product_id):
    cart = session.get("cart", {})
    new_quantity = request.form.get("quantity")

    if str(product_id) in cart and new_quantity.isdigit():
        cart[str(product_id)]["quantity"] = int(new_quantity)

    session["cart"] = cart  # ✅ Save to session
    flash("Cart updated!", "success")

    return redirect(url_for("cart"))

# remove cart
@app.route("/remove_from_cart/<int:product_id>", methods=["POST"])
def remove_from_cart(product_id):
    cart = session.get("cart", {})

    if str(product_id) in cart:
        del cart[str(product_id)]  # ✅ Remove item

    session["cart"] = cart
    flash("Item removed from cart!", "danger")

    return redirect(url_for("cart"))

# cart
@app.route("/cart")
def cart():
    cart = session.get("cart", {})
    
    headers = ["Product", "Quantity", "Price"]  # ✅ Default headers
    if any(item["discount"] > 0 for item in cart.values()):  # ✅ Check if any item has a discount
        headers.append("Discount Price")  # ✅ Add Discount column dynamically
    headers.append("Actions")  # ✅ Always include Actions column

    subtotal = 0
    for item in cart.values():
        # ✅ If the item has a discount, use the discounted price; otherwise, use the original price
        item_price = float(item["original_price"])
        if item["discount"] and item["discount"] > 0:
            item_price -= float(item["discount"])  # ✅ Apply discount
        subtotal += item_price * int(item["quantity"])  # ✅ Add to subtotal

    tax = round(subtotal * 0.08, 2)
    total_price = round(subtotal + tax, 2)

    return render_template(
        "cart.html",
        cart=cart,
        headers=headers,
        subtotal=f"{subtotal:.2f}",
        tax=f"{tax:.2f}",
        total_price=f"{total_price:.2f}"
    )

# order processing route
import random

@app.route("/checkout")
def checkout():
    cart_items = Cart.query.filter_by(user_id=current_user.id).all()
    if not cart_items:
        flash("Your cart is empty!", "warning")
        return redirect(url_for("index"))

    order_number = f"ORD{random.randint(1000, 9999)}"
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    new_order = Order(order_number=order_number, user_id=current_user.id, total_price=total_price)
    db.session.add(new_order)
    db.session.commit()

    Cart.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()
    
    flash(f"Order placed successfully! Your order number is {order_number}", "success")
    return redirect(url_for("orders"))

# get user route
@app.route("/get_users")
def get_users():
    users = User.query.all()  # ✅ Runs within the app context
    return str(users)

# contact us route
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        subject = request.form["subject"]
        message = request.form["message"]
        flash("Your message has been sent!", "success")
        return redirect(url_for("index"))

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)