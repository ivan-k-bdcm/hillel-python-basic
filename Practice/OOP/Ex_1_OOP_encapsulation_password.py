class User:
    def __init__(self, password = ""):
        self.password = password


    @property
    def password(self) -> str:
        return "********"


    @password.setter
    def password(self, value: str):
        if len(value) >= 8:
            self._password = value
        else:
            raise ValueError(
                "Password must be at least 8 characters"
            )



user = User("123іфіфаіфа")
print(user.password)
user.password = "123"