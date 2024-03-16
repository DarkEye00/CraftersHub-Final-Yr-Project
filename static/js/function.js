console.log("Working Fine");
// Get a reference to the div
var myDiv = document.getElementById("notify");

// Use setTimeout to hide the div after 2000 milliseconds (2 seconds)
setTimeout(function () {
  myDiv.style.display = "none";
}, 1000);

////////////////////////////////
//Add to cart functionality

$("#add-to-cart-btn").on("click", function () {
  let quantity = $("#product-quantity").val();
  let product_title = $(".product-title").val();
  let product_id = $(".product-pid").val();
  let product_price = $(".product-price").text();
  let product_image = $(".product-image").attr("src");
  let this_val = $(this);

  console.log("Quantity:", quantity);
  console.log("title:", product_title);
  console.log("ID:", product_id);
  console.log("price:", product_price);
  console.log("current_element:", this_val);
  console.log("Image:", product_image);

  $.ajax({
    url: "/add-to-cart",
    data: {
      id: product_id,
      qty: quantity,
      title: product_title,
      price: product_price,
      image: product_image,
      pid: product_id,
    },
    dataType: "json",
    beforeSend: function () {
      console.log("Adding products to cart....");
    },
    success: function (response) {
      this_val.html("Added to cart");
      console.log("Products added to cart");
      $(".cart-items-count").text(response.totalcartitems);
      this_val.attr("disabled", false);
    },
  });
});
/////////////////////////////////////////////////
//Delete Product
$(document).on("click", ".delete-product", function () {
  let product_id = $(this).attr("data-product");
  let this_val = $(this);

  console.log("Product Id:", product_id);

  $.ajax({
    url: "/delete-from-cart",
    data: {
      id: product_id,
    },
    dataType: "json",
    beforeSend: function () {
      this_val.hide();
    },
    success: function (response) {
      this_val.show();
      console.log("Product removed from cart");
      $(".cart-items-count").text(response.totalcartitems);
      $("#cart-list").html(response.data);
    },
  });
});
///////////////////////////////////////////////////////////
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

//////////////////////////////////////
//Process review.comments
$("#CommentForm").submit(function (e) {
  e.preventDefault();

  $.ajax({
    data: $(this).serialize(),

    method: $(this).attr("method"),
    url: $(this).attr("action"),
    dataType: "json",

    success: function (response) {
      console.log("Comment Saved");
      /*
      if (response.bool == true) {
        $("#review-res").html("Review Added Successfully");
        $(".hide-comment-form").hide();

          
          let _html = '<div class="pb-5"></div>'
              _html += '<a class="text-green-500 font-semibold py-2"
              >{{r.user.username|title}} |<span class="text-black font-light">
                {{r.date|date}}</span
              ></a
            >'
      } */
    },
  });
});
