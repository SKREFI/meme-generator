from PIL import Image, ImageDraw, ImageFont
from os import getcwd as wd
from random import randint as getRandom

from Utils.Models import Quote
from Utils.Loging import Log as L


class MemeGenerator():

    @classmethod
    def load_image(cls, path: str, size: int) -> Image:
        '''
        Load and return croped image if bigger then 500 px
        '''
        im = Image.open(path)
        width, height = im.size
        if width > size or height > size:
            resize = size, size
            im.thumbnail(resize)
        return im

    @classmethod
    def place_text(cls, im: Image, quote: Quote, size: int):
        '''
        Place text on a random position on the image
        '''
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(
            'Pillow/Tests/fonts/FreeMono.ttf', 30)
        max_x = im.size[0]
        max_x = (size - len(quote)//2 * 18)
        # Edit, I tried, I leave the text start at the begginging of the picture
        # I am trying to calculate the maxim X for the START of the text, for one or 2 rows
        if len(quote) > max_x/18:
            quote = quote.split(' ')
            quote = ' '.join(quote[:len(quote)//2]) + \
                '\n' + ' '.join(quote[len(quote)//2:])
            max_x /= 2
        randomPosition = (0, getRandom(0, size))
        draw.text(randomPosition, quote, (255, 255, 255), font)
        return im

    @classmethod
    def make_meme(cls, path: str, q: Quote, size: int = 500) -> str:
        quote = q.quote + ' - ' + q.author
        im = cls.load_image(path, size)
        # this may seem complex but I am only geting the path + img name + edited + image extension
        # save_path = wd() + '/_data/photos/tmp/' + \
        #     path.split('/')[-1].split('.')[0] + '_edited' + \
        #     '.' + path.split('/')[-1].split('.')[1]

        # save_path = wd() + '/_data/photos/tmp/tmp_edited.png'
        save_path = wd() + '/static/pic.' + \
            path.split('/')[-1].split('.')[1]

        im = cls.place_text(im, quote, size)
        im.save(save_path)
        return 'static/pic.' + \
            path.split('/')[-1].split('.')[1]


if __name__ == '__main__':
    pass
