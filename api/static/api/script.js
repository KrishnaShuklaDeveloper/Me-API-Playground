const API_BASE = "/api";

let allProjects = [];
let allSkills = [];

async function loadProfile() {
  try {
    const res = await fetch(`${API_BASE}/profiles/`);
    const data = await res.json();

    if (data.length > 0) {
      const profile = data[0];
      let html = `<p><strong>Name:</strong> ${profile.name}</p>
                  <p><strong>Email:</strong> ${profile.email}</p>
                  <p><strong>Education:</strong> ${profile.education}</p>
                  <p><strong>Summary:</strong> ${profile.summary}</p>`;

      if (profile.links) {
        html += `<p><strong>Links:</strong> `;
        if (profile.links.github)
          html += `<a href="${profile.links.github}" target="_blank">GitHub</a> `;
        if (profile.links.linkedin)
          html += `| <a href="${profile.links.linkedin}" target="_blank">LinkedIn</a>`;
        if (profile.links.portfolio)
          html += `| <a href="${profile.links.portfolio}" target="_blank">Portfolio</a>`;
        html += `</p>`;
      }

      document.getElementById("profile").innerHTML = html;
    } else {
      document.getElementById("profile").innerHTML = "<p>No profile found.</p>";
    }
  } catch (err) {
    console.error("Error loading profile:", err);
    document.getElementById("profile").innerHTML = "<p>Error loading profile.</p>";
  }
}

async function loadData() {
  try {
    const projectsRes = await fetch(`${API_BASE}/projects/`);
    allProjects = await projectsRes.json();

    const skillsRes = await fetch(`${API_BASE}/skills/`);
    allSkills = await skillsRes.json();

    displayProjects(allProjects);
    displaySkills(allSkills);

  } catch (err) {
    console.error("Error loading data:", err);
  }
}

function displayProjects(projects) {
  const container = document.getElementById("projects");
  if (!projects.length) {
    container.innerHTML = "<p>No projects found.</p>";
    return;
  }

  container.innerHTML = projects.map(p => {
    const skills = p.skills.map(s => `${s.name} (${s.level}/5)`).join(", ");
    let linksHtml = p.links ? `<a href="${p.links}" target="_blank">Project Link</a>` : "";
    return `<div>
              <h3>${p.title}</h3>
              <p>${p.description}</p>
              <p>${linksHtml}</p>
              <p><strong>Skills:</strong> ${skills}</p>
            </div>`;
  }).join("<hr>");
}

function displaySkills(skills) {
  const container = document.getElementById("skills");
  if (!skills.length) {
    container.innerHTML = "<p>No skills found.</p>";
    return;
  }

  container.innerHTML = skills.map(s => `<div>${s.name} (${s.level}/5)</div>`).join("");
}

function filterData(query) {
  query = query.toLowerCase();

  const filteredProjects = allProjects.filter(p =>
    p.title.toLowerCase().includes(query) ||
    p.description.toLowerCase().includes(query) ||
    p.skills.some(s => s.name.toLowerCase().includes(query))
  );

  const filteredSkills = allSkills.filter(s =>
    s.name.toLowerCase().includes(query)
  );

  displayProjects(filteredProjects);
  displaySkills(filteredSkills);
}

document.getElementById("searchInput").addEventListener("input", (e) => {
  filterData(e.target.value);
});

const toggleBtn = document.getElementById("darkModeToggle");

if (localStorage.getItem("dark-mode") === "enabled") {
  document.body.classList.add("dark-mode");
  toggleBtn.textContent = "☀️Light Mode";
}

toggleBtn.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");

  if (document.body.classList.contains("dark-mode")) {
    localStorage.setItem("dark-mode", "enabled");
    toggleBtn.textContent = "☀️Light Mode";
  } else {
    localStorage.setItem("dark-mode", "disabled");
    toggleBtn.textContent = "🌙Dark Mode";
  }
});

window.onload = () => {
  loadProfile();
  loadData();
};

