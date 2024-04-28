const photoImage = document.getElementById("photo-image"),
      previewButton = document.getElementById("image-launch-button");
      retakeButton = document.getElementById("retake-image-button");
      takePhotoButton = document.getElementById("take-image");
      donwloadButton = document.getElementById("download-button");
      testInput = document.getElementById("test");

function launchPreview() {
  console.log("launchPreview lancé");
  photoImage.classList.remove("cache");
  previewButton.classList.add("cache");
  takePhotoButton.classList.remove("off");
}

function retakeImage() {
  console.log("retakeImage lancé");
  photoImage.classList.add("cache");
  previewButton.classList.remove("cache")
  retakeButton.classList.add("cache");
  donwloadButton.classList.add("off")
}

function takeImage(){
  console.log("takeImage lancé")
  retakeButton.classList.remove("cache")
  donwloadButton.classList.remove("off")
  takePhotoButton.classList.add("off")
}

function runPython(url) {
  fetch('http://192.168.1.127:5000' + url)
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
