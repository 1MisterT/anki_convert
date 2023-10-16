document.getElementById("myfile").addEventListener("change", (event) => {
    btn = event.target;
    filename = btn.files[0].name;
    btn.parentNode.children[1].innerHTML = filename
})
try {
    document.getElementById("copy-btn").addEventListener("click", copy_text);
} catch (e) {
    if (e instanceof TypeError)
        e = 0;
    else alert(e);
}

function copy_text(){
    const copyText = document.getElementById("myInput").textContent.trim();
    const textArea = document.createElement('textarea');
    textArea.textContent = copyText;
    document.body.append(textArea);
    textArea.select();
    document.execCommand("copy");
    textArea.style.display = "none";

    // console.log("Hello World!");
}
