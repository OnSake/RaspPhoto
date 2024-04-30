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
  photoImage.src = 'assets/img/icon.png'
}

function retakeImage() {
  console.log("retakeImage lancé");
  photoImage.classList.add("cache");
  previewButton.classList.remove("cache")
  retakeButton.classList.add("cache");
  downloadButton.classList.add("off")
}

function takeImage(){
  console.log("takeImage lancé")
  retakeButton.classList.remove("cache")
  takePhotoButton.classList.add("off")
  runPython('/leds')
  runPython('/shot')
    .then((photoName) => {
      var photo_nom = 'assets/photos/' + photoName + '.jpg'
      photoImage.src = photo_nom
      downloadButton.classList.remove("off")
    })
}

function downloadImage(){
  console.log("DownloadImage Lancé")
  const link = document.createElement('a')
  link.href = photoImage.src
  link.download = 'photo.jpg'
  document.body.appendChild(link)
  link.click()
  document.body.removeChlid(link)
}

//172.20.80.138
function runPython(url) {
  return new Promise((resolve, reject) => {
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
      resolve(data);
    })
    .catch((error) => {
      console.error("Erreur:", error);
      reject(error)
    });
  })

}
