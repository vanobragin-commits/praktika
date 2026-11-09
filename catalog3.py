import json

books = []


def load():
    try:
        with open("catalog.json", encoding="utf-8") as file:
            books.extend(json.load(file))
    except FileNotFoundError:
        pass


def save():
    with open("catalog.json", "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False)


def find(book_id):
    for book in books:
        if book[0] == book_id:
            return book
    return None


def add(book_id, title, author, kind):
    if book_id == "" or find(book_id):
        return False
    books.append([book_id, title, author, kind])
    return True


def delete(book_id):
    book = find(book_id)
    if book:
        books.remove(book)
        return True
    return False


def main():
    load()
    while True:
        choice = input("\n1 найти по ID, 2 добавить, 3 удалить, 4 все, 0 выход: ")
        if choice == "0":
            break
        elif choice == "1":
            print(find(input("ID: ")) or "Не найдено")
        elif choice == "2":
            if add(input("ID: "), input("Название: "), input("Автор: "), input("Тип: ")):
                print("Добавлено")
                save()
            else:
                print("Ошибка: ID пустой или уже занят")
        elif choice == "3":
            if delete(input("ID: ")):
                print("Удалено")
                save()
            else:
                print("ID не найден")
        elif choice == "4":
            for book in books:
                print(book)


if __name__ == "__main__":
    main()
