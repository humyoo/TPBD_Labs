from user import User
from subscription import Subscription
from video import Video
from genre import Genre
from view import View
from db_setup import create_session

def show_menu():
    print("1. Показати всі жанри")
    print("2. Показати всі підписки")
    print("3. Показати всі відео")
    print("4. Показати всіх користувачів")
    print("5. Показати всі перегляди")
    print("6. Вийти")

def print_table_data(query):
    for row in query:
        print(row)

def main():
    session = create_session()

    while True:
        show_menu()
        choice = input("Виберіть опцію: ")

        if choice == '1':
            print("Жанри:")
            print_table_data(session.query(Genre).all())
        elif choice == '2':
            print("Підписки:")
            print_table_data(session.query(Subscription).all())
        elif choice == '3':
            print("Відео:")
            print_table_data(session.query(Video).all())
        elif choice == '4':
            print("Користувачі:")
            print_table_data(session.query(User).all())
        elif choice == '5':
            print("Перегляди:")
            print_table_data(session.query(View).all())
        elif choice == '6':
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
