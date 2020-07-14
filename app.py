from flask import Flask, flash, url_for, render_template, jsonify, abort, session, request, redirect, send_file, send_from_directory
from markupsafe import escape
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
from twitterasscrapper import scrap, writeintocsv
import os
import json
import datetime

try:
    (os.listdir("./tmp"))
except Exception as e:
    os.mkdir("./tmp")
finally:
    TMP_ABS_PATH = os.path.abspath(os.getcwd())+'/tmp/'


TWITTERPARSINGFIELDS = json.load(open('./config/twitter.json'))

app = Flask(__name__)
app.secret_key = 'SOMETHING_VERY_SECRET'

bcrypt = Bcrypt(app)


@app.route('/')
def index():
    # return render_template('index.html')
    return redirect('/twitter')


@app.route('/twitter')
def twitterdashboard():
    allTweetsJson = scrap()
    print(allTweetsJson[0]["user"]["screen_name"])
    return render_template('twitter.html', allTweetsJson=allTweetsJson,
                           parsingFields=TWITTERPARSINGFIELDS)


@app.route('/export_all', methods=["POST"])
def exportToCsv():
    allTweetsJson = scrap()
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d-%H-%M-%S")
    exportation_name = "Carrefour-" + now + ".csv"
    tmpfilename = TMP_ABS_PATH+exportation_name
    f = open(tmpfilename, "a+")
    f.close()
    isSuccess = writeintocsv(allTweetsJson, tmpfilename)
    assert isSuccess
    return jsonify(exportation_name=exportation_name)


@app.route('/report_download/<exportation_name>')
def report_download(exportation_name):
    return send_from_directory(TMP_ABS_PATH, filename=(exportation_name), as_attachment=True)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(401)
def page_not_found(error):
    return render_template('401.html'), 404


@app.errorhandler(Exception)
def handle_500(e):
    original = getattr(e, "original_exception", None)
    app.logger.error('An error occurred', e)
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)
