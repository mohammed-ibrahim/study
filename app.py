from flask import Flask, render_template, request, jsonify, send_from_directory, render_template
from src.reader import load_from_file, load_json_from_file, load_kvp_from_file
from src.content_manager import get_ruku_content
from src.contest import upload_contest_data
from random import shuffle

# ___________                           .__          __  .__
# \__    ___/___________    ____   _____|  | _____ _/  |_|__| ____   ____
#   |    |  \_  __ \__  \  /    \ /  ___/  | \__  \\   __\  |/  _ \ /    \
#   |    |   |  | \// __ \|   |  \\___ \|  |__/ __ \|  | |  (  <_> )   |  \
#   |____|   |__|  (____  /___|  /____  >____(____  /__| |__|\____/|___|  /
#                       \/     \/     \/          \/                    \/

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

#    _____                  ________          __
#   /  _  \ ______ ______   \______ \ _____ _/  |______
#  /  /_\  \\____ \\____ \   |    |  \\__  \\   __\__  \
# /    |    \  |_> >  |_> >  |    `   \/ __ \|  |  / __ \_
# \____|__  /   __/|   __/  /_______  (____  /__| (____  /
#         \/|__|   |__|             \/     \/          \/


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

    english_meaning = load_kvp_from_file("content/translations/english-meaning-v2.txt")

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

# _________                __                   __
# \_   ___ \  ____   _____/  |_  ____   _______/  |_
# /    \  \/ /  _ \ /    \   __\/ __ \ /  ___/\   __\
# \     \___(  <_> )   |  \  | \  ___/ \___ \  |  |
#  \______  /\____/|___|  /__|  \___  >____  > |__|
#         \/            \/          \/     \/
class Contest:
    contest_content = list()
    initial_keywords = list()

    def get_next_contest_word(self):
        if (len(self.initial_keywords) > 0):
            return (self.initial_keywords.pop(), 200)

        if (len(self.contest_content) < 0):
            return ("Dictionary is over", 400)

        return (self.contest_content.pop(), 200)

    def get_next_mcq(self):
        if (len(self.contest_content) < 4):
            return ("Dictionary is over", 400)

        selected = self.contest_content.pop()
        correct_answer = selected['value']
        question = selected['key']

        size = len(self.contest_content)

        op1 = self.contest_content[size-1]
        op2 = self.contest_content[size-2]
        op3 = self.contest_content[size-3]

        options = [selected, op1, op2, op3]
        shuffle(options)
        resp = {
            "question": question,
            "correct_answer": correct_answer,
            "options": options
        }

        shuffle(self.contest_content)
        return (resp, 200)

    def get_next_mtf(self):
        if (len(self.contest_content) < 5):
            return ("Dictionary is over", 400)

        r1 = self.contest_content.pop();
        r2 = self.contest_content.pop();
        r3 = self.contest_content.pop();
        r4 = self.contest_content.pop();
        r5 = self.contest_content.pop();

        correct_order = {}
        correct_order[r1['key']] = r1['value']
        correct_order[r2['key']] = r2['value']
        correct_order[r3['key']] = r3['value']
        correct_order[r4['key']] = r4['value']
        correct_order[r5['key']] = r5['value']

        values = [correct_order[k] for k in correct_order]
        keys = [k for k in correct_order]
        shuffle(values)
        resp = {
            "input": correct_order,
            "value_order": values,
            "key_order": keys
        }
        return (resp, 200)

app_data = AppData()
contest_data = Contest()

app = Flask(__name__, static_url_path='')

#    _____         .__
#   /  _  \ ______ |__|
#  /  /_\  \\____ \|  |
# /    |    \  |_> >  |
# \____|__  /   __/|__|
#         \/|__|

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

@app.route('/api/contest', methods = ['POST'])
def upload_dictionary():
    json_data = request.get_json(force=True)
    upload_contest_data(contest_data, json_data)
    return jsonify({"status": "true"})

@app.route('/api/contest/learn')
def get_next_contest_word():
    (content, response_code) = contest_data.get_next_contest_word()
    #(content, response_code) = contest_data.get_next_mtf()
    return jsonify(content), response_code

#   ___ ___   __          .__
#  /   |   \_/  |_  _____ |  |
# /    ~    \   __\/     \|  |
# \    Y    /|  | |  Y Y  \  |__
#  \___|_  / |__| |__|_|  /____/
#        \/             \/

@app.route('/ruku/<int:ruku_number>')
def ruku_page(ruku_number):
    try:
        return render_template('ruku.html')
    except Exception, e:
        return str(e), 500

@app.route('/contest/upload')
def contest_upload_page():
    return render_template('contest-upload.html')

@app.route('/contest/learn')
def contest_learn_page():
    return render_template('contest-learn.html')

#    _____         .__
#   /     \ _____  |__| ____
#  /  \ /  \\__  \ |  |/    \
# /    Y    \/ __ \|  |   |  \
# \____|__  (____  /__|___|  /
#         \/     \/        \/

if __name__ == '__main__':
   app.run(debug = True)
