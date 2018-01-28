

transliteration_to_bw_map = {
    'Alif': 'A',
    'hamza': 'A',
    'Ayn':  'E',
    'Ba': 'b',
    'Dad': 'D',
    'Daad': 'D',
    'Dal': 'd',
    'dal': 'd',
    'Fa': 'f',
    'Gh': 'g',
    'Ghayn': 'g',
    'ha': 'h',
    'Ha': 'H',
    'Haa': 'H',
    'Jiim': 'j',
    'Kaf': 'k',
    'Kha': 'x',
    'Kh': 'x',
    'Lam': 'l',
    'La': 'l',
    'Miim': 'm',
    'Meem': 'm',
    'Nun': 'n',
    'Qaf': 'q',
    'Ra': 'r',
    'Sad': 'S',
    'Saad': 'S',
    'Sh': '$',
    'Shiin': '$',
    'Siin': 's',
    'Ta': 't',
    'Tay': 'T',
    'Tha': 'v',
    'Thaa': 'v',
    'Thal': '*',
    'Dhal': '*',
    'Waw': 'w',
    'Ya': 'y',
    'Za': 'Z',
    'Zay': 'z'
}

with open('../content/original/Root_d.txt', 'r') as in_file:
    with open('dictionary.v2.txt', 'w') as out_file:
        line = in_file.readline()

        while line:
            parts = line.split(' =')
            key = parts[0].split(' ')[0]
            meaning = ''
            if len(parts) > 1:
                meaning = parts[1]

            transliterated_key_list = key.split("-")
            new_key = ''

            for transliterated_key in transliterated_key_list:
                new_key = new_key + transliteration_to_bw_map[transliterated_key.strip()]

            out_file.write(new_key + "|" + meaning.strip() + "\n");
            line = in_file.readline()
