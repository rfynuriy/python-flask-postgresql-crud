from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pandas as pd

import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
#menghubungkan dengan uri database
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

db = SQLAlchemy()
migrate = Migrate(app, db)

class Barang(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_barang = db.Column(db.String(100), nullable=False)
    harga = db.Column(db.Integer, nullable=False)
    jumlah_barang = db.Column(db.Integer, nullable=False )

#menyatukan db dan app
db.init_app(app)

#buat tabel
with app.app_context():
    db.create_all()
    print("berhasil membuat table")










