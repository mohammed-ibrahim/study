nMaxPages = 2;

window.onload = function() {

  if (getParameterByName("sat") == null
  || getParameterByName("crp") == null
  || getParameterByName("nptd") == null) {

    var d = new Date();
    var sat = d.getTime();
    window.location.href = buildLearnUrl(sat, 1, 0);
    return;
  }

  var currentPageNum = parseInt(getParameterByName("crp"));

  if (currentPageNum > nMaxPages) {
    var sat = getParameterByName("sat");
    var nptd = getParameterByName("nptd");
    var mcqUrl = buildMcqUrl(sat, 1, nptd);
    window.location.href = mcqUrl;
    return;
  }

  getData();
};

function buildLearnUrl(startAt, pageNum, numPracticed) {
  var url = window.location.protocol + "//" + window.location.host + "/contest/learn"
  + "?sat=" + startAt.toString() + "&crp=" + pageNum.toString() + "&nptd=" + numPracticed.toString();

  if (document.getElementById("learn_show_meaning").checked) {
    url = url + "&with_meaning=true";
  }

  return url;
}

function buildMcqUrl(startAt, pageNum, numPracticed) {
  var url = window.location.protocol + "//" + window.location.host + "/contest/mcq"
  + "?sat=" + startAt.toString() + "&crp=" + pageNum.toString() + "&nptd=" + numPracticed.toString();

  return url;
}

function onSubmit() {
  var sat = getParameterByName("sat");
  var crp = parseInt(getParameterByName("crp")) + 1;
  var nptd = parseInt(getParameterByName("nptd")) + 1;

  window.location.href = buildLearnUrl(sat, crp, nptd);
}

function getApiUrl() {

  return window.location.protocol + "//" + window.location.host + "/api/contest/learn";
}

var pageData = {}

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
  if ("key" in pageData) {
    document.getElementById("learn_key").innerHTML = getArabicRepresentation(pageData["key"]);
    //document.getElementById("learn_key").innerHTML = pageData["key"];
  }

  if (getParameterByName("with_meaning") == "true") {
    //Show meaning box.
    document.getElementById("learn_value").style.display = "block";
    document.getElementById("learn_show_meaning").checked = true;
  } else {
    //Hide meaning box.
    document.getElementById("learn_value").style.display = "none";
    document.getElementById("learn_show_meaning").checked = false;
  }

  if ("value" in pageData) {
    document.getElementById("learn_value").innerHTML = pageData["value"];
  }
}

function onRootClick() {
  document.getElementById("learn_value").style.display = "block";
}

function toggleMeaningBox() {
  document.getElementById("learn_show_meaning").checked = !document.getElementById("learn_show_meaning").checked;

  if (document.getElementById("learn_show_meaning").checked) {
    //Show meaning box.
    document.getElementById("learn_value").style.display = "block";
  } else {
    //Hide meaning box.
    document.getElementById("learn_value").style.display = "none";
  }
}
