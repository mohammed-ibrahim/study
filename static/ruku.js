var pageStateSurahMetaData = {}
var pageStateRukuData = {}

window.onload = function() {
    var lastPartOfUrl = getLastPartOfUrl();
    var num = parseInt(lastPartOfUrl);

    if (!isNaN(num)) {
        var rukuNumber = num;
        makeMetadataRequest(rukuNumber);
    } else {
        console.log("lastPartOfUrl is not parseable as int: " + lastPartOfUrl);
    }
}

function getLastPartOfUrl() {
    var url = window.location.href;
    return url.substr(url.lastIndexOf('/') + 1);
}

function getMetadataApiUrl() {

    return window.location.protocol + "//" + window.location.host + "/api/surah/metadata";
}

function makeMetadataRequest(rukuNumber) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', getMetadataApiUrl(), true);

    xhr.onreadystatechange = function() {

        if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
            pageStateSurahMetaData = JSON.parse(xhr.responseText);
            makeRukuDataRequest(rukuNumber);
        }

        if (xhr.readyState == XMLHttpRequest.DONE && xhr.status != 200) {
            console.error("Api request failed: " + getMetadataApiUrl());
        }
    }

    xhr.send();
}

function getRukuDataApiUrl(rukuNumber) {

    return window.location.protocol + "//" + window.location.host + "/api/ruku/" + rukuNumber.toString();
}

function makeRukuDataRequest(rukuNumber) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', getRukuDataApiUrl(rukuNumber), true);

    xhr.onreadystatechange = function() {

        if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
            pageStateRukuData = JSON.parse(xhr.responseText);
            render(rukuNumber);
        }

        if (xhr.readyState == XMLHttpRequest.DONE && xhr.status != 200) {
            console.error("Api request failed: " + getRukuDataApiUrl(rukuNumber));
        }
    }

    xhr.send();
}

function render(rukuNumber) {

    //1: Set/Select Surah Select box
    setSurahSelectBox();
    //2: Set/Select Ruku Select box
    //3: Set arabic content
    //4: Set translation
    //5: Set root details
}

var selectTemplate = `
        <option value="__option_value_place_holder__">__option_text_place_holder__</option>
`;

function setSurahSelectBox() {
    var text = "";

    for (var i=1; i<=114; i++) {
        var key = i.toString();
        var surahNumber = key;
        var surahName = pageStateSurahMetaData[surahNumber]["name"];
        text = text + selectTemplate.replace("__option_value_place_holder__", surahNumber)
                .replace("__option_text_place_holder__", getNumberInArabic(surahNumber) + " - " + surahName);
    }

    document.getElementById("surah_selection").innerHTML = text;
    document.getElementById("surah_selection").value = pageStateRukuData["surah_number"];
}
