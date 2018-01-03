
def get_ruku_content(app_data, ruku_number):
    result = app_data.get_surah_and_ruku_metadata(ruku_number)
    surah_data = result["surah_data"];
    ruku_data = result["ruku_data"];

    data = {
        "surah_name": surah_data["name"],
        "surah_number": result["surah_number"],
        "ruku_number": ruku_number,
        "current_ruku_in_surah": result["current_ruku_in_surah"],
        "number_of_ruku_in_surah": len(surah_data["ruku"]),
        "next_ruku_number": "PENDING",
        "juz_number": "PENDING",
        "previous_ruku_number": "PENDING",
        "ayah_number_sequence": ruku_data["aayaah_in_ruku"]
    }
    return data
