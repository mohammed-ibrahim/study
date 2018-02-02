
window.onload = function() {
  getData();
};

function onSubmit() {
  getData();
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
  }

  if (document.getElementById("learn_show_meaning").checked) {
    //Show meaning box.
    document.getElementById("learn_value").style.display = "block";
  } else {
    //Hide meaning box.
    document.getElementById("learn_value").style.display = "none";
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
