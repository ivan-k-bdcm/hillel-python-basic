class Email:
    def __init__(self, u_email):
        self.email = u_email



    @property
    def email(self):
        return self._email




    @email.setter
    def email(self, value):
        if '@' in value and '.' in value:
            self._email = value
        else:
            raise ValueError(
                "Email must be in format: email@mail.com"
            )



email = Email("ajax@google.com")
print(email.email)

email.email = "ajax"