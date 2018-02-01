
function onUpload() {
  var textBox = document.getElementById("primary_input_text");

  if (!textBox.value) {
    alert("Empty input");
    return false;
  }

  var data = textBox.value
  var sdata = data.split("\n");

  var result = Array();

  for (line in sdata) {
    linedata = sdata[line];
    var content = linedata.split(" - ");

    if (content.length == 2) {
      var dictObj = {key: content[0], value: content[1]};
      result.push(dictObj);
    } else {

      console.error("Entry format error: " + linedata);
    }
  }

  if (result.length > 0) {
    var xhr = new XMLHttpRequest();
    var url = getPostUrl();
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = function () {

      if (xhr.readyState === 4) {
        if (xhr.status === 200) {

          window.location = window.location.protocol + "//" + window.location.host + "/contest/learn";
          console.log(xhr.responseText);
        } else {

          console.log("There was error posting data");
        }
      }
    };

    var data = JSON.stringify(result);
    xhr.send(data);
  } else {
    alert("Dictionary size is zero");
  }
}

function getPostUrl() {
  return window.location.protocol + "//" + window.location.host + "/api/contest";
}
