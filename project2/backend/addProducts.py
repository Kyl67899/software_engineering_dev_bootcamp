from app import app  # Make sure to import your Flask app instance
from app import db, Product  # Import db and your models

def add_product(name, description, price, discount, stock, new_items, image_url, featured, category_id):
    new_product = Product(
        name=name,
        description=description,
        price=price,
        discount=discount,
        stock=stock,
        new_items= new_items,
        image_url=image_url,
        featured=featured,
        category_id=category_id,
    )
    db.session.add(new_product)
    db.session.commit()

# Wrap your code in an application context
if __name__ == '__main__':
    with app.app_context():
        add_product(
            "14 in HP high end gaming Laptop",
            "14 in high end gaming laptop", 
            1599.99,
            None,
            250,
            True,
            "https://www.bing.com/aclick?ld=e8WvAcuDTAR2YPCSpos8rYjDVUCUyA_KCWgZfy0K7fkdDHrFKn0ks7ntFixOt41pcEsWBruGDvuT2M9NADvAb0CMoFlmPUu_dkc-inQCN4-kIHHewA1yE_T7N6oaegdBsImZUkLfanwA2KBYVkGiV72Cn42cD_fdvlIl17mzKUTn5m72HZTHiGgO_e7AbwyMEC5UBnYw&u=aHR0cHMlM2ElMmYlMmZ3d3cuYW1hem9uLmNvbSUyZkFTVVMtMTQtQ29tcHV0ZXItTWljcm9zb2Z0LUVhcnBob25lcyUyZmRwJTJmQjBEVEI3Wlk4TSUyZnJlZiUzZGFzY19kZl9CMERUQjdaWThNJTNmdGFnJTNkYmluZ3Nob3BwaW5nYS0yMCUyNmxpbmtDb2RlJTNkZGYwJTI2aHZhZGlkJTNkNzk4NTIyMzAzNjUwNzQlMjZodm5ldHclM2RvJTI2aHZxbXQlM2RlJTI2aHZibXQlM2RiZSUyNmh2ZGV2JTNkYyUyNmh2bG9jaW50JTNkJTI2aHZsb2NwaHklM2QlMjZodnRhcmdpZCUzZHBsYS00NTgzNDUxNjkzOTI3OTE2JTI2cHNjJTNkMSUyNm1zY2xraWQlM2Q5ODRmYjA5NjI3YTcxNmRlMzhhYWQ4YTc3MDBkYmE2NA&rlid=984fb09627a716de38aad8a7700dba64&ntb=1", 
            False,
            1
        )
