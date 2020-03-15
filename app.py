import random
import os
from os import getcwd as wd
import requests
from flask import Flask, flash, render_template, \
    redirect, url_for, abort, request
from werkzeug.utils import secure_filename
from PIL import Image


from Utils.Loging import Log as L
from UtilsQuote.Models import Quote
from UtilsQuote.QuoteEngine import Importer
from UtilsMeme.MemeEngine import MemeGenerator

app = Flask(__name__, static_url_path='/static')
app.config["CACHE_TYPE"] = "null"

meme = MemeGenerator(wd() + '/static/pic.')


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
    quote = random.choice(quotes)
    img = random.choice(imgs)
    L.fail(img)
    path = meme.make_meme(img, quote.body, quote.author)

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
    try:
        r = requests.get(image_url)
    except:
        L.fail('IMAGE URL NOT PROVIDED, using default')
        image_url = 'https://i.imgur.com/NArhr29.jpg'
        r = requests.get(image_url)
    extension = image_url.split('.')[-1]
    path = f'{wd()}/static/tmp.' + extension
    img = open(path, 'wb').write(r.content)

    edited_path = meme.make_meme(path, body, author)
    os.remove(path)

    return render_template('meme.html', path=edited_path)


if __name__ == "__main__":
    app.run(debug=True)
