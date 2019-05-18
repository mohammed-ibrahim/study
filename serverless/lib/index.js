
var languagesWithDirRtl = [ "ar", "ur" ];

function loadScript(rnum) {

    var srcName = "content_" + rnum + ".js";
    var script = document.createElement('script');
    script.src = srcName;
    document.head.appendChild(script);

    script.onload = function() {
        console.log("Successfully loaded: " + srcName);
    }
}

window.onload = function() {

    setSurahSelectBox();
    dyload(1);

}

function dyload(surahNumber) {
    console.log("Loading surahNumber: " + surahNumber);
    var rukuNumber = metadata[surahNumber]["ruku"][0]["ruku_index"];
    setRukuSelectBox(surahNumber);
    dyloadRukuNumber(rukuNumber);
}

function dyloadRukuNumber(rukuNumber) {
    var script = document.createElement('script');
    script.src = "content/r-" + rukuNumber.toString() + ".js";
    document.head.appendChild(script);

    script.onload = function() {
        render();
    }
}

function render() {

    var firstAyahNumber = rukuContent["aayaah"][0]["ayah_number"];
    setAyahSelectBox();
    renderArabicContent(firstAyahNumber);
    renderTranslation(firstAyahNumber);
    renderRootDetails(firstAyahNumber);
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
        var surahName = metadata[surahNumber]["name"];
        text = text + selectTemplate.replace("__option_value_place_holder__", surahNumber)
                .replace("__option_text_place_holder__", getNumberInArabic(surahNumber) + " - " + surahName);
    }

    document.getElementById("surah_selection").innerHTML = text;
    //document.getElementById("surah_selection").value = rukuContent["surah_number"];
}


function setRukuSelectBox(currentSurahNumber) {
    var text = "";

    for (var index in metadata[currentSurahNumber]["ruku"]) {
        var rukuDetails = metadata[currentSurahNumber]["ruku"][index];
        var rukuNumberInSurah = parseInt(index) + 1;
        var rukuIndex = rukuDetails["ruku_index"];
        text = text + selectTemplate.replace("__option_value_place_holder__", rukuIndex)
                .replace("__option_text_place_holder__", getNumberInArabic(rukuNumberInSurah));
    }

    document.getElementById("ruku_selection").innerHTML = text;
    document.getElementById("ruku_selection").value = metadata[currentSurahNumber]["ruku"][0]["ruku_index"];
}

function setAyahSelectBox() {
    var text = "";

    for (var index in rukuContent["ayah_number_sequence"]) {
        var value = rukuContent["ayah_number_sequence"][index];
        var ayahNumberInArabic = getNumberInArabic(value.split(":")[1]);
        text = text + selectTemplate.replace("__option_value_place_holder__", value)
            .replace("__option_text_place_holder__", ayahNumberInArabic);
    }

    document.getElementById("ayah_selection").innerHTML = text;
    document.getElementById("ayah_selection").value = rukuContent["ayah_number_sequence"][0];
}


var arabicContentDivTemplate = `
                        <div class="arabic" dir="rtl" id="__arabic_content_id_holder__" onclick="selectAyah('__onclick_param_place_holder__')">__arabic_content_div__</div>
`;
function renderArabicContent(ayahNumber) {
    var text = "";

    var start = rukuContent.ayah_number_sequence.indexOf(ayahNumber) - 1;

    if (start < 0) {

        start = 0;
    }

    for (var i=start; i< rukuContent["aayaah"].length; i++) {

        var ayahNumber = rukuContent["aayaah"][i]["ayah_number"].split(":")[1];
        var ayahText = rukuContent["aayaah"][i]["arabic_content"]["uthmani"] + " (" + getNumberInArabic(ayahNumber) + ")";
        var fullSurahAndAyahNumber = rukuContent["aayaah"][i]["ayah_number"];

        text = text + arabicContentDivTemplate.replace("__onclick_param_place_holder__", fullSurahAndAyahNumber)
            .replace("__arabic_content_div__", ayahText)
            .replace("__arabic_content_id_holder__", fullSurahAndAyahNumber);
    }

    document.getElementById("arabic_content").innerHTML = text;
}



var translationContentDiv = `
        <div dir="__dir_place_holder__">__translation_content_place_holder__</div>
`;

var authorContentTemplate = `
                        <br/><label class="author_font">__author_text_place_holder__</label><br/><br/>
`;


function renderTranslation(ayahNumber) {
    var indexOfAyah = rukuContent["ayah_number_sequence"].indexOf(ayahNumber);
    var text = "";

    for (var index in rukuContent["translation_sequence"]) {
        var translationKey = rukuContent["translation_sequence"][index];

        var translationContent = rukuContent["aayaah"][indexOfAyah]["translations"][translationKey]["ayah_translation"];
        var authorName = rukuContent["aayaah"][indexOfAyah]["translations"][translationKey]["author"];
        var language = rukuContent["aayaah"][indexOfAyah]["translations"][translationKey]["language"];

        var dir = "";
        if (languagesWithDirRtl.includes(language)) {
            dir = "rtl";
        } else {
            dir = "ltr";
        }

        text = text + authorContentTemplate.replace("__author_text_place_holder__", authorName);
        text = text + translationContentDiv.replace("__translation_content_place_holder__", translationContent)
            .replace("__dir_place_holder__", dir);
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

    var indexOfAyah = rukuContent["ayah_number_sequence"].indexOf(ayahNumber);
    var text = "";

    for (var index in rukuContent["aayaah"][indexOfAyah]["detailed_root_sequence"]) {
        var detailedRoot = rukuContent["aayaah"][indexOfAyah]["detailed_root_sequence"][index];

        var root = detailedRoot["bw_root"];
        var rootStatistics = detailedRoot['statistics']['num_of_occurrence'].toString() + ":"
            + detailedRoot['statistics']['appears_number_of_surah'].toString();

        var englishMeaning = detailedRoot["english-meaning"];
        var urduMeaning = detailedRoot["urdu-meaning"];

        var meaningToDisplay = urduMeaning + "<br/>----<br/>" + englishMeaning;

        text = text + rootDataTemplate.replace("__root_word__", getArabicRepresentation(root))
            .replace("__root_stats__", rootStatistics)
            .replace("__root_meaning__", meaningToDisplay);
    }

    document.getElementById("roots_table").innerHTML = text;
}
