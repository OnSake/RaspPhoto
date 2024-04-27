const photoImage = document.getElementById("photo-image"),
  imageButton = document.getElementById("image-launch-button");
retakeButton = document.getElementById("retake-image-button");
testInput = document.getElementById("test");

function launchImage() {
  console.log("launchImage lancé");
  photoImage.classList.remove("cache");
  imageButton.classList.add("cache");
  retakeButton.classList.remove("retake_image");
}

function retakeImage() {
  console.log("retakeImage lancé");
  photoImage.classList.add("cache");
  imageButton.classList.remove("cache");
  retakeButton.classList.add("retake_image");
}

function runPython(url) {
  fetch("http://localhost:5000" + url)
    .then((response) => {
      if (!response.ok) {
        throw new Error("La requête a échoué");
      }
      return response.text(); // Convertir la réponse en texte
    })
    .then((data) => {
      // Utiliser les données récupérées
      console.log(data); // Afficher les données dans la console
      // Vous pouvez assigner les données à une variable si nécessaire
      let variableContenantLesDonnees = data;
      testInput.textContent = data;
    })
    .catch((error) => {
      console.error("Erreur:", error);
    });
}
