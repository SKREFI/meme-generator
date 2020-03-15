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
    def split_text(cls, text, chars):
        words = text.split(' ')
        new_quote = ''
        c = chars
        rows = 1
        for word in words:
            if len(word) < c - 6:
                new_quote += word + ' '
                c -= len(word) + 1
            else:
                rows += 1
                new_quote += '\n' + word + ' '
                c = chars
        return new_quote, rows

    @classmethod
    def place_text(cls, im: Image, quote, author):
        '''
        Place text on a random position on the image
        '''
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(
            'Pillow/Tests/fonts/FreeMono.ttf', im.size[0]//17)

        chars = im.size[0]//18
        quote, quote_r = cls.split_text(quote, chars)
        author,  author_r = cls.split_text(author, chars)
        rows = quote_r + author_r

        try:
            print('Debug:', len(quote))
            randomPosition = (0, getRandom(
                0, im.size[1] - im.size[0]//17 * rows))
            draw.text(randomPosition, quote + '\n- ' +
                      author, (255, 255, 255), font)
        except:
            # random.randint() is helping me right here, since
            # I am calculating the space my calculating space this way:
            # height (500px) - ~30px (500/17) * rows (author + body)
            # and randint() will fail if the interval is (0, negative)
            raise Exception('Text too long for the image,\
                             it doesn\'t fit in the image')

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
        print(save_path)
        im = self.place_text(im, quote, author)
        im.save(save_path)
        return 'static/pic.' + \
            path.split('/')[-1].split('.')[1]


if __name__ == '__main__':
    meme = MemeGenerator(wd() + '/static/pic.')
    img = wd() + "/_data/photos/dog/xander_4.jpg"
    # print(meme.make_meme(img, 'This is small', "Me_SKREF"))
    print(meme.make_meme(
          img, 'This is supposed to be a medium quote size', "Me_SKREF"))
