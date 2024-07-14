document.addEventListener('DOMContentLoaded', function() {
    const formLogin = document.getElementById('formlogin');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    const btnServices = document.getElementById('btn-services');
  
    formLogin.addEventListener('submit', function(event) {
      event.preventDefault();
      
      if (usernameInput.value === '' || passwordInput.value === '') {
        showToast('Por favor, completa todos los campos.');
      } else {
        // Realizar la solicitud de inicio de sesión mediante AJAX
        const formData = new FormData(formLogin);
        fetch(formLogin.action, {
          method: 'POST',
          body: formData,
          headers: {
            'X-CSRFToken': getCookie('csrftoken')
          }
        })
        .then(response => {
          if (!response.ok) {
            throw new Error('Error en la solicitud.');
          }
          return response.json();
        })
        .then(data => {
          // Si el inicio de sesión es exitoso, mostrar el botón de servicios y redirigir a index.html
          btnServices.classList.remove('d-none');
          window.location.replace("{% url 'index' %}");
        })
        .catch(error => {
          showToast('Error en el inicio de sesión.');
          console.error(error);
        });
      }
    });
  
    function showToast(message) {
      const toastContainer = document.getElementById('toastContainer');
      const toastElement = document.createElement('div');
      toastElement.classList.add('toast');
      toastElement.setAttribute('role', 'alert');
      toastElement.setAttribute('aria-live', 'assertive');
      toastElement.setAttribute('aria-atomic', 'true');
  
      const toastBody = document.createElement('div');
      toastBody.classList.add('toast-body');
      toastBody.textContent = message;
  
      toastElement.appendChild(toastBody);
      toastContainer.appendChild(toastElement);
  
      const bootstrapToast = new bootstrap.Toast(toastElement);
      bootstrapToast.show();
    }
  
    // Función para obtener el valor de la cookie CSRF
    function getCookie(name) {
      const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
      return cookieValue ? cookieValue.pop() : '';
    }
  });