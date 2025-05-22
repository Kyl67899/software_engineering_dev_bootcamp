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
add_product("16in HP high end gaming Laptop", " 16 in high end gaming laptop", 1599.99, 120, 1, 
            "https://www.bing.com/images/search?view=detailV2&ccid=ZA7d7MoD&id=D54778CF9215536413B3C94088998A3724E6AF6D&thid=OIP.ZA7d7MoDZnMe4ao84yo53gHaFJ&mediaurl=https%3a%2f%2fcdn.oneesports.id%2fcdn-data%2fwp-content%2fuploads%2f2019%2f07%2fHPpavilionultraviolet.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.640eddecca0366731ee1aa3ce32a39de%3frik%3dba%252fmJDeKmYhAyQ%26pid%3dImgRaw%26r%3d0&exph=556&expw=800&q=hp+high+end+gaming+laptop&simid=608001326772480485&FORM=IRPRST&ck=CFDF5CED88D0E5DFC33D926D79524DB9&selectedIndex=9&itb=0", 
            True
           )

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
