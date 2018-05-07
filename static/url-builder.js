
function buildUploadUrl() {
  return window.location.protocol + "//" + window.location.host + "/contest/upload";
}

function buildSuggestApiUrl(term) {
  return window.location.protocol + "//" + window.location.host + "/api/suggest/" + term;
}

function buildInitialUrl(startAt, pageNum, numPracticed) {
  var url = window.location.protocol + "//" + window.location.host + "/contest/initial"
  + "?sat=" + startAt.toString() + "&crp=" + pageNum.toString() + "&nptd=" + numPracticed.toString();

  var element = document.getElementById("learn_show_meaning");
  if (element && element.checked) {
    url = url + "&with_meaning=true";
  }

  return url;
}

function buildLearnUrl(startAt, pageNum, numPracticed) {
  var url = window.location.protocol + "//" + window.location.host + "/contest/learn"
  + "?sat=" + startAt.toString() + "&crp=" + pageNum.toString() + "&nptd=" + numPracticed.toString();

  var element = document.getElementById("learn_show_meaning");
  if (element && element.checked) {
    url = url + "&with_meaning=true";
  }

  return url;
}

function buildMcqUrl(startAt, pageNum, numPracticed) {
  var url = window.location.protocol + "//" + window.location.host + "/contest/mcq"
  + "?sat=" + startAt.toString() + "&crp=" + pageNum.toString() + "&nptd=" + numPracticed.toString();

  return url;
}

function buildMtfUrl(startAt, pageNum, numPracticed) {
  var url = window.location.protocol + "//" + window.location.host + "/contest/mtf"
  + "?sat=" + startAt.toString() + "&crp=" + pageNum.toString() + "&nptd=" + numPracticed.toString();

  return url;
}

function buildSimUrl(startAt, pageNum, numPracticed) {
  var url = window.location.protocol + "//" + window.location.host + "/contest/sim"
  + "?sat=" + startAt.toString() + "&crp=" + pageNum.toString() + "&nptd=" + numPracticed.toString();

  return url;
}

function getContestApiUrl(section) {

  return window.location.protocol + "//" + window.location.host + "/api/contest/" + section;
}

function brokenUrl() {
  if (getParameterByName("sat") == null
  || getParameterByName("crp") == null
  || getParameterByName("nptd") == null) {

    return true;
  }

  return false;
}

function safeRedirect() {
  window.location.href = buildUploadUrl();
}
