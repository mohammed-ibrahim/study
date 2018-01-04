from flask import Flask, render_template, request, jsonify, send_from_directory, render_template
from src.reader import load_from_file, load_json_from_file
from src.content_manager import get_ruku_content

class Translation:
    author = None
    language = ""
    content_map = {}
    def __init__(self, author, language, file_name):
        self.author = author
        self.language = language
        self.content_map = load_from_file(file_name, self.language)

    def get_ayah(self, ayah_number):
        return self.content_map[ayah_number]

    def get_ayah_and_details(self, ayah_number):
        return {
            "author": self.author,
            "ayah_translation": self.content_map[str(ayah_number)],
            "language": self.language
        }

class AppData:
    arabic = load_from_file("content/arabic/quran-uthmani.txt", "ar")

    translation_yusuf_ali = Translation("Yusuf Ali", "en", "content/translations/en.yusufali.txt")
    translation_shakir = Translation("Shakir", "en", "content/translations/en.shakir.txt")
    translation_maulana_maududi = Translation("Maulana Maududi", "ur", "content/translations/ur.maududi.txt")
    translation_maulana_jalandhry = Translation("Maulana Jalandhry", "ur", "content/translations/ur.jalandhry.txt")

    surah_metadata = load_json_from_file("content/metadata/surah_metadata.json")
    ruku_to_surah_mapping = load_json_from_file("content/metadata/ruku_to_surah_mapping.json")
    verse_number_to_root_sequence_mapping = load_json_from_file("content/metadata/verse_number_to_root_sequence_mapping.json")
    root_statistics = load_json_from_file("content/metadata/root_statistics.json")

    translation_sequence = [
        "translation_maulana_jalandhry",
        "translation_maulana_maududi",
        "translation_yusuf_ali",
        "translation_shakir"
    ]

    def get_surah_and_ruku_metadata(self, ruku_number):
        ruku_number_str = str(ruku_number)

        if ruku_number_str not in self.ruku_to_surah_mapping:
            raise Exception('Ruku number: ' + ruku_number_str + ' is not available')

        surah_number = self.ruku_to_surah_mapping[ruku_number_str]["surah_number"]
        ruku_number_of_surah = int(self.ruku_to_surah_mapping[ruku_number_str]["ruku_number_of_surah"])
        surah_data = self.surah_metadata[surah_number]

        if surah_data is None:
            raise Exception('Surah number: ' + surah_number + ' is not available')

        ruku_index_in_surah = ruku_number_of_surah - 1
        ruku_data = surah_data["ruku"][ruku_index_in_surah]

        if ruku_data is None:
            raise Exception('Not able to fetch ruku by ruku index: ' + str(ruku_index_in_surah))

        return {
            "surah_data": surah_data,
            "ruku_data": ruku_data,
            "current_ruku_in_surah": ruku_index_in_surah,
            "surah_number": surah_number
        }

app_data = AppData()

app = Flask(__name__, static_url_path='')

@app.route('/')
def hello_world():
    return "Hello"

@app.route('/api/ruku/<int:ruku_number>')
def get_ruku_data(ruku_number):
    return jsonify(get_ruku_content(app_data, ruku_number))

@app.route('/api/ruku/metadata/<int:ruku_number>')
def get_ruku_metadata(ruku_number):
    return jsonify(app_data.get_surah_and_ruku_metadata(ruku_number))

@app.route('/api/surah/metadata')
def get_surah_metadata():
    return jsonify(app_data.surah_metadata)

@app.route('/ruku/<int:ruku_number>')
def ruku_page(ruku_number):
    try:
        return render_template('ruku.html')
    except Exception, e:
        return str(e), 500

if __name__ == '__main__':
   app.run(debug = True)
