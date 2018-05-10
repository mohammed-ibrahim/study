from flask import Flask, render_template, request, jsonify, send_from_directory

# from src.utils.reader import load_from_file, load_json_from_file, load_kvp_from_file
from src.content import content_manager
#  import get_ruku_content, get_root_details
# from src.uti import upload_contest_data

from src.content.contest import Contest
from src.content.app_data import AppData


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
    return jsonify(content_manager.get_ruku_content(app_data, ruku_number))

@app.route('/api/ruku/metadata/<int:ruku_number>')
def get_ruku_metadata(ruku_number):
    return jsonify(app_data.get_surah_and_ruku_metadata(ruku_number))

@app.route('/api/surah/metadata')
def get_surah_metadata():
    return jsonify(app_data.surah_metadata)

# @app.route('/api/contest', methods = ['POST'])
# def upload_dictionary():
#     json_data = request.get_json(force=True)
#     upload_contest_data(contest_data, json_data)
#     return jsonify({"status": "true"})

# @app.route('/api/contest/initial')
# def get_next_initial():
#     (content, response_code) = contest_data.get_next_initial()
#     return jsonify(content), response_code

@app.route('/api/contest/learn')
def get_next_learn():
    (content, response_code) = contest_data.get_next_contest_word()
    return jsonify(content), response_code

@app.route('/api/contest/mcq')
def get_next_mcq():
    (content, response_code) = contest_data.get_next_mcq()
    return jsonify(content), response_code

@app.route('/api/contest/mtf')
def get_next_mtf():
    (content, response_code) = contest_data.get_next_mtf()
    return jsonify(content), response_code

@app.route('/api/contest/sim')
def get_next_sim_api():
    (content, response_code) = contest_data.get_next_sim()

    if response_code <= 200:
        resp = {
            'data': content_manager.get_root_details(app_data, content),
            'seq': content
        }

        return jsonify(resp), response_code

    else:
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

# @app.route('/contest/upload')
# def contest_upload_page():
#     return render_template('contest-upload.html')

# @app.route('/contest/initial')
# def contest_initial_page():
#     return render_template('contest-initial.html')

@app.route('/contest/learn')
def contest_learn_page():
    return render_template('contest-learn.html')

@app.route('/contest/mcq')
def contest_mcq_page():
    return render_template('contest-mcq.html')

@app.route('/contest/mtf')
def contest_mtf_page():
    return render_template('contest-mtf.html')

@app.route('/contest/sim')
def contest_sim_page():
    return render_template('contest-sim.html')

#    _____         .__
#   /     \ _____  |__| ____
#  /  \ /  \\__  \ |  |/    \
# /    Y    \/ __ \|  |   |  \
# \____|__  (____  /__|___|  /
#         \/     \/        \/

if __name__ == '__main__':
   app.run(debug = True)
