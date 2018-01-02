from flask import Flask, render_template, request, jsonify
from src.reader import load_from_file
from src.content_manager import get_data

arabic = load_from_file("static/arabic/quran-uthmani.txt")
yusuf_ali_translation = load_from_file("static/translations/en.yusufali.txt")
shakir_translation = load_from_file("static/translations/en.shakir.txt")
maulana_maududi_translation = load_from_file("static/translations/ur.maududi.txt")
maulana_jalandhry_translation = load_from_file("static/translations/ur.jalandhry.txt")

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello"

@app.route('/api/ruku/<int:ruku_number>')
def get_ruku_data(ruku_number):
    get_data()
    obj =  {
        "ruku_number": ruku_number
    }

    return jsonify(obj)

if __name__ == '__main__':
   app.run(debug = True)
