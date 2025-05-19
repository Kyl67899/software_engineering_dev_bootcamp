"""
Kyle Parsotan
May 5th, 2025
lab 13 Flask App
"""

from flask import Flask, render_template, session, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:0000@localhost/ecommerceDB"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = ""
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=60)

login_manager.session_protection = "strong"
app.config["REMEMBER_COOKIE_DURATION"] = timedelta(days=7)  # ✅ Keep users logged in for 7 days


from flask_mail import Mail, Message

app.config["MAIL_SERVER"] = "smtp.gmail.com"  # Change if using another provider
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "your-email@gmail.com"
app.config["MAIL_PASSWORD"] = "your-email-password"

SESSION_PERMANENT = False
SESSION_TYPE = "filesystem"
SESSION_TIMEOUT = 900  # Logout after 15 minutes (900 seconds)

mail = Mail(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

# User Model
class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=True)  # Adjusted datatype for phone number
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    
    # change to role after 
    role = db.Column(db.String(20), default="user")  # ✅ Assign roles: 'admin', 'staff', 'user'

    # ✅ Correct Relationships
    reviews = db.relationship("Review", back_populates="user", lazy=True) 
    favorites = db.relationship("favorite", back_populates="user", lazy=True)
    orders = db.relationship("Order", back_populates="user", lazy=True)
    cart_items = db.relationship("Cart", back_populates="user", lazy=True)
    review_replies = db.relationship("ReviewReply", back_populates="user", lazy=True)

# favorite model
class Favorite(db.Model):
    __tablename__ = "favorite"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)

    user = db.relationship("User", back_populates="favorites")
    product = db.relationship("Product", back_populates="favorites")
    
# Product Model
class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=True)
    image_url = db.Column(db.String(255), nullable=True)
    rating = db.Column(db.Integer, default=0)
    
    favorites = db.relationship("Favorite", back_populates="product", lazy=True)
    reviews = db.relationship("Review", back_populates="product", lazy=True)  
    # favorited_by = db.relationship("Favorite", back_populates="product", lazy=True) 
    name = db.Column(db.String(100), nullable=False, index=True) 
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True, index=True) 
    carted_by = db.relationship("Cart", back_populates="product", lazy=True)  
    
# order model
from datetime import datetime, timedelta

class Order(db.Model):
    __tablename__ = "order"
    
    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String(20), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False) 
    
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    product_title = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    purchase_date = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="orders", lazy=True) 
    
    @property
    def can_review(self):
        return datetime.utcnow() >= self.purchase_date + timedelta(hours=24)

#review model
class Review(db.Model):
     __tablename__ = "reviews"
     id = db.Column(db.Integer, primary_key=True)
     user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
     product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
     title = db.Column(db.String(255), nullable=False)
     description = db.Column(db.Text, nullable=False)
     rating = db.Column(db.Integer, nullable=False)
     
     user = db.relationship("User", back_populates="reviews")
     product = db.relationship("Product", back_populates="reviews") 
     category = db.relationship("Category", back_populates="reviews")
     replies = db.relationship("ReviewReply", back_populates="review", lazy=True)

# review reply model
class ReviewReply(db.Model):
    __tablename__ = "ReviewReply" 
    id = db.Column(db.Integer, primary_key=True)
    review_id = db.Column(db.Integer, db.ForeignKey("review.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    review = db.relationship("Review", back_populates="replies") 
    user = db.relationship("User", back_populates="review_replies")

# category model
class Category(db.Model):
    __tablename__ = "categories"
    __table_args__ = {'extend_existing': True} 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)


# Sales Model
class Sale(db.Model):
    __tablename__ = "sales"
    
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Cart model
class Cart(db.Model):
    __tablename__ = "cart"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False) 
    quantity = db.Column(db.Integer, nullable=False, default=1)

    user = db.relationship("User", back_populates="cart_items")
    product = db.relationship("Product", back_populates="carted_by") 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# home route
@app.route("/")
def home():
        # try:
        #    products = Product.query.all()
        #    return render_template("index.html", products=products)
        # except Exception as e:
        #     return f"Error fetching products: {e}", 500
        
        try:
            products = Product.query.all()
            categories = Category.query.all()  # Fetch categories
            featured_items = Product.query.filter_by(featured=True).limit(6).all()  # Featured products
            sale_items = Product.query.filter(Product.price < 50).limit(6).all()  # Sale products
            clothing_items = Product.query.filter(Product.category_id == 2).limit(4).all()  # Clothing section
            user_logged_in = "users_id" in session # check if user is logged in
            admin_logged_in = "admin_id" in session # check if admin is logged in
            admin = User.query.get(session.get("admin_logged_in")) if admin_logged_in else None  # Fetch admin details if logged in
            user = User.query.get(session.get("user_id")) if user_logged_in else None  # Fetch user details if logged in
            
            return render_template("index.html", admin_logged_in=admin_logged_in, admin=admin, user_logged_in=user_logged_in, user=user, products=products, categories=categories, featured_items=featured_items, sale_items=sale_items, clothing_items=clothing_items)
        except Exception as e:
            return f"Error fetching data: {e}", 500

# login route
@app.route("/login", methods=["GET", "POST"])
def login():
    try:
        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]
            
            user = User.query.filter_by(email=email).first()
            
            if user and check_password_hash(user.password, password):
                login_user(user)
                flash("Login successful!", "success")
                return redirect(url_for("dashboard"))
            else:
                flash("Invalid credentials!", "danger")
                return redirect(url_for("login"))
    except Exception as e:
        return f"Error logging in: {e}", 500

from werkzeug.security import generate_password_hash

# sign up route
@app.route("/signup", methods=["GET", "POST"])
def signup():
    try:
        fname = request.form["fname"]
        lname = request.form["lname"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = generate_password_hash(request.form["password"])  # ✅ Hash password
        is_admin = request.form.get("is_admin", False)  # ✅ Only True for admins
        
        new_user = User(fname=fname, lname=lname, email=email, phone=phone, password=password, is_admin=is_admin)
        db.session.add(new_user)
        db.session.commit()
        
        flash("User registered successfully!", "success")
        return redirect(url_for("dashboard"))
    except Exception as e:
        return f"Error logging in: {e}", 500
    
# admin route
@app.route("/admin")
@login_required
def admin_dashboard():
    if current_user.role != "admin":  # ✅ Ensure only admins can access
        flash("Unauthorized access!", "danger")
        return redirect(url_for("dashboard"))

    users = User.query.all()  # Example: List all users
    return render_template("admin.html", users=users)

# admin manage users route
@app.route("/admin/manage_users", methods=["GET", "POST"])
@login_required
def manage_users():
    if current_user.role != "admin":
        flash("Unauthorized access!", "danger")
        return redirect(url_for("dashboard"))

    users = User.query.all()
    return render_template("manage_users.html", users=users)

# timer route
@app.before_request
def session_timeout():
    session.modified = True  # Keeps the session active while the user interacts
    if "user_id" in session:
        session.permanent = True  # Activates the timeout

# logout route
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("index"))

# dashboard route
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])
    purchased_products = Order.query.filter_by(user_id=user.id).all()

    return render_template("dashboard.html", user=user, purchased_products=purchased_products)

# profile route
@app.route("/profile")
@login_required
def profile():
    user = current_user
    purchases = Order.query.filter_by(user_id=user.id).all()
    return render_template("profile.html", user=user, purchases=purchases)

#review route
@app.route("/review/<int:product_id>", methods=["GET", "POST"])
def review(product_id):
    if "user_id" not in session:
        return redirect(url_for("login"))  # Redirect if not logged in

    user = User.query.get(session["user_id"])
    product = Product.query.get(product_id)
    order = Order.query.filter_by(user_id=user.id, product_id=product_id).first()

    if not order or not order.can_review:
        flash("You can only review after 24 hours of receiving the item.", "warning")
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        rating = int(request.form["rating"])  # ✅ Correct syntax
        image_url = request.form["image_url"]
        video_url = request.form["video_url"]

        new_review = Review(
            user_id=user.id, product_id=product_id, title=title,
            description=description, rating=rating, image_url=image_url,
            video_url=video_url
        )

        db.session.add(new_review)
        db.session.commit()
        flash("Review submitted successfully!", "success")
        return redirect(url_for("dashboard"))

    return render_template("review.html", product=product)

# like review
@app.route("/like_review/<int:review_id>")
def like_review(review_id):
    review = Review.query.get(review_id)
    if review:
        review.likes += 1  # Increment likes
        db.session.commit()
    return redirect(url_for("product", product_id=review.product_id))

# reply review
@app.route("/reply_review/<int:review_id>", methods=["POST"])
def reply_review(review_id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    message = request.form["message"]
    new_reply = ReviewReply(review_id=review_id, user_id=session["user_id"], message=message)
    db.session.add(new_reply)
    db.session.commit()
    return redirect(url_for("product", product_id=Review.query.get(review_id).product_id))

# product route
@app.route("/products")
def products():
    page = request.args.get("page", 1, type=int)  # Get the page number from URL
    per_page = 10  # Limit the number of products per page
    
    categories = Category.query.all()
    query = Product.query

    # Apply filters
    min_price = request.args.get("min_price", type=float)
    max_price = request.args.get("max_price", type=float)
    rating = request.args.get("rating", type=float)
    category_id = request.args.get("category_id", type=int)
    search_term = request.args.get("search", type=str)

    if min_price and max_price:
        query = query.filter(Product.price.between(min_price, max_price))
    if rating:
        query = query.filter(Product.rating >= rating)
    if category_id:
        query = query.filter(Product.category_id == category_id)
    if search_term:
        query = query.filter(Product.name.ilike(f"%{search_term}%"))

    paginated_products = query.paginate(page=page, per_page=per_page)

    return render_template(
        "products.html",
        products=paginated_products.items,
        categories=categories,
        pagination=paginated_products  # ✅ Pass pagination variable
    )

# Individual product page
from sqlalchemy.orm import joinedload

@app.route("/product/<int:product_id>")
def product(product_id):
    product = Product.query.get_or_404(product_id)  # ✅ Get product
    reviews = Review.query.filter_by(product_id=product_id).all()  # ✅ Fetch reviews
    return render_template("product.html", product=product, reviews=reviews)

# recommended products
@app.route("/recommended_products")
def recommended_products():
    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])
    
    # Get categories of products the user has purchased
    purchased_categories = set(order.product.category_id for order in Order.query.filter_by(user_id=user.id).all())

    # Get search history
    search_terms = session.get("search_history", [])

    # Recommend based on purchases & searches
    recommended_products = Product.query.filter(
        (Product.category_id.in_(purchased_categories)) | 
        (Product.name.ilike(f"%{search_terms[-1]}%") if search_terms else False)
    ).limit(6).all()

    return render_template("product.html", products=recommended_products)

# search items
@app.route("/search", methods=["GET"])
def search():
    search_term = request.args.get("search", "")

    # Store searches in session (can use database for long-term tracking)
    if "search_history" not in session:
        session["search_history"] = []
    
    if search_term and search_term not in session["search_history"]:
        session["search_history"].append(search_term)
        session.modified = True

    products = Product.query.filter(Product.name.ilike(f"%{search_term}%")).all()
    return render_template("products.html", products=products)

# cart route
from flask import jsonify

@app.route("/add_to_cart/<int:product_id>", methods=["POST"])
@login_required  # Ensure user is logged in
def add_to_cart(product_id):
    user_id = current_user.id  # Get logged-in user
    cart_item = Cart.query.filter_by(user_id=user_id, product_id=product_id).first()

    if cart_item:
        cart_item.quantity += 1  # Increase quantity if item exists
    else:
        cart_item = Cart(user_id=user_id, product_id=product_id, quantity=1)
        db.session.add(cart_item)

    db.session.commit()
    flash("Item added to cart!", "success")
    return redirect(url_for("cart"))

# remove item from cart route
@app.route("/remove_from_cart/<int:product_id>")
def remove_from_cart(product_id):
    if "cart" in session and str(product_id) in session["cart"]:
        session["cart"].pop(str(product_id), None)
        session.modified = True

    return jsonify({"message": "Item removed"})

# toggle cart route
@app.route("/toggle_cart/<int:product_id>", methods=["POST"])
def toggle_cart(product_id):
    if "cart" not in session:
        session["cart"] = {}

    cart = session["cart"]

    if str(product_id) in cart:
        cart.pop(str(product_id), None)  # Remove item
        message = "Removed from Cart"
    else:
        cart[str(product_id)] = 1  # Add item with default quantity
        message = "Added to Cart"

    session.modified = True
    return jsonify({"message": message, "cart_count": sum(cart.values())})

# cart route
@app.route("/cart")
@login_required
def cart():
    user_id = current_user.id
    cart_items = Cart.query.filter_by(user_id=user_id).all()

    total_items = sum(item.quantity for item in cart_items)  # Calculate total quantity

    return render_template("cart.html", cart_items=cart_items, total_items=total_items)

# cart summary route
@app.route("/cart_summary")
def cart_summary():
    cart_items = []
    total_price = 0

    if "cart" in session:
        for product_id, quantity in session["cart"].items():
            product = Product.query.get(product_id)
            cart_items.append({"product": product, "quantity": quantity})
            total_price += product.price * quantity

    return jsonify(cart_items=cart_items, total_price=total_price)

# checkout route
import uuid
from flask import jsonify

# checkout route
import random
import string

# checkout
@app.route("/checkout", methods=["POST"])
@login_required
def checkout():
    user_id = current_user.id
    cart_items = Cart.query.filter_by(user_id=user_id).all()

    if not cart_items:
        flash("Your cart is empty!", "danger")
        return redirect(url_for("cart"))

    # Generate a random order number
    order_number = "ORD-" + "".join(random.choices(string.ascii_uppercase + string.digits, k=8))

    # Create an order for each item in the cart
    for item in cart_items:
        order = Order(
            order_number=order_number,
            user_id=user_id,
            first_name=current_user.fname,
            last_name=current_user.lname,
            email=current_user.email,
            product_title=item.product.name,
            quantity=item.quantity,
        )
        db.session.add(order)

    # Clear cart after purchase
    Cart.query.filter_by(user_id=user_id).delete()
    db.session.commit()

    flash(f"Order placed successfully! Order Number: {order_number}", "success")
    return redirect(url_for("receipt", order_number=order_number))

# receipt route
@app.route("/receipt/<order_number>")
@login_required
def receipt(order_number):
    orders = Order.query.filter_by(order_number=order_number).all()

    if not orders:
        flash("Invalid order number!", "danger")
        return redirect(url_for("cart"))

    return render_template("receipt.html", orders=orders, order_number=order_number)

# track route
@app.route("/track_order", methods=["GET"])
def track_order():
    order_number = request.args.get("order_number")
    order = Order.query.filter_by(order_number=order_number).first()

    if not order:
        return jsonify({"message": "Order not found"}), 404

    return jsonify({
        "order_number": order.order_number,
        "product_title": order.product_title,
        "quantity": order.quantity,
        "purchase_date": order.purchase_date.strftime('%Y-%m-%d %H:%M:%S'),
        "customer_name": f"{order.first_name} {order.last_name}"
    })


if __name__ == "__main__":
    app.run(debug=True)