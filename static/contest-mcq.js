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

function onSubmit() {

  if (!validateResult()) {
    return;
  }

  var sat = getParameterByName("sat");
  var crp = parseInt(getParameterByName("crp")) + 1;
  var nptd = parseInt(getParameterByName("nptd")) + 1;

  window.location.href = buildMcqUrl(sat, crp, nptd);
}

function resetPanels() {
  document.getElementById("mcq_a").checked = false;
  document.getElementById("mcq_b").checked = false;
  document.getElementById("mcq_c").checked = false;
  document.getElementById("mcq_d").checked = false;
}

var pageData = {}

function validateResult() {

  var selectedAnswer;
  if (document.getElementById("mcq_a").checked) {

    selectedAnswer = document.getElementById("label_for_mcq_a").innerHTML;
  } else if (document.getElementById("mcq_b").checked) {

    selectedAnswer = document.getElementById("label_for_mcq_b").innerHTML;
  } else if (document.getElementById("mcq_c").checked) {

    selectedAnswer = document.getElementById("label_for_mcq_c").innerHTML;
  } else if (document.getElementById("mcq_d").checked) {

    selectedAnswer = document.getElementById("label_for_mcq_d").innerHTML;
  } else {

    alert("Please make a selection!");
    return false;
  }

  if (selectedAnswer == pageData["correct_answer"]) {

    return true;
  } else {

    alert("Incorrect answer");
  }

  return false;
}

function getData() {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', getContestApiUrl('mcq'), true);

  xhr.onreadystatechange = function() {

    if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
      pageData = JSON.parse(xhr.responseText);
      renderPageData();
    }

    if (xhr.readyState == XMLHttpRequest.DONE && xhr.status != 200) {
      console.error("Api request failed: " + getContestApiUrl('mcq'));
    }
  }

  xhr.send();
}

function renderPageData() {
  document.getElementById("mcq_question").innerHTML = getArabicRepresentation(pageData["question"]);
  document.getElementById("label_for_mcq_a").innerHTML = pageData["options"][0]["value"];
  document.getElementById("label_for_mcq_b").innerHTML = pageData["options"][1]["value"];
  document.getElementById("label_for_mcq_c").innerHTML = pageData["options"][2]["value"];
  document.getElementById("label_for_mcq_d").innerHTML = pageData["options"][3]["value"];
}

function onOptionLabelClick(element) {
  var elementId = element.id;
  var lastChar = elementId[elementId.length - 1];
  document.getElementById("mcq_" + lastChar).checked = true;
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
