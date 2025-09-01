#!/usr/bin/env python3

from app import app
from models import db

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure tables exist
    app.run(port=5555, debug=True)
