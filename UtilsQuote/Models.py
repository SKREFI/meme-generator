class Quote():
    def __init__(self, body, author):
        self.author = author
        self.body = body

    def __repr__(self):
        return f'{self.author} -> {self.quote}'
