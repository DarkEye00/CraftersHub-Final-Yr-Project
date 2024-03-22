console.log("Working Fine");

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

      if (response.bool == true) {
        $("#review-res").html("Review Added Successfully");
        $(".hide-comment-form").hide();

        let _html = '<div class="pb-5">';
        _html += '<div class="flex">';

        _html +=
          '<a class="text-green-500 font-semibold py-2"> ' +
          response.context.user +
          '<span class="text-black font-light"></span>';
        ("</a>");
        _html = "<p>";
        for (let i = 1; i <= response.context.rating; i++) {
          _html += "<p></p>";
        }
        ("</p>");

        _html += "</div>";
        _html += '<div class="w-[500px]">';
        _html += "<hr />";
        _html += "</div>";

        _html += "<p>" + response.context.review + "</p>";
        _html += "</div>";
        $(".comment-list").prepend(_html);

        location.reload();
      }
    },
  });
});
