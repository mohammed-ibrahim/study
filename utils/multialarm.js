var ST_PENDING = "PENDING";
var ST_COUNTING = "COUNTING";
var ST_ON_ALARM = "ON_ALARM";
var N_ALARMS = 15;

//TODO: convert to minutes later
var SNOOZE_TOME = 3;

var actionButtons = [
  "start_button",
  "close_button",
  "snooze_button"
];

String.prototype.replaceAll = function(search, replacement) {
    var target = this;
    return target.replace(new RegExp(search, 'g'), replacement);
};

window.onbeforeunload = function() {
  var ans = confirm("Are you sure you want change page!");
  if(ans == true) {

    return true;
  } else {

    return false;
  }
};

window.onload = function() {
  var template = document.getElementById("template").innerHTML;
  var buffer = "";

  for (i=0;  i<N_ALARMS; i++) {
    buffer = buffer + template.replaceAll("_placeholder", "_" + (i+1).toString())
  }

  document.getElementById("placement").innerHTML = buffer;
}

function convertToMinutes(value) {
  return parseInt(value) * 60;
}

function getIdentifier(element) {
  var parts = element.id.split("_");
  return parts[parts.length - 1];
}

function playAudio() {
  var x = document.getElementById("audio_element");
  x.currentTime = 0;
  x.play();
}

function pauseAudio() {
  var x = document.getElementById("audio_element");
  x.pause();
}

function getSufixedArray(arr, id) {
  var sf = [];

  for (var index in arr) {
    var value = arr[index];
    sf.push(value + "_" + id);
  }

  return sf;
}

function showOnlyButtons(arr, id) {
  arr = getSufixedArray(arr, id);
  for (var index in actionButtons) {
    var buttonId = actionButtons[index] + "_" + id;

    if (arr.includes(buttonId)) {
      document.getElementById(buttonId).disabled = false;
    } else {
      document.getElementById(buttonId).disabled = true;
    }
  }
}

function updateStatus(state, count, id) {
  document.getElementById("status_" + id).innerHTML = state;

  if (count != null) {
    document.getElementById("count_" + id).innerHTML = count.toString();
  }
}

function startAlarm(element) {
  var id = getIdentifier(element);
  var strCount = document.getElementById("count_" + id).innerHTML;
  var intCount = parseInt(strCount);

  showOnlyButtons(["close_button"], id);
  var selectedValue = document.getElementById("select_" + id).value;

  updateStatus(ST_COUNTING, convertToMinutes(selectedValue), id);
}

function closeAlarm(element) {

  var id = getIdentifier(element);
  pauseAudio();
  showOnlyButtons(["start_button"], id);
  updateStatus(ST_PENDING, 0, id);
}

function snoozeAlarm() {

  var id = getIdentifier(element);
  showOnlyButtons(["close_button"], id);
  pauseAudio();
  updateStatus(ST_COUNTING, SNOOZE_TOME, id);
}

function getStatus(id) {
  var state = document.getElementById("status_" + id).innerHTML;
  var count = parseInt(document.getElementById("count_" + id).innerHTML);

  if (!isNaN(count)) {
    return {
      "state": state,
      "count": count
    }
  }
}

function counter() {
  for (i=0;  i<N_ALARMS; i++) {
    counterFor((i+1).toString());
  }
}

function counterFor(id) {

  var status = getStatus(id);

  if (status != null && status.state == ST_COUNTING) {

    var count = status.count;

    if (count <= 0) {

      playAudio();
      showOnlyButtons(["snooze_button","close_button"], id);
      updateStatus(ST_ON_ALARM, 0, id);
    } else {

      count = count - 1;
      updateStatus(status.state, count, id);
    }
  }

}

window.setInterval(counter, 1000);
