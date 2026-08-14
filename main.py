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


# tabel barang
class infentori(db.Model):
    __tablename__ = 'infentori'
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

@app.route('/tambah', methods=['POST'])
def tambah_barang():
    data = request.get_json()
    b = data['nama_barang']
    h = data['harga']
    j = data['jumlah_barang']
    hasil = infentori(nama_barang=b, harga=h, jumlah_barang= j)
    db.session.add(hasil)
    db.session.commit()
    return jsonify({'masage': 'data berhasil di tambah'})

@app.route('/edit/data/<int:target_id>', methods=['PATCH'])
def edit_barang(target_id):
    target = infentori.query.get(target_id)
    data = request.get_json()
    target.nama_barang = data.get('nama_barang', target.nama_barang)
    target.harga = data.get('harga', target.harga)
    target.jumlah_barang = data.get('jumlah_barang', target.jumlah_barang)
    db.session.commit()
    return jsonify({'masage': 'barang berhasil di edit'})

@app.route('/hapus/<int:target_id>', methods=['DELETE'])
def hapus_data(target_id):
    target = infentori.query.get(target_id)
    db.session.delete(target)
    db.session.commit()
    return jsonify({'masage': 'data berhasil dihapus'})



if __name__ == '__main__':
    app.run(debug=True)








