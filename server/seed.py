# server/seed.py

from app import app
from models import db, Plant

with app.app_context():
    print("Seeding database...")

    # Drop all rows in the plants table
    Plant.query.delete()

    # Reset auto-incrementing primary key (for SQLite only)
    db.session.execute("DELETE FROM sqlite_sequence WHERE name='plants'")

    # Add sample plants
    p1 = Plant(name="Aloe", image="./images/aloe.jpg", price=11.50, is_in_stock=True)
    p2 = Plant(name="Snake Plant", image="./images/snake.jpg", price=18.00, is_in_stock=True)
    p3 = Plant(name="Peace Lily", image="./images/peace.jpg", price=22.75, is_in_stock=False)

    db.session.add_all([p1, p2, p3])
    db.session.commit()

    print("Seeded plants!")
