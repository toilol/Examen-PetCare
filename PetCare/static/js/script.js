let cart = [];
let totalPrice = 0.00;

function addToCart(productName, productPrice) {
    // Añadir producto al carrito
    cart.push({ name: productName, price: parseFloat(productPrice) });
    // Actualizar el precio total
    totalPrice += parseFloat(productPrice);
    // Actualizar la interfaz de usuario
    updateCartUI();
}

function updateCartUI() {
    const cartItemsElement = document.getElementById('cart-items');
    const totalPriceElement = document.getElementById('total-price');

    // Limpiar la lista del carrito
    cartItemsElement.innerHTML = '';

    // Añadir cada producto del carrito a la lista
    cart.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.name} - $${item.price.toFixed(2)}`;
        cartItemsElement.appendChild(li);
    });

    // Actualizar el precio total
    totalPriceElement.textContent = totalPrice.toFixed(2);
}