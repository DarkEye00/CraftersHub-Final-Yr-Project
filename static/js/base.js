document
  //buton functionality in the product detail page
  .getElementById("descriptionBtn")
  .addEventListener("click", function () {
    document.getElementById("reviews").style.display = "none";
    document.getElementById("specification").style.display = "none";
    document.getElementById("description").style.display = "block";
    descriptionBtn.classList.add("text-green-700");
    descriptionBtn.classList.remove("text-gray-700");
    reviewsBtn.classList.add("text-gray-700");
    reviewsBtn.classList.remove("text-green-700");
    specificationBtn.classList.add("text-gray-700");
    specificationBtn.classList.remove("text-green-700");
  });

document.getElementById("reviewsBtn").addEventListener("click", function () {
  document.getElementById("description").style.display = "none";
  document.getElementById("specification").style.display = "none";
  document.getElementById("reviews").style.display = "block";
  reviewsBtn.classList.add("text-green-700");
  reviewsBtn.classList.remove("text-gray-700");
  descriptionBtn.classList.add("text-gray-700");
  descriptionBtn.classList.remove("text-green-700");
  specificationBtn.classList.add("text-gray-700");
  specificationBtn.classList.remove("text-green-700");
});
document
  .getElementById("specificationBtn")
  .addEventListener("click", function () {
    document.getElementById("reviews").style.display = "none";
    document.getElementById("specification").style.display = "block";
    document.getElementById("description").style.display = "none";
    specificationBtn.classList.add("text-green-700");
    specificationBtn.classList.remove("text-gray-700");
    descriptionBtn.classList.remove("text-green-700");
    descriptionBtn.classList.add("text-gray-700");
    reviewsBtn.classList.add("text-gray-700");
    reviewsBtn.classList.remove("text-green-700");
  });

// Get a reference to the div
var myDiv = document.getElementById("notify");

// Use setTimeout to hide the div after 2000 milliseconds (2 seconds)
setTimeout(function () {
  myDiv.style.display = "none";
}, 1000);
