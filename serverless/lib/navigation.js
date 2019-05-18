// window.addEventListener("keydown", keyboardHandler, false);
//
// function keyboardHandler(e) {
//
//     if (event.defaultPrevented) {
//         return; // Do nothing if the event was already processed
//     }
//
//     switch (event.key) {
//         case "ArrowDown":
//             // code for "down arrow" key press.
//             window.scrollBy(0, 500);
//             break;
//
//         case "ArrowUp":
//             // code for "up arrow" key press.
//             window.scrollBy(0, -500);
//             break;
//
//         case "ArrowLeft":
//             // code for "left arrow" key press.
//             previousRuku();
//             break;
//
//         case "ArrowRight":
//             // code for "right arrow" key press.
//             nextRuku();
//             break;
//
//         default:
//             return; // Quit when this doesn't handle the key event.
//     }
//
//     // Cancel the default action to avoid it being handled twice
//     event.preventDefault();
// }

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

    if (selectedValue && rukuContent && metadata) {
        dyload(selectedValue)
    }
}

function navigateToRuku() {
    var selectedValue = document.getElementById("ruku_selection").value;

    if (selectedValue) {
        dyloadRukuNumber(selectedValue);
    }
}

function navigateToAyah() {
    var selectedValue = document.getElementById("ayah_selection").value;

    if (selectedValue) {
        selectAyah(selectedValue);
    }
}
