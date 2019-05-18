
function swap(json){

    var ret = {};

    for(var key in json){
        ret[json[key]] = key;
    }

    return ret;
}

var arabicToEnglishNumbers = {"٠":"0","١":"1","٢":"2","٣":"3","٤":"4","٥":"5","٦":"6","٧":"7","٨":"8","٩":"9"};
var englishToArabicNumbers = swap(arabicToEnglishNumbers);

function getNumberInArabic(englishNumber) {
    var engNumberStr = englishNumber.toString();
    var arabicNumberStr = "";

    for (var i in engNumberStr) {
        var enChar = engNumberStr[i];
        arabicNumberStr = arabicNumberStr + englishToArabicNumbers[enChar];
    }

    return arabicNumberStr;
}
