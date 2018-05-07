nMaxPages = 7;

window.onload = function() {

  if (brokenUrl()) {
    safeRedirect();
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

var pageData = {}

function getData() {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', getContestApiUrl('sim'), true);

  xhr.onreadystatechange = function() {

    if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
      pageData = JSON.parse(xhr.responseText);
      renderPageData();
    }

    if (xhr.readyState == XMLHttpRequest.DONE && xhr.status != 200) {
      pageData = null;
      console.error("Api request failed: " + getContestApiUrl('sim'));
    }
  }

  xhr.send();
}

var table_content_placeholder = "<tr>   <td  class=\"bigfont\">__root__</td>    <td>__meaning__</td>  <td>__stats__</td>   </tr>";

function renderPageData() {
  if (pageData) {

    var text = "";

    var rootSequence = pageData['seq'];

    for (var index in rootSequence) {
      var rootValue = rootSequence[index];

      var englishMeaning = pageData['data'][rootValue]['english-meaning'];
      var distinctAppearence = pageData['data'][rootValue]['statistics']['appears_number_of_surah'];
      var numOccurrence = pageData['data'][rootValue]['statistics']['num_of_occurrence'];

      text = text + table_content_placeholder.replace("__root__", getArabicRepresentation(rootValue))
          .replace("__meaning__", englishMeaning)
          .replace("__stats__", distinctAppearence.toString() + "-" + numOccurrence.toString());
    }

    document.getElementById("tbody_identifier").innerHTML = text;
  }
}

function onSubmit() {

  var sat = getParameterByName("sat");
  var crp = parseInt(getParameterByName("crp")) + 1;
  var nptd = parseInt(getParameterByName("nptd")) + 1;

  window.location.href = buildSimUrl(sat, crp, nptd);
}
