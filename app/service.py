import os
from flask import Flask


from app.models.models import db
from app.routes.routes import book_bp

app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))


app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database/book.db'

db.init_app(app)
app.register_blueprint(book_bp)

if __name__ == '__main__':
    app.run(debug=True)