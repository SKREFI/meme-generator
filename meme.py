import os
from os import getcwd as wd
import random
import argparse

from UtilsQuote.QuoteEngine import Importer
from UtilsQuote.Models import Quote
from UtilsMeme.MemeEngine import MemeGenerator
from Utils.Loging import Log as L

# @TODO Import your Ingestor and MemeEngine classes

meme = MemeGenerator(wd() + '/static/pic.')


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = wd() + "/_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = [wd() + '/_data/DogQuotes/DogQuotes.txt',
                       wd() + '/_data/DogQuotes/DogQuotes.docx',
                       wd() + '/_data/DogQuotes/DogQuotes.pdf',
                       wd() + '/_data/DogQuotes/DogQuotes.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Importer.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = Quote(author, body)

    # I know the signature should look like (path, quote, author, size)
    # Quote insted of author and quote just makes more sense
    # I am parsing it in the function
    # no need to be messy here
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Meme generator')

    parser.add_argument('-p', '--path',
                        help='Path to a image, path \
                        to meme-generator folder already added!',
                        default=None)
    parser.add_argument('-b', '--body', help='Quote body',
                        default=None)
    parser.add_argument('-a', '--author', help='Author\'s name', default=None)

    args = parser.parse_args()

    path = generate_meme(args.path, args.author, args.body)
    print(path)
