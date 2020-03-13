class Quote():
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote

    def __repr__(self):
        return f'{self.author} -> {self.quote}'
