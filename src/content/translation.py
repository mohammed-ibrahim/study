from src.utils import reader_util

class Translation:
    author = None
    language = ""
    content_map = {}
    def __init__(self, author, language, file_name):
        self.author = author
        self.language = language
        self.content_map = reader_util.load_from_file(file_name, self.language)

    def get_ayah(self, ayah_number):
        return self.content_map[ayah_number]

    def get_ayah_and_details(self, ayah_number):
        return {
            "author": self.author,
            "ayah_translation": self.content_map[str(ayah_number)],
            "language": self.language
        }
