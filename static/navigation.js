window.addEventListener("keydown", keyboardHandler, false);

function keyboardHandler(e) {

    if (event.defaultPrevented) {
        return; // Do nothing if the event was already processed
    }

    switch (event.key) {
        case "ArrowDown":
            // code for "down arrow" key press.
            window.scrollBy(0, 500);
            break;

        case "ArrowUp":
            // code for "up arrow" key press.
            window.scrollBy(0, -500);
            break;

        case "ArrowLeft":
            // code for "left arrow" key press.
            previousRuku();
            break;

        case "ArrowRight":
            // code for "right arrow" key press.
            nextRuku();
            break;

        default:
            return; // Quit when this doesn't handle the key event.
    }

    // Cancel the default action to avoid it being handled twice
    event.preventDefault();
}

function nextRuku() {
    if (pageStateRukuData) {
        var rukuIndex = pageStateRukuData["next_ruku_number"].toString();
        var newUrl = window.location.href.replace(/\/[^\/]*$/, '/' + rukuIndex);
        console.log(newUrl);
        window.location.href = newUrl;
    }
}

function previousRuku() {
    if (pageStateRukuData) {
        var rukuIndex = pageStateRukuData["previous_ruku_number"].toString();
        var newUrl = window.location.href.replace(/\/[^\/]*$/, '/' + rukuIndex);
        console.log(newUrl);
        window.location.href = newUrl;
    }
}

function navigateToSurah() {
    var selectedValue = document.getElementById("surah_selection").value;

    if (selectedValue && pageStateRukuData && pageStateSurahMetaData) {
        var rukuNumber = pageStateSurahMetaData[selectedValue]["ruku"][0]["ruku_index"];
        var newUrl = window.location.href.replace(/\/[^\/]*$/, '/' + rukuNumber);
        console.log(newUrl);
        window.location.href = newUrl;
    }
}

function navigateToRuku() {
    var selectedValue = document.getElementById("ruku_selection").value;

    if (selectedValue) {
        var newUrl = window.location.href.replace(/\/[^\/]*$/, '/' + selectedValue);
        console.log(newUrl);
        window.location.href = newUrl;
    }
}
