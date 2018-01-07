var pageStateSurahMetaData = null;
var pageStateRukuData = null;

window.onload = function() {

    if (getParameterByName("test")) {
        return;
    }

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
    if (!pageStateRukuData) {

        return;
    }

    // Set/Select Surah Select box
    setSurahSelectBox();
    // Set/Select Ruku Select box
    setRukuSelectBox(rukuNumber);
    // Set/Select Ayah Select Box
    setAyahSelectBox();
    // Set arabic content
    var firstAyahNumber = pageStateRukuData["aayaah"][0]["ayah_number"];
    renderArabicContent(firstAyahNumber);
    // Set translation
    renderTranslation(firstAyahNumber);
    // Set root details
    renderRootDetails(firstAyahNumber);
    // Hilight first Ayah.
    markSelectedAyah(firstAyahNumber);
}

function selectAyah(ayahNumber) {
    renderArabicContent(ayahNumber);
    renderTranslation(ayahNumber);
    renderRootDetails(ayahNumber);
    markSelectedAyah(ayahNumber);
    document.getElementById("ayah_selection").value = ayahNumber;
}

var currentAyahSelection = null;

function markSelectedAyah(ayahNumber) {
    var selectedFontColor = "LightSeaGreen";
    var defaultFontColor = "Black";

    if (!currentAyahSelection) {
        document.getElementById(ayahNumber).style.color = selectedFontColor;
        currentAyahSelection = ayahNumber;
    } else {

        if (document.getElementById(currentAyahSelection)) {
            document.getElementById(currentAyahSelection).style.color = defaultFontColor;
        }
        document.getElementById(ayahNumber).style.color = selectedFontColor;
        currentAyahSelection = ayahNumber;
    }
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

function setRukuSelectBox(rukuNumber) {
    var currentSurahNumber = pageStateRukuData["surah_number"];
    var text = "";

    for (var index in pageStateSurahMetaData[currentSurahNumber]["ruku"]) {
        var rukuDetails = pageStateSurahMetaData[currentSurahNumber]["ruku"][index];
        var rukuNumberInSurah = parseInt(index) + 1;
        var rukuIndex = rukuDetails["ruku_index"];
        text = text + selectTemplate.replace("__option_value_place_holder__", rukuIndex)
                .replace("__option_text_place_holder__", getNumberInArabic(rukuNumberInSurah));
    }

    document.getElementById("ruku_selection").innerHTML = text;
    document.getElementById("ruku_selection").value = rukuNumber.toString();
}

function setAyahSelectBox(rukuNumber) {
    var text = "";

    for (var index in pageStateRukuData["ayah_number_sequence"]) {
        var value = pageStateRukuData["ayah_number_sequence"][index];
        var ayahNumberInArabic = getNumberInArabic(value.split(":")[1]);
        text = text + selectTemplate.replace("__option_value_place_holder__", value)
            .replace("__option_text_place_holder__", ayahNumberInArabic);
    }

    document.getElementById("ayah_selection").innerHTML = text;
    document.getElementById("ayah_selection").value = pageStateRukuData["ayah_number_sequence"][0];
}

var arabicContentDivTemplate = `
                        <div class="arabic" dir="rtl" id="__arabic_content_id_holder__" onclick="selectAyah('__onclick_param_place_holder__')">__arabic_content_div__</div>
`;
function renderArabicContent(ayahNumber) {
    var text = "";

    var start = pageStateRukuData.ayah_number_sequence.indexOf(ayahNumber) - 1;

    if (start < 0) {

        start = 0;
    }

    for (var i=start; i< pageStateRukuData["aayaah"].length; i++) {

        var ayahNumber = pageStateRukuData["aayaah"][i]["ayah_number"].split(":")[1];
        var ayahText = pageStateRukuData["aayaah"][i]["arabic_content"]["uthmani"] + " (" + getNumberInArabic(ayahNumber) + ")";
        var fullSurahAndAyahNumber = pageStateRukuData["aayaah"][i]["ayah_number"];

        text = text + arabicContentDivTemplate.replace("__onclick_param_place_holder__", fullSurahAndAyahNumber)
            .replace("__arabic_content_div__", ayahText)
            .replace("__arabic_content_id_holder__", fullSurahAndAyahNumber);
    }

    document.getElementById("arabic_content").innerHTML = text;
}

var translationContentDiv = `
        <div>__translation_content_place_holder__</div>
`;

var authorContentTemplate = `
                        <br/><label class="author_font">__author_text_place_holder__</label><br/><br/>
`;

function renderTranslation(ayahNumber) {
    var indexOfAyah = pageStateRukuData["ayah_number_sequence"].indexOf(ayahNumber);
    var text = "";

    for (var index in pageStateRukuData["translation_sequence"]) {
        var translationKey = pageStateRukuData["translation_sequence"][index];
        var translationContent = pageStateRukuData["aayaah"][indexOfAyah]["translations"][translationKey]["ayah_translation"];
        var authorName = pageStateRukuData["aayaah"][indexOfAyah]["translations"][translationKey]["author"];
        text = text + authorContentTemplate.replace("__author_text_place_holder__", authorName);
        text = text + translationContentDiv.replace("__translation_content_place_holder__", translationContent);
    }

    document.getElementById("translation_content").innerHTML = text;
}

var rootDataTemplate = `
                            <tr>
                                <td class="roots_td_info">
                                    __root_word__
                                    <br/>
                                    __root_stats__
                                </td>
                                <td class="roots_td_meaning">
                                    __root_meaning__
                                </td>
                            </tr>
`;

function renderRootDetails(ayahNumber) {
    var indexOfAyah = pageStateRukuData["ayah_number_sequence"].indexOf(ayahNumber);
    var text = "";

    for (var index in pageStateRukuData["aayaah"][indexOfAyah]["root_sequence"]) {
        var root = pageStateRukuData["aayaah"][indexOfAyah]["root_sequence"][index];
        var rootStatistics = pageStateRukuData["root_details"][root]["statistics"]["num_of_occurrence"] + ":"
            + pageStateRukuData["root_details"][root]["statistics"]["appears_number_of_surah"];
        var englishMeaning = pageStateRukuData["root_details"][root]["english-meaning"];

        text = text + rootDataTemplate.replace("__root_word__", getArabicRepresentation(root))
            .replace("__root_stats__", rootStatistics)
            .replace("__root_meaning__", englishMeaning);
    }

    document.getElementById("roots_table").innerHTML = text;
}
