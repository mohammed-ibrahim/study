var ST_PENDING = "PENDING";
var ST_COUNTING = "COUNTING";
var ST_ON_ALARM = "ON_ALARM";

//TODO: convert to minutes later
var SNOOZE_TOME = 3;

var actionButtons = [
  "start_button_placeholder",
  "close_button_placeholder",
  "snooze_button_placeholder"
];



function playAudio() {
  var x = document.getElementById("audio_element");
  x.currentTime = 0;
  x.play();
}

function pauseAudio() {
  var x = document.getElementById("audio_element");
  x.pause();
}

function showOnlyButtons(arr) {
  for (var index in actionButtons) {
    var buttonId = actionButtons[index];

    if (arr.includes(buttonId)) {
      document.getElementById(buttonId).disabled = false;
    } else {
      document.getElementById(buttonId).disabled = true;
    }
  }
}

function updateStatus(state, count) {
  document.getElementById("status_placeholder").innerHTML = state;

  if (count != null) {
    document.getElementById("count_placeholder").innerHTML = count.toString();
  }
}

function startAlarm(element) {
  var strCount = document.getElementById("count_placeholder").innerHTML;
  var intCount = parseInt(strCount);

  showOnlyButtons(["close_button_placeholder"]);
  var selectedValue = document.getElementById("select_placeholder").value;

  //TODO: convert to minutes later
  // updateStatus(ST_COUNTING, selectedValue);
  updateStatus(ST_COUNTING, selectedValue);
}

function closeAlarm(element) {

  pauseAudio();
  console.log("Navigated to close()");
  showOnlyButtons(["start_button_placeholder"]);
  updateStatus(ST_PENDING, 0);
}

function snoozeAlarm() {

  showOnlyButtons(["close_button_placeholder"]);
  pauseAudio();
  updateStatus(ST_COUNTING, SNOOZE_TOME);
}

function getStatus() {
  var state = document.getElementById("status_placeholder").innerHTML;
  var count = parseInt(document.getElementById("count_placeholder").innerHTML);

  if (!isNaN(count)) {
    return {
      "state": state,
      "count": count
    }
  }
}

function counter() {

  var status = getStatus();

  if (status != null && status.state == ST_COUNTING) {

    var count = status.count;

    if (count <= 0) {

      playAudio();
      showOnlyButtons(["snooze_button_placeholder","close_button_placeholder"]);
      updateStatus(ST_ON_ALARM, 0);
    } else {

      count = count - 1;
      updateStatus(status.state, count);
    }
  }

}

window.setInterval(counter, 1000);
