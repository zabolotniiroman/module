import csv
import matplotlib.pyplot as plt
from collections import Counter

class LibraryApp:
    def __init__(self):
        self.data = []

    def load_csv(self):
        """Завантаження даних із CSV-файлу"""
        file_path = input("Введіть шлях до CSV файлу: ")
        try:
            with open(file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                self.data = [row for row in reader]
            print("Файл успішно завантажено!")
        except Exception as e:
            print(f"Помилка: Не вдалося завантажити файл: {e}")
    def save_csv(self):
        """Збереження даних у CSV-файл"""
        file_path = input("Введіть шлях для збереження CSV файлу: ")
        try:
            with open(file_path, mode="w", encoding="utf-8", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.data[0].keys())
                writer.writeheader()
                writer.writerows(self.data)
            print("Файл успішно збережено!")
        except Exception as e:
            print(f"Помилка: Не вдалося зберегти файл: {e}")
    def add_book(self):
        """Додавання нової книги"""
        title = input("Введіть назву книги: ").capitalize()
        author = input("Введіть автора книги: ").capitalize()
        year = input("Введіть рік видання: ")
        genre = input("Введіть жанр книги: ").capitalize()
        
        while True:
            quantity = input("Введіть кількість примірників: ")
            try:
                quantity = int(quantity)
                if quantity < 0:
                    print("Кількість не може бути від'ємною. Спробуйте ще раз.")
                else:
                    break
            except ValueError:
                print("Неправильний формат для кількості! Спробуйте ще раз.")
        self.data.append({
            "Назва книги": title,
            "Автор": author,
            "Рік видання": year,
            "Жанр": genre,
            "Кількість примірників": quantity
        })
        print(f"Книга '{title}' додана!")
    def edit_book(self):
        """Редагування інформації про книгу"""
        title = input("Введіть назву книги для редагування: ").lower()
        book = next((book for book in self.data if book["Назва книги"].lower() == title), None)
        if book:
            print(f"Редагуємо: {book}")
            book["Назва книги"] = input("Введіть нову назву: ").capitalize()
            book["Автор"] = input("Введіть нового автора: ").capitalize()
            book["Рік видання"] = input("Введіть новий рік видання: ")
            book["Жанр"] = input("Введіть новий жанр: ").capitalize()
            
            while True:
                quantity = input("Введіть нову кількість примірників: ")
                try:
                    quantity = int(quantity)
                    if quantity < 0:
                        print("Кількість не може бути від'ємною. Спробуйте ще раз.")
                    else:
                        break
                except ValueError:
                    print("Неправильний формат для кількості! Спробуйте ще раз.")
                
            book["Кількість примірників"] = quantity
            print(f"Книга '{title}' оновлена!")
        else:
            print(f"Книга '{title}' не знайдена!")
    def delete_book(self):
        """Видалення книги за назвою"""
        title = input("Введіть назву книги для видалення: ")
        new_data = [book for book in self.data if book["Назва книги"].lower() != title.lower()]
        if len(new_data) < len(self.data):
            self.data = new_data
            print(f"Книга '{title}' видалена!")
        else:
            print(f"Книга '{title}' не знайдена!")

    def show_table(self):
        """Виведення списку книг у вигляді таблиці"""
        if not self.data:
            print("Немає даних для відображення!")
            return
        print(f"{'Назва книги':<30}{'Автор':<20}{'Рік видання':<15}{'Жанр':<20}{'Кількість примірників':<10}")
        for book in self.data:
            print(f"{book['Назва книги']:<30}{book['Автор']:<20}{book['Рік видання']:<15}{book['Жанр']:<20}{book['Кількість примірників']:<10}")

    def total_books(self):
        """Обчислення загальної кількості книг у бібліотеці"""
        total = sum(int(book["Кількість примірників"]) for book in self.data)
        print(f"Загальна кількість книг у бібліотеці: {total}")

    def popular_genres(self):
        """Виведення списку найпопулярніших жанрів"""
        genres = [book["Жанр"] for book in self.data]
        genre_counts = Counter(genres)
        print("Найпопулярніші жанри:")
        for genre, count in genre_counts.items():
            print(f"{genre}: {count}")

    def search_books(self):
        """Пошук книг певного автора або книг, виданих у конкретному році"""
        search_type = input("Пошук за автором (1) або роком видання (2)? Введіть 1 або 2: ")
        if search_type == "1":
            author = input("Введіть автора: ").capitalize()
            books_by_author = [book for book in self.data if book["Автор"].capitalize() == author]
            if books_by_author:
                print(f"Книги автора {author}:")
                for book in books_by_author:
                    print(f"{book['Назва книги']} ({book['Рік видання']})")
            else:
                print(f"Книги автора {author} не знайдено.")
        elif search_type == "2":
            year = input("Введіть рік видання: ")
            books_by_year = [book for book in self.data if book["Рік видання"] == year]
            if books_by_year:
                print(f"Книги, видані у {year} році:")
                for book in books_by_year:
                    print(f"{book['Назва книги']} ({book['Автор']})")
            else:
                print(f"Книги, видані у {year} році, не знайдено.")
        else:
            print("Невірний вибір. Спробуйте ще раз.")

    def plot_pie_chart(self):
        """Кругова діаграма розподілу книг за жанрами"""
        if not self.data:
            print("Немає даних для діаграми.")
            return
        genres = [book["Жанр"] for book in self.data]
        genre_counts = Counter(genres)

        plt.pie(genre_counts.values(), labels=genre_counts.keys(), autopct="%1.1f%%")
        plt.title("Розподіл книг за жанрами")
        plt.show()

    def plot_histogram(self):
        """Гістограма кількості книг за роками видання"""
        if not self.data:
            print("Немає даних для гістограми.")
            return
        years = [int(book["Рік видання"]) for book in self.data]

        plt.hist(years, bins=10, edgecolor="black")
        plt.title("Гістограма кількості книг за роками видання")
        plt.xlabel("Рік видання")
        plt.ylabel("Кількість книг")
        plt.show()

def menu():
    app = LibraryApp()
    while True:
        print("1. Завантажити CSV файл")
        print("2. Зберегти CSV файл")
        print("3. Додати книгу")
        print("4. Редагувати книгу")
        print("5. Видалити книгу")
        print("6. Показати дані (таблиця)")
        print("7. Загальна кількість книг у бібліотеці")
        print("8. Найпопулярніші жанри")
        print("9. Пошук книг")
        print("10. Кругова діаграма розподілу книг за жанрами")
        print("11. Гістограма кількості книг за роками видання")
        print("12. Вийти")
        choice = input("Оберіть опцію (1-12): ")

        if choice == "1":
            app.load_csv()
        elif choice == "2":
            app.save_csv()
        elif choice == "3":
            app.add_book()
        elif choice == "4":
            app.edit_book()
        elif choice == "5":
            app.delete_book()
        elif choice == "6":
            app.show_table()
        elif choice == "7":
            app.total_books()
        elif choice == "8":
            app.popular_genres()
        elif choice == "9":
            app.search_books()
        elif choice == "10":
            app.plot_pie_chart()
        elif choice == "11":
            app.plot_histogram()
        elif choice == "12":
            print("Програма закінчена!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")
menu()