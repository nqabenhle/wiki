window.onload = function() {
    countChar();
    path = window.location.pathname;

    console.log(path);
}

function countChar() {
    let charCountContainer = document.querySelectorAll(".count-char"),
    textarea = document.querySelector(".mkdown-content");

    textCount = document.createElement("p");
    textCount.classList = "char-count";
    node = document.createTextNode(textarea.value.length + " characters.");
    textCount.appendChild(node);
    charCountContainer[1].appendChild(textCount);

    textarea.addEventListener("input", () => {
        textCount.textContent = textarea.value.length + " characters."
    });
}