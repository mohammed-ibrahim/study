from src.utils import reader_util
from src.content.translation import Translation
#  import load_from_file, load_json_from_file, load_kvp_from_file

class AppData:
    arabic = reader_util.load_from_file("content/arabic/quran-uthmani.txt", "ar")

    translation_yusuf_ali = Translation("Yusuf Ali", "en", "content/translations/en.yusufali.txt")
    translation_shakir = Translation("Shakir", "en", "content/translations/en.shakir.txt")
    translation_maulana_maududi = Translation("Maulana Maududi", "ur", "content/translations/ur.maududi.txt")
    translation_maulana_jalandhry = Translation("Maulana Jalandhry", "ur", "content/translations/ur.jalandhry.txt")

    surah_metadata = reader_util.load_json_from_file("content/metadata/surah_metadata.json")
    ruku_to_surah_mapping = reader_util.load_json_from_file("content/metadata/ruku_to_surah_mapping.json")
    verse_number_to_root_sequence_mapping = reader_util.load_json_from_file("content/metadata/verse_number_to_root_sequence_mapping.json")
    root_statistics = reader_util.load_json_from_file("content/metadata/root_statistics.json")

    # english_meaning = reader_util.load_kvp_from_file("content/translations/english-meaning-v2.txt")
    root_meaning = reader_util.load_root_meaning("content/translations/root-meaning-v2.csv")

    translation_sequence = [
        "translation_maulana_jalandhry",
        "translation_maulana_maududi",
        "translation_yusuf_ali",
        "translation_shakir"
    ]

    def get_surah_and_ruku_metadata(self, ruku_number):
        ruku_number_str = str(ruku_number)

        if ruku_number_str not in self.ruku_to_surah_mapping:
            raise Exception('Ruku number: ' + ruku_number_str + ' is not available')

        surah_number = self.ruku_to_surah_mapping[ruku_number_str]["surah_number"]
        ruku_number_of_surah = int(self.ruku_to_surah_mapping[ruku_number_str]["ruku_number_of_surah"])
        surah_data = self.surah_metadata[surah_number]

        if surah_data is None:
            raise Exception('Surah number: ' + surah_number + ' is not available')

        ruku_index_in_surah = ruku_number_of_surah - 1
        ruku_data = surah_data["ruku"][ruku_index_in_surah]

        if ruku_data is None:
            raise Exception('Not able to fetch ruku by ruku index: ' + str(ruku_index_in_surah))

        return {
            "surah_data": surah_data,
            "ruku_data": ruku_data,
            "current_ruku_in_surah": ruku_index_in_surah,
            "surah_number": surah_number
        }
