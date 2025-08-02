# server/app.py

from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Plant

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/plants/<int:id>', methods=['PATCH'])
def update_plant(id):
    plant = Plant.query.get(id)
    if not plant:
        return {"error": "Plant not found"}, 404

    data = request.get_json()

    for attr in data:
        setattr(plant, attr, data[attr])

    db.session.commit()

    return plant.to_dict(), 200

if __name__ == "__main__":
    app.run(port=5555, debug=True)
