$("#add-to-cart-btn").on("click", function () {
  let quantity = $("#product-quantity").val();
  let product_title = $(".product-title").val();
  let product_id = $(".product_id").val();
  let product_price = $(".product_price").text();
  let this_val = $(this);

  console.log("Quantity:", quantity);
  console.log("title:", Product - title);
  console.log("ID", product_id);
  console.log("price:", product_price);
  console.log("current_element:", this_val);
});
