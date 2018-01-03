from flask import Flask, render_template, request, jsonify
from src.reader import load_from_file, load_json_from_file
from src.content_manager import get_ruku_content

class AppData:
    arabic = load_from_file("static/arabic/quran-uthmani.txt")
    translation_yusuf_ali = load_from_file("static/translations/en.yusufali.txt")
    translation_shakir = load_from_file("static/translations/en.shakir.txt")
    translation_maulana_maududi = load_from_file("static/translations/ur.maududi.txt")
    translation_maulana_jalandhry = load_from_file("static/translations/ur.jalandhry.txt")
    surah_metadata = load_json_from_file("static/metadata/surah_metadata.json")
    ruku_to_surah_mapping = load_json_from_file("static/metadata/ruku_to_surah_mapping.json")
    verse_number_to_root_sequence_mapping = load_json_from_file("static/metadata/verse_number_to_root_sequence_mapping.json")
    root_statistics = load_json_from_file("static/metadata/root_statistics.json")

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

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello"

@app.route('/api/ruku/<int:ruku_number>')
def get_ruku_data(ruku_number):
    return jsonify(get_ruku_content(app_data, ruku_number))

@app.route('/api/ruku/metadata/<int:ruku_number>')
def get_ruku_metadata(ruku_number):
    return jsonify(app_data.get_surah_and_ruku_metadata(ruku_number))

if __name__ == '__main__':
   app.run(debug = True)
