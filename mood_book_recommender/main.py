import json

class Book:
    def __init__(self, title, author, mood):
        self.title = title
        self.author = author
        self.mood = mood

    def display(self):
        print(f"{self.title} by {self.author}")


class BookDatabase:
    def __init__(self, filename):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        with open(self.filename, "r") as file:
            data = json.load(file)

            for item in data:
                book = Book(item["title"], item["author"], item["mood"])
                self.books.append(book)

    def get_books_by_mood(self, mood):
        result = []

        for book in self.books:
            if book.mood == mood:
                result.append(book)

        return result


class RecommendationSystem:
    def __init__(self, database):
        self.database = database

    def ask_user_mood(self):
        print("\nHow are you feeling today?")
        print("happy")
        print("sad")
        print("romantic")
        print("curious")
        print("adventurous")
        print("stressed")

        choice = input("Enter your mood: ").lower()

        return choice

    def recommend_books(self):
        mood = self.ask_user_mood()

        books = self.database.get_books_by_mood(mood)

        if not books:
            print("No books found for this mood.")
            return

        print("\nRecommended Books:\n")

        for book in books:
            book.display()


def main():
    db = BookDatabase("books.json")

    system = RecommendationSystem(db)

    system.recommend_books()


if __name__ == "__main__":
    main()