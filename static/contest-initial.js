

window.onload = function() {

  if (brokenUrl()) {
    safeRedirect();
    return;
  }

  getData();
};

function onSubmit() {
  var sat = getParameterByName("sat");
  var crp = parseInt(getParameterByName("crp")) + 1;
  var nptd = parseInt(getParameterByName("nptd")) + 1;

  window.location.href = buildInitialUrl(sat, crp, nptd);
}

var pageData = {}

function getData() {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', getContestApiUrl('initial'), true);

  xhr.onreadystatechange = function() {

    if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
      pageData = JSON.parse(xhr.responseText);
      renderPageData();
      return;
    }

    if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 405) {
      console.log("url sent 405 redirecting to learn page...");
      var sat = getParameterByName("sat");
      var nptd = getParameterByName("nptd");
      var url = buildLearnUrl(sat, 1, nptd);
      window.location.href = url;
      return;
    }

    if (xhr.readyState == XMLHttpRequest.DONE && xhr.status != 200) {
      console.error("Api request failed: " + getContestApiUrl('initial'));
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
