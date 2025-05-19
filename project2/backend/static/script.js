// apply filter
function applyFilters() {
    let formData = new FormData(document.getElementById("filter-form"));

    // Show loading animation
    document.getElementById("product-list").innerHTML = "<div class='loader'></div>";

    fetch("/products?" + new URLSearchParams(formData), { method: "GET" })
        .then(response => response.text())
        .then(html => {
            document.getElementById("product-list").innerHTML = html;  // Replace product grid
        })
        .catch(error => console.error("Error fetching filtered data:", error));
}

// update total price
function updateTotalPrice() {
    let quantity = document.getElementById("quantity").value;
    let price = document.getElementById("price").textContent;
    document.getElementById("total-price").textContent = (quantity * price).toFixed(2);
}

// add to cart
function addToCart(productId, quantity) {
    fetch(`/add_to_cart/${productId}/${quantity}`)
    .then(response => response.json())
    .then(data => {
        document.getElementById("cart-count").textContent = data.cart_count;
        updateCartSummary();
    });
}

// update cart summary
function updateCartSummary() {
    fetch("/cart_summary")
    .then(response => response.json())
    .then(data => {
        let cartList = document.getElementById("cart-items-list");
        let cartTotal = document.getElementById("cart-total");

        cartList.innerHTML = "";
        data.cart_items.forEach(item => {
            let cartItem = `<li>
                ${item.product.name} x${item.quantity} - $${(item.product.price * item.quantity).toFixed(2)}
                <button onclick="removeFromCart(${item.product.id})" class="btn btn-sm btn-danger">Remove</button>
            </li>`;
            cartList.innerHTML += cartItem;
        });

        cartTotal.textContent = data.total_price.toFixed(2);
    });
}

// remove from cart
function removeFromCart(productId) {
    fetch(`/remove_from_cart/${productId}`)
    .then(response => response.json())
    .then(() => updateCartSummary());  // Refresh cart summary instantly
}

// Update cart summary when page loads
document.addEventListener("DOMContentLoaded", updateCartSummary);

function toggleCart(productId) {
    fetch(`/toggle_cart/${productId}`, { method: "POST" })
    .then(response => response.json())
    .then(data => {
        document.getElementById("cart-button").textContent = data.message;
        document.getElementById("cart-count").textContent = data.cart_count;
        animateCartUpdate();  // Call animation effect
    });
}

function animateCartUpdate() {
    let cartIcon = document.getElementById("cart-icon");
    cartIcon.classList.add("cart-bounce");

    setTimeout(() => {
        cartIcon.classList.remove("cart-bounce");
    }, 500);
}

// Load cart state on page load
document.addEventListener("DOMContentLoaded", () => {
    fetch(`/cart_summary`)
    .then(response => response.json())
    .then(data => {
        document.getElementById("cart-count").textContent = data.cart_items.length;
    });
});


//  like reviews
function likeReview(reviewId) {
    fetch(`/like_review/${reviewId}`, { method: "GET" })
    .then(response => location.reload());  // Reload page to reflect new likes
}