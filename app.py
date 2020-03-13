import random
import os
from os import getcwd as wd
import requests
from flask import Flask, flash, render_template, redirect, url_for, abort, request
from werkzeug.utils import secure_filename
from PIL import Image


from Utils.Loging import Log as L
from Utils.Models import Quote
from Utils.QuoteEngine import Importer
from Utils.MemeEngine import MemeGenerator

app = Flask(__name__, static_url_path='/static')
app.config["CACHE_TYPE"] = "null"


def setup():
    """ Load all resources """

    quote_files = [wd() + '/_data/DogQuotes/DogQuotes.txt',
                   wd() + '/_data/DogQuotes/DogQuotes.docx',
                   wd() + '/_data/DogQuotes/DogQuotes.pdf',
                   wd() + '/_data/DogQuotes/DogQuotes.csv']

    quotes = []
    for X in [Importer.parse(file) for file in quote_files]:
        for q in X:
            quotes.append(q)

    images_path = wd() + "/_data/photos/dog/"

    imgs = [wd() + '/_data/photos/dog/' + pic
            for pic in os.listdir(images_path)]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/', methods=['GET', 'POST'])
def meme_rand():
    """ Generate a random meme """
    path = MemeGenerator.make_meme(random.choice(imgs), random.choice(quotes))

    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """

    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    image_url = request.form.get('image_url')
    body = request.form.get('body', 'Default body')
    author = request.form.get('author', 'SKREFI')

    extension = image_url.split('.')[-1]

    r = requests.get(image_url)
    path = f'{wd()}/static/tmp.' + extension
    img = open(path, 'wb').write(r.content)

    edited_path = MemeGenerator.make_meme(path, Quote(author, body))
    os.remove(path)
    L.warning(edited_path)

    return render_template('meme.html', path=edited_path)


if __name__ == "__main__":
    app.run(debug=True)

