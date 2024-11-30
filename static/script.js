document.addEventListener("DOMContentLoaded", () => {
    const fadeElements = document.querySelectorAll(".fade-in");

    const appearOnScroll = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("show");
                observer.unobserve(entry.target);
            }
        });
    });

    fadeElements.forEach(element => {
        appearOnScroll.observe(element);
    });
});
$(document).ready(function () {
    $('#bookingForm').on('submit', function (event) {
        event.preventDefault(); // Зупиняємо перезавантаження сторінки

        // Збираємо дані форми
        const formData = $(this).serialize();

        // Відправка AJAX-запиту на сервер
        $.ajax({
            url: '/submit',
            type: 'POST',
            data: formData,
            success: function () {
                // Ховаємо форму
                $('#bookingForm').hide();

                // Відображаємо повідомлення
                $('#successMessage').fadeIn();
            },
            error: function () {
                alert('Сталася помилка! Будь ласка, спробуйте ще раз.');
            }
        });
    });
});
