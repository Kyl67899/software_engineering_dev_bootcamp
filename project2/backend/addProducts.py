### add products
from app import db, Product

def add_product(name, description, price, stock, category_id, image_url, featured=False):
    new_product = Product(
        name=name,
        description=description,
        price=price,
        stock=stock,
        category_id=category_id,
        image_url=image_url,
        featured=featured
    )
    db.session.add(new_product)
    db.session.commit()
    print("Product added successfully!")

# Example Usage
add_product("Gaming Laptop", "High-end gaming laptop", 1299.99, 10, 1, "images/laptop.jpg", True)

### add products

def get_products():
    products = Product.query.all()
    for product in products:
        print(f"{product.id}: {product.name} - ${product.price}")

# Example Usage
get_products()

def get_products_by_category(category_id):
    products = Product.query.filter_by(category_id=category_id).all()
    return products


def update_product(product_id, new_price, new_stock):
    product = Product.query.get(product_id)
    if product:
        product.price = new_price
        product.stock = new_stock
        db.session.commit()
        print(f"Product {product.name} updated!")
    else:
        print("Product not found!")

# Example Usage
update_product(1, 1099.99, 5)

def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        print(f"Product {product.name} deleted!")
    else:
        print("Product not found!")

# Example Usage
delete_product(1)
