# server/seed.py

from app import app
from models import db, Plant

with app.app_context():
    print("Seeding database...")

    # Clear out the plants table
    Plant.query.delete()

    # Reset the primary key counter (works for SQLite only)
    # If you're using another database (Postgres/MySQL), comment this out.
    try:
        db.session.execute("DELETE FROM sqlite_sequence WHERE name='plants'")
    except Exception:
        # Ignore if not using SQLite
        pass

    # Add sample plants
    plants = [
        Plant(name="Aloe", image="./images/aloe.jpg", price=11.50, is_in_stock=True),
        Plant(name="Snake Plant", image="./images/snake.jpg", price=18.00, is_in_stock=True),
        Plant(name="Peace Lily", image="./images/peace.jpg", price=22.75, is_in_stock=False),
    ]

    db.session.add_all(plants)
    db.session.commit()

    print("✅ Database seeded!")
