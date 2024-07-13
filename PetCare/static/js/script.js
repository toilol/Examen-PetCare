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

document.addEventListener('DOMContentLoaded', function() {
    const btnPagar = document.getElementById('btn-pagar');
    const mensajeExito = document.getElementById('mensaje-exito');
    const boleta = document.getElementById('boleta');
    const totalBoleta = document.getElementById('total-boleta');

    btnPagar.addEventListener('click', function() {
        // Mostrar mensaje de compra exitosa
        mensajeExito.style.display = 'block';

        // Limpiar la boleta actual
        boleta.innerHTML = '';

        // Calcular y mostrar la boleta
        let total = 0.0;
        cart.forEach(item => {
            const li = document.createElement('li');
            li.textContent = `${item.name} - $${item.price.toFixed(2)}`;
            boleta.appendChild(li);
            total += parseFloat(item.price);
        });
        totalBoleta.textContent = total.toFixed(2);
        
        // Limpiar el carrito después de pagar (opcional)
        cart = [];
        totalPrice = 0.0;
        updateCartUI();
    });
});
