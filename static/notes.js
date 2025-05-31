const createNote = () => {
    const container = document.getElementById("note-container");

    const section = document.createElement("div");
    section.className = "note-section";

    const editable = document.createElement("div");
    editable.className = "editable";
    editable.contentEditable = true;
    editable.innerText = "Write your notes here...";

    section.appendChild(editable);
    container.appendChild(section);
}

const saveNote = () => {
    const title = document.getElementById("note-title").value;
    const sections = document.querySelectorAll(".editable");
    let content = "";

    sections.forEach((sec, i) => {
        content += `<h3>Section ${i + 1}</h3>\n` + sec.innerHTML + "\n<hr>\n";
    });

    fetch("/save_note", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            title: title,
            content: content,
            format: "html" // Or "md" if you build markdown support
        })
    })
    .then(res => res.json())
    .then(data => alert(data.message));
}

const loadNote = () => {
    const title = document.getElementById("note-title").value;
    fetch(`/load_note?title=${title}&format=html`)
        .then(res => res.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
                return;
            }

            const container = document.getElementById("note-container");
            container.innerHTML = "";

            // Optionally parse sections out of loaded HTML
            const tempDiv = document.createElement("div");
            tempDiv.innerHTML = data.content;

            tempDiv.querySelectorAll("h3, .editable, hr").forEach(el => {
                const section = document.createElement("div");
                section.className = "note-section";

                if (el.tagName === "H3" || el.tagName === "HR") {
                    section.appendChild(el);
                } else {
                    el.className = "editable";
                    el.contentEditable = true;
                    section.appendChild(el);
                }

                container.appendChild(section);
            });
        });
}
