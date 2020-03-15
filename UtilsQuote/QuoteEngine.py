from UtilsQuote.Ingestors import *


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
