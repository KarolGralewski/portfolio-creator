//fuction that copies the div and pastes it below
//and adds number to the div id
var projectsCounter = 1;
function copyDiv() {
  if (projectsCounter < 3) {
    var container = document.getElementById("projects");
    var section = document.getElementById("project0");
    var clone = section.cloneNode(true);
    clone.id = "project" + projectsCounter;
    clone.name = "project" + projectsCounter;
    projectsCounter++;
    container.appendChild(clone);
  }
}

let textArea = document.getElementById("infoShort");
let characterCounter = document.getElementById("infoShortCharCount");
const maxNumOfChars = 100;

function changeColor(counter) {
  if (counter < 15) {
    characterCounter.style.color = "red";
  } else if (counter < 50) {
    characterCounter.style.color = "orange";
  } else {
    characterCounter.style.color = "";
  }
}

const countCharacters = () => {
  let numOfEnteredChars = textArea.value.length;
  let counter = maxNumOfChars - numOfEnteredChars;
  characterCounter.textContent = counter + "/100";
  changeColor(counter);
};

textArea.addEventListener("input", countCharacters);
