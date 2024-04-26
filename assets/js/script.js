const photoImage = document.getElementById("photo-image"),
  imageButton = document.getElementById("image-launch-button");
retakeButton = document.getElementById("retake-image-button");

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
