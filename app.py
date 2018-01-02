from flask import Flask, render_template, request
from src.reader import load_from_file

arabic = load_from_file("static/arabic/quran-uthmani.txt")
yusuf_ali_translation = load_from_file("static/translations/en.yusufali.txt")
shakir_translation = load_from_file("static/translations/en.shakir.txt")
maulana_maududi_translation = load_from_file("static/translations/ur.maududi.txt")
maulana_jalandhry_translation = load_from_file("static/translations/ur.jalandhry.txt")

app = Flask(__name__)

@app.route('/')
def hello_world():
    #return load_from_file();
    #return maulana_maududi_translation["1:1"]
    return "Hello"

if __name__ == '__main__':
   app.run(debug = True)
