from app import app
from extensions import db
from models import Plant

with app.app_context():
    Plant.query.delete()

    plants = [
        Plant(
            name="Aloe",
            image="https://upload.wikimedia.org/wikipedia/commons/c/cb/Aloe_vera_flower.JPG",
            price=11.50,
            is_in_stock=True
        ),
        Plant(
            name="ZZ Plant",
            image="https://upload.wikimedia.org/wikipedia/commons/0/0f/Zamioculcas_zamiifolia.jpg",
            price=25.98,
            is_in_stock=True
        )
    ]

    db.session.add_all(plants)
    db.session.commit()
