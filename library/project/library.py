# from library.project.user import User


class Library:
    user_records = []
    books_available = {}
    rented_books = {}

    @staticmethod
    def add_user(user) -> str:
        if user in Library.user_records:
            return (
                f"User with id = {user.user_id} "
                f"already registered in the library!"
            )

        Library.user_records.append(user)

    @staticmethod
    def remove_user(user):
        if user not in Library.user_records:
            return f"We could not find such user to remove!"

        Library.user_records.remove(user)

    @staticmethod
    def change_username(user_id: int, new_username: str):
        matched_user_list = [
            user
            for user in Library.user_records
            if user.user_id == user_id
        ]

        if not matched_user_list:
            return f"There is no user with id = {user_id}!"

        matched_user_obj = matched_user_list[0]

        if matched_user_obj.username == new_username:
            return (
                "Please check again the provided username - "
                "it should be different than the username used so far!"
            )

        matched_user_obj.username = new_username
        Library.rented_books = {
            new_username if key == matched_user_obj.username else key: value
            for key, value in Library.rented_books.items()
        }
        return f"Username successfully changed to: {new_username} for userid: {user_id}"

    @staticmethod
    def days_of_rented_books(book_name: str):
        for users, dict_value in Library.rented_books.items():
            for key_book_name, days_left in dict_value.items():
                if book_name == key_book_name:
                    return days_left
