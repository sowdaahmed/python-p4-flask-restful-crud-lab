# server/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plant(db.Model):
    __tablename__ = "plants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # added max length
    image = db.Column(db.String(255), nullable=True)  # safer default length
    price = db.Column(db.Float, nullable=False)
    is_in_stock = db.Column(db.Boolean, default=True, nullable=False)

    def to_dict(self):
        """Serialize Plant instance into dictionary for JSON responses."""
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "price": self.price,
            "is_in_stock": self.is_in_stock,
        }
