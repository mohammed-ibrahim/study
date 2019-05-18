
function encode_utf8( s ) {
    return unescape( encodeURIComponent( s ) );
}

function decode_utf8( s ) {
    return decodeURIComponent(  s  );
    //return s;
}

//DefaultMap
var global_BwMapping_BwToArabicMap = {
    "A": "ا",
    "b": "ب",
    "t": "ت",
    "v": "ث",
    "j": "ج",
    "H": "ح",
    "x": "خ",
    "d": "د",
    "*": "ذ",
    "r": "ر",
    "z": "ز",
    "s": "س",
    "$": "ش",
    "S": "ص",
    "D": "ض",
    "T": "ط",
    "Z": "ظ",
    "E": "ع",
    "g": "غ",
    "f": "ف",
    "q": "ق",
    "k": "ك",
    "l": "ل",
    "m": "م",
    "n": "ن",
    "h": "ه",
    "w": "و",
    "y": "ي",
    "p": "ة", //teh marbuta

    "a": '\u064E', // fatha
    "u": '\u064f', // damma
    "i": '\u0650', // kasra
    "F": '\u064B', // fathatayn
    "N": '\u064C', // dammatayn
    "K": '\u064D', // kasratayn
    "~": '\u0651', // shadda
    "o": '\u0652', // sukun

    "'": '\u0621', // lone hamza
    ">": '\u0623', // hamza on alif
    "<": '\u0625', // hamza below alif
    "&": '\u0624', // hamza on wa
    "}": '\u0626', // hamza on ya

    "|": '\u0622', // madda on alif
    "{": '\u0671', // alif al-wasla
    "`": '\u0670', // dagger alif
    "Y": '\u0649', // alif maqsura

    " ": " ",
    ".": "."
};


function swap(json){

    var ret = {};

    for(var key in json){
        ret[json[key]] = key;
    }

    return ret;
}

var global_BwMapping_ArabicToBwMap = swap(global_BwMapping_BwToArabicMap);

function getArabicToBwMap() {

    return global_BwMapping_ArabicToBwMap;
}


function getBuckWalterRepresentation(arabicData) {
    var transliteration = "";

    for (var i=0;i<arabicData.length;i++) {
        transliteration = transliteration + global_BwMapping_ArabicToBwMap[arabicData[i]];
    }

    return transliteration;
}

function getArabicRepresentation(bwData) {

    var transliteration = "";

    for (var i=0;i<bwData.length;i++) {
        transliteration = transliteration + global_BwMapping_BwToArabicMap[bwData[i]];
    }

    return transliteration;
}
