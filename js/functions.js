
//fuction that copies the div and pastes it below
//and adds number to the div id
var projectsCounter = 1;
function copyDiv() {
   if (projectsCounter < 3) {
      var container = document.getElementById('projects');
      var section = document.getElementById("project0");
      var clone = section.cloneNode(true);
      clone.id = "project" + projectsCounter;
      clone.name = "project" + projectsCounter;
      projectsCounter++;
      container.appendChild(clone);
   }

}


