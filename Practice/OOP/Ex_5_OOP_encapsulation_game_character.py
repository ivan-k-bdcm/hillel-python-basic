class GameCharacter:
    _MAX_HEALTH= 100
    _MAX_MANA = 100


    def __init__(self):
        self._health = self._MAX_HEALTH
        self._mana = self._MAX_MANA

    @property
    def health(self):
        return self._health


    @property
    def mana(self):
        return self._mana

    @property
    def max_health(self):
        return self._MAX_HEALTH


    def take_damage(self, damage):
        self._health = max(0, self._health - damage)


    def heal(self, healing):
        self._health = min(self._MAX_HEALTH, self.health + healing)


    def use_mana(self, mana):
        self._mana = max(0, self._mana - mana)


    @property
    def get_info(self):
        return f'Health: {self._health}\nMana: {self._mana}\nMax health: {self._MAX_HEALTH}\n'



player1 = GameCharacter()
print(player1.get_info)

player1.take_damage(5)
print(player1.get_info)

player1.use_mana(25)
print(player1.get_info)

player1.heal(100)
print(player1.get_info)

player1.take_damage(300)
print(player1.get_info)


player2 = GameCharacter()
print(player2.get_info)