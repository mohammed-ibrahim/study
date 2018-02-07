nMaxPages = 2;
var dontKnowStaticValue = "dontknow";


//Color Configuration
var panelDefaultColor = "white";

var colorCodeMapping = {
  a: "mintcream",
  b: "mistyrose",
  c: "aliceblue",
  d: "thistle",
  e: "silver"
}

window.onload = function() {
  if (getParameterByName("sat") == null
  || getParameterByName("crp") == null
  || getParameterByName("nptd") == null) {

    var d = new Date();
    var sat = d.getTime();
    window.location.href = startPage(sat, 1, 0);
    return;
  }

  var currentPageNum = parseInt(getParameterByName("crp"));

  if (currentPageNum > nMaxPages) {
    var sat = getParameterByName("sat");
    var nptd = getParameterByName("nptd");
    var mtfUrl = buildMtfUrl(sat, 1, nptd);
    window.location.href = mtfUrl;
    return;
  }

  getData();
};

function startPage(startAt, pageNum, numPracticed) {
  var url = window.location.protocol + "//" + window.location.host + "/contest/learn"
  + "?sat=" + startAt.toString() + "&crp=" + pageNum.toString() + "&nptd=" + numPracticed.toString();

  return url;
}

function buildMtfUrl(startAt, pageNum, numPracticed) {
  var url = window.location.protocol + "//" + window.location.host + "/contest/mtf"
  + "?sat=" + startAt.toString() + "&crp=" + pageNum.toString() + "&nptd=" + numPracticed.toString();

  return url;
}

function buildLearnUrl(startAt, pageNum, numPracticed) {
  var url = window.location.protocol + "//" + window.location.host + "/contest/learn"
  + "?sat=" + startAt.toString() + "&crp=" + pageNum.toString() + "&nptd=" + numPracticed.toString();

  if (document.getElementById("learn_show_meaning").checked) {
    url = url + "&with_meaning=true";
  }

  return url;
}


function onSubmit() {

  if (!validateResult()) {
    return;
  }

  var sat = getParameterByName("sat");
  var crp = parseInt(getParameterByName("crp")) + 1;
  var nptd = parseInt(getParameterByName("nptd")) + 5;

  window.location.href = buildMtfUrl(sat, crp, nptd);
}

function resetPanels() {
  document.getElementById("mcq_a").checked = false;
  document.getElementById("mcq_b").checked = false;
  document.getElementById("mcq_c").checked = false;
  document.getElementById("mcq_d").checked = false;
}

function getApiUrl() {

  return window.location.protocol + "//" + window.location.host + "/api/contest/mtf";
}

var pageData = {}

function validateResult() {
  var selectionItems = ["a", "b", "c", "d", "e"];
  var lhsTemplate = "mat_td_lhs_lab_";
  var lhsLabelTemplate = "mat_lhs_label_";
  var rhsLabelTemplate = "mat_rhs_label_";

  for (i=0; i<selectionItems.length; i++) {
    var lhsTdId = lhsTemplate + selectionItems[i];
    var currentLhsTdColor = document.getElementById(lhsTdId).style.backgroundColor;
    var itemsOnRhs = getRhsElementsIdsWithColor(currentLhsTdColor);

    if (!itemsOnRhs || itemsOnRhs.length < 1) {

      alert("Please make selection on position: " + selectionItems[i]);
      return false;
    }

    var rhsTdId = itemsOnRhs[0];
    var lastCharOfRhsTdId = rhsTdId[rhsTdId.length - 1];
    // var lastCharOfLhsTdId = lhsTdId[lhsTdId.length - 1];

    console.log("checking for key: " + (lhsLabelTemplate + selectionItems[i]));
    console.log("matching for rhs: " + (rhsLabelTemplate + lastCharOfRhsTdId));
    var matchedKey = document.getElementById(lhsLabelTemplate + selectionItems[i]).innerHTML;
    var matchedValue = document.getElementById(rhsLabelTemplate + lastCharOfRhsTdId).innerHTML;

    var expectedAnswer = pageData["input"][getBuckWalterRepresentation(matchedKey)];

    console.log("expectedAnswer: " + expectedAnswer);
    console.log("selectedAnswer: " + matchedValue);

    if (expectedAnswer !== matchedValue) {

      alert("Wrong answer for: " + selectionItems[i]);
      return false;
    }
  }

  return true;
}

function getData() {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', getApiUrl(), true);

  xhr.onreadystatechange = function() {

    if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
      pageData = JSON.parse(xhr.responseText);
      renderPageData();
    }

    if (xhr.readyState == XMLHttpRequest.DONE && xhr.status != 200) {
      console.error("Api request failed: " + getApiUrl());
    }
  }

  xhr.send();
}

function renderPageData() {

  document.getElementById("mat_lhs_label_a").innerHTML = getArabicRepresentation(pageData["key_order"][0]);
  document.getElementById("mat_rhs_label_a").innerHTML = pageData["value_order"][0];

  document.getElementById("mat_lhs_label_b").innerHTML = getArabicRepresentation(pageData["key_order"][1]);
  document.getElementById("mat_rhs_label_b").innerHTML = pageData["value_order"][1];

  document.getElementById("mat_lhs_label_c").innerHTML = getArabicRepresentation(pageData["key_order"][2]);
  document.getElementById("mat_rhs_label_c").innerHTML = pageData["value_order"][2];

  document.getElementById("mat_lhs_label_d").innerHTML = getArabicRepresentation(pageData["key_order"][3]);
  document.getElementById("mat_rhs_label_d").innerHTML = pageData["value_order"][3];

  document.getElementById("mat_lhs_label_e").innerHTML = getArabicRepresentation(pageData["key_order"][4]);
  document.getElementById("mat_rhs_label_e").innerHTML = pageData["value_order"][4];
}

function markLastSelection(element) {
  var currentColor = document.getElementById(element.id).style.backgroundColor;

  document.getElementById("last_lhs_selection_id_holder").value = element.id;

  var lastSelection = element.id;
  var lastChar = lastSelection[lastSelection.length - 1];
  document.getElementById(element.id).style.backgroundColor = colorCodeMapping[lastChar];
}

function getRhsElementsIdsWithColor(color) {
  var rhsElements = Array();

  if ((!color) || color === panelDefaultColor) {

    return rhsElements;
  }

  var itemsToCheck = ["a", "b", "c", "d", "e"];

  for (var i=0; i<itemsToCheck.length; i++) {

    var keyVar = itemsToCheck[i];
    var fullKey = "mat_td_rhs_lab_" + keyVar;

    if (document.getElementById(fullKey).style.backgroundColor === color) {

      rhsElements.push(fullKey);
    }
  }

  return rhsElements;
}

function matchLastSelection(element) {

  var lastSelection = document.getElementById("last_lhs_selection_id_holder").value;

  if ((!lastSelection) || (lastSelection === dontKnowStaticValue)) {
    return;
  }

  var lastChar = lastSelection[lastSelection.length - 1];
  document.getElementById(element.id).style.backgroundColor = colorCodeMapping[lastChar];

  var otherElementsWithSameColor = getRhsElementsIdsWithColor(colorCodeMapping[lastChar]);
  document.getElementById("last_lhs_selection_id_holder").value = dontKnowStaticValue;
  if (!otherElementsWithSameColor) {

    return;
  }

  var thisElementId = element.id;
  for (var i=0; i<otherElementsWithSameColor.length; i++) {

    var otherElementId = otherElementsWithSameColor[i];

    if (thisElementId !== otherElementId) {

      document.getElementById(otherElementId).style.backgroundColor = panelDefaultColor;
    }
  }
}

function resetSelections() {

  var itemsToCheck = ["a", "b", "c", "d", "e"];

  for (var i=0; i<itemsToCheck.length; i++) {

    var keyVar = itemsToCheck[i];
    document.getElementById("mat_td_lhs_lab_" + keyVar).style.backgroundColor = panelDefaultColor;
    document.getElementById("mat_td_rhs_lab_" + keyVar).style.backgroundColor = panelDefaultColor;
  }

  document.getElementById("last_lhs_selection_id_holder").value = dontKnowStaticValue;
}
