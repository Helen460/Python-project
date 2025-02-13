#Консольний застосунок "База даних магазину продуктів"
import os

#Ініціалізація списку для збереження даних про продукти
products = []

#Функція для завантаження даних з файлу
def load_from_file():
    global products
    try:
        #Перевірка, чи існує файл
        if os.path.exists('products.txt'):
            with open('products.txt', 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    #Обробка кожного рядка файлу та розділення даних на частини
                    product_data = line.strip().split(', ')
                    #Додавання продукту в список
                    products.append([product_data[0], product_data[1], float(product_data[2]), int(product_data[3])])
    except Exception as e:
        #Повідомлення про помилку при завантаженні
        print("Помилка при завантаженні даних з файлу:", e)

#Функція для збереження даних у файл
def save_to_file():
    try:
        with open('products.txt', 'w', encoding='utf-8') as f:
            for product in products:
                #Запис кожного продукту у файл, розділеного комами
                f.write(', '.join(map(str, product)) + '\n')
        print("База даних збережена у файл.")
    except Exception as e:
        #Повідомлення про помилку при збереженні
        print("Помилка при збереженні даних у файл:", e)

#Функція для додавання нового продукту
def add_product():
    name = input("Введіть назву продукту: ")
    category = input("Введіть категорію продукту: ")

    #Перевірка правильності введення ціни
    while True:
        try:
            price = float(input("Введіть ціну продукту: "))
            break
        except ValueError:
            print("Помилка! Ціна повинна бути числом.")

    #Перевірка правильності введення кількості
    while True:
        try:
            quantity = int(input("Введіть кількість на складі: "))
            break
        except ValueError:
            print("Помилка! Кількість повинна бути цілим числом.")
    
    #Додавання нового продукту до списку
    products.append([name, category, price, quantity])
    print("Продукт", name, "додано в базу даних.")

#Функція для перегляду всіх продуктів у зручному вигляді
def view_products():
    if len(products) == 0:
        print("База даних порожня.")
    else:
        print("\nСписок продуктів:")
        #Форматоване виведення заголовків таблиці
        print("{:<20} {:<20} {:<10} {:<10}".format("Назва", "Категорія", "Ціна", "Кількість"))
        print('-' * 60)
        for product in products:
            #Форматоване виведення даних кожного продукту
            print("{:<20} {:<20} {:<10.2f} {:<10}".format(product[0], product[1], product[2], product[3]))

#Функція для пошуку продукту за назвою
def find_product():
    name = input("Введіть назву продукту для пошуку: ")
    found = False
    for product in products:
        if product[0].lower() == name.lower():
            print("\nЗнайдений продукт:")
            #Форматоване виведення заголовків таблиці
            print("{:<20} {:<20} {:<10} {:<10}".format("Назва", "Категорія", "Ціна", "Кількість"))
            print('-' * 60)  # Лінія розділення
            #Форматоване виведення знайденого продукту
            print("{:<20} {:<20} {:<10.2f} {:<10}".format(product[0], product[1], product[2], product[3]))
            found = True
            break
    if not found:
        print("Продукт", name, "не знайдено.")

#Функція для видалення продукту
def delete_product():
    name = input("Введіть назву продукту для видалення: ")
    global products
    # Видалення продукту з бази даних за назвою
    products = [product for product in products if product[0].lower() != name.lower()]
    print("Продукт", name, "видалено з бази даних.")

#Функція для оновлення даних про продукт
def update_product():
    name = input("Введіть назву продукту для оновлення: ")
    for product in products:
        if product[0].lower() == name.lower():
            print("\nОберіть, що ви хочете змінити для продукту", name, ":")
            print("1. Ціна")
            print("2. Кількість на складі")
            choice = input("Ваш вибір: ")

            #Оновлення ціни
            if choice == "1":
                while True:
                    try:
                        new_price = float(input("Введіть нову ціну: "))
                        product[2] = new_price
                        print("Ціна продукту", name, "оновлена.")
                        break
                    except ValueError:
                        print("Помилка! Ціна повинна бути числом.")
            #Оновлення кількості на складі
            elif choice == "2":
                while True:
                    try:
                        new_quantity = int(input("Введіть нову кількість на складі: "))
                        product[3] = new_quantity
                        print("Кількість продукту", name, "оновлена.")
                        break
                    except ValueError:
                        print("Помилка! Кількість повинна бути цілим числом.")
            else:
                print("Невірний вибір.")
            break
    else:
        print("Продукт", name, "не знайдено.")

#Головне меню програми
def menu():
    while True:
        print("\nМеню:")
        print("1. Переглянути всі продукти")
        print("2. Додати новий продукт")
        print("3. Знайти продукт за назвою")
        print("4. Видалити продукт")
        print("5. Оновити продукт")
        print("6. Зберегти базу даних у файл")
        print("7. Вийти з програми")
        
        choice = input("Оберіть дію: ")

        #Обробка вибору користувача
        if choice == "1":
            view_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            find_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            update_product()
        elif choice == "6":
            save_to_file()
        elif choice == "7":
            save_to_file()
            print("Завершення роботи програми...")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

#Головна функція, що завантажує дані та викликає меню
def main():
    load_from_file()  #Завантаження даних при старті програми
    menu()

#Запуск програми
if __name__ == "__main__":
    main()
