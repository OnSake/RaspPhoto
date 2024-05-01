//Elements HTML
const photoImage = document.getElementById("photo-image"),
      previewButton = document.getElementById("image-launch-button"),
      compteReboursText = document.getElementById('compte-rebours-text'),      
      go1 = document.getElementById('1'),
      go2 = document.getElementById('2'),
      go3 = document.getElementById('3'),
      retakeButton = document.getElementById("retake-image-button"),
      takePhotoButton = document.getElementById("take-image"),
      downloadButton = document.getElementById("download-button"),
      launchPreviewText = document.getElementById("launch-preview-text");
      
//Affichage de l'écran pour la 
function launchPreview() {
  console.log("launchPreview lancé");
  previewButton.classList.add("cache");
  takePhotoButton.classList.remove("off");
  launchPreviewText.classList.remove("cache")
  compteReboursText.classList.remove("cache")
  photoImage.src = 'assets/img/icon.png'
}


function retakeImage() {
  console.log("retakeImage lancé");
  photoImage.classList.add("cache");
  previewButton.classList.remove("cache")
  retakeButton.classList.add("cache");
  downloadButton.classList.add("off")
  compteReboursText.classList.add("cache")
}



function takeImage(){
  console.log("takeImage lancé");
  retakeButton.classList.remove("cache");
  takePhotoButton.classList.add("off");
  ledsAndPhoto(); 
}

function ledsAndPhoto(){
  runPython('/leds');
  go1.classList.add("compte_go");
  setTimeout(() =>{
    go2.classList.add("compte_go");
  }, 1500);
  setTimeout(() =>{
    go3.classList.add("compte_go");
  }, 3000);

  // Appel à runPython('/shot') après que toutes les animations et les délais soient terminés
  setTimeout(() =>{
    runPython('/shot')
      .then((photoName) => {
        var photo_nom = 'assets/photos/' + photoName + '.jpg';
        photoImage.src = photo_nom;
        downloadButton.classList.remove("off");
        photoImage.classList.remove("cache");
      });
    
    // Cache le texte de l'aperçu après que la photo ait été prise
    setTimeout(() =>{
      compteReboursText.classList.add("cache");
      go1.classList.remove("compte_go")
      go2.classList.remove("compte_go")
      go3.classList.remove("compte_go")
    }, 500);
  }, 4500);
}
//Téléchargement de photo affichée
function downloadImage(){
  console.log("DownloadImage Lancé")
  const link = document.createElement('a')
  link.href = photoImage.src
  link.download = 'photo.jpg'
  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)
  //On crée un élément html <a> dans lequel on insère l'image, on 
}

//172.20.80.138
function runPython(url) {
  return new Promise((resolve, reject) => {
    fetch('http://192.168.1.127:5000' + url) 
    .then((response) => {
      if (!response.ok) {
        throw new Error("La requête a échoué");
      }
      return response.text(); 
    })
    .then((data) => {
      console.log(data); 
      resolve(data);
    })
    .catch((error) => {
      console.error("Erreur:", error);
      reject(error)
    });
  })

}
