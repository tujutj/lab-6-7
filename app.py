from flask import Flask, render_template, request
import os
import datetime

app = Flask(__name__)

# Директорія для збереження записів
BOOKING_DIR = "bookings"

# Створюємо директорію, якщо її не існує
if not os.path.exists(BOOKING_DIR):
    os.makedirs(BOOKING_DIR)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/booking')
def booking_form():
    return render_template('booking.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/price-list')
def price():
    return render_template('price-list.html')


@app.route('/submit', methods=['POST'])
def submit_booking():
    """Обробка даних запису"""
    # Отримуємо дані з форми
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    service = request.form.get('service')
    appointment_date = request.form.get('appointment_date')

    # Формуємо текст для запису у файл
    booking_text = f"""
    Запис до салону:
    -------------------------
    Ім'я клієнта: {name}
    Email: {email}
    Телефон: {phone}

    Послуга: {service}
    Дата і час запису: {appointment_date}

    Дата і час створення заявки: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    -------------------------
    """

    # Формуємо ім'я файлу
    filename = f"{BOOKING_DIR}/{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

    # Записуємо дані у текстовий файл
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(booking_text)

    # Повертаємо успішну відповідь
    return '', 200


if __name__ == '__main__':
    app.run(debug=True)
