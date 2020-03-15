from PIL import Image, ImageDraw, ImageFont
from os import getcwd as wd
from random import randint as getRandom


class MemeGenerator():

    def __init__(self, path):
        self.path = path

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
    def place_text(cls, im: Image, quote, author, size: int):
        '''
        Place text on a random position on the image
        '''
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(
            'Pillow/Tests/fonts/FreeMono.ttf', 30)

        chars = im.size[0]//18
        quote = quote.split(' ')
        new_quote = ''
        rows = 1
        for word in quote:
            if len(word) < chars:
                new_quote += word + ' '
                chars -= len(word) + 1
            else:
                rows += 1
                new_quote += '\n' + word + ' '
                chars = im.size[0]//18
        randomPosition = (0, getRandom(0, im.size[1] - 50 * rows))
        draw.text(randomPosition, new_quote + '\n- ' +
                  author, (255, 255, 255), font)
        return im

    def make_meme(self, path, quote, author, size=500) -> str:
        '''
        Place text of choice on a picture of choice
        OR Place some random text on a random pic
        from the database
        @param path: path to the picture
        @param quote: str
        @param author: str
        '''
        im = self.load_image(path, size)
        extension = path.split('/')[-1].split('.')[1]
        save_path = self.path + extension

        im = self.place_text(im, quote, author, size)
        im.save(save_path)
        return 'static/pic.' + \
            path.split('/')[-1].split('.')[1]


if __name__ == '__main__':
    meme = MemeGenerator(wd() + '/static/pic.')
    img = wd() + "/_data/photos/dog/xander_4.jpg"
    # print(meme.make_meme(img, 'This is small', "Me_SKREF"))
    print(meme.make_meme(
          img, 'This is supposed to be a medium to large quote size',
          "Me_SKREF"))
