from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if len(username) < 3:
            raise UserInputError("Username is too short, it should be at least 3 characters long")

        hyvaksytyt_kirjaimet = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
        for i in range(len(username)):
            if username[i] not in hyvaksytyt_kirjaimet:
                raise UserInputError("Invalid username, it should only contain letters from a-z")
        
        if len(password) < 8:
            raise UserInputError("Password is too short, it should be at least 8 characters long")

        number_counter = 0
        for i in range(len(password)):
            if password[i] in "1234567890":
                number_counter = 1
                break
        if number_counter == 0:
            raise UserInputError("Invalid password, it should contain at least 1 number")

        user = self._user_repository.find_by_username(username)
        if user:
            raise UserInputError("Username is already taken")
