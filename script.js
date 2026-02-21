document.getElementById("resumeForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let name = document.getElementById("name").value;
    let education = document.getElementById("education").value;
    let skills = document.getElementById("skills").value;
    let projects = document.getElementById("projects").value;

    let resumeTemplate = `
        <h3>${name}</h3>
        <hr>
        <p><strong>Education:</strong><br>${education}</p>
        <p><strong>Skills:</strong><br>${skills}</p>
        <p><strong>Projects:</strong><br>${projects}</p>
        <p><em>This resume was generated using AI-based template simulation.</em></p>
    `;

    document.getElementById("resumeContent").innerHTML = resumeTemplate;
    document.getElementById("output").classList.remove("hidden");
});
