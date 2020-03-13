from abc import ABC, abstractmethod
from typing import List
import pandas
import docx
import subprocess
import random
import os
from os import getcwd as wd


from Utils.Models import Quote
from Utils.Loging import Log as L


class IngestorInterface(ABC):
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return path.split('.')[-1] in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[Quote]:
        pass


class TXTImporter(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        quotes = []
        with open(path, 'r', encoding='utf-8-sig') as f:
            for line in f.readlines():
                line = line.strip()
                if len(line) > 0:
                    line = line.split(' - ')
                    quotes.append(Quote(line[0].strip('"'), line[1]))
        return quotes


class CSVImporter(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        quotes = []
        f = pandas.read_csv(path, header=0)
        for _, row in f.iterrows():
            quotes.append(Quote(row['body'], row['author']))
        return quotes


class DOCXImporter(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        quotes = []
        doc = docx.Document(path)
        for p in doc.paragraphs:
            if p.text != '':
                inp = p.text.split(' - ')
                quotes.append(Quote(inp[1].strip(), inp[0].strip('"')))
        return quotes


class PDFImporter(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        tmp = f'{wd()}/tmp/{random.randint(10000,99999)}.txt'
        tmp_file = open(tmp, 'w+')
        tmp_file.close()
        subprocess.call(['touch', tmp])
        call = subprocess.call(['pdftotext', path, tmp])
        quotes = TXTImporter.parse(tmp)
        os.remove(tmp)
        return quotes
    allowed_extensions = ['pdf']


class Importer(IngestorInterface):
    allowed_extensions = ['pdf', 'docx', 'csv', 'txt']

    importers = {
        'pdf': PDFImporter,
        'docx': DOCXImporter,
        'csv': CSVImporter,
        'txt': TXTImporter
    }

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        if not cls.can_ingest(path):
            raise Exception(f'Can\'t ingest extension')
        return cls.importers.get(path.split('.')[-1]).parse(path)


if __name__ == '__main__':
    quotes = Importer.parse(wd() + '/_data/DogQuotes/DogQuotes.txt')

    [print(x) for x in quotes]
