#  Définition de Classe(s)
class BasketTeam:
    fine_account = 50_000
    number_of_teams = 0

    # Méthodes d'instance
    def __init__(self, name, wins, loses):
        self.name = name
        self.wins = wins
        self.loses = loses
        self.totalfines = 0
        BasketTeam.number_of_teams += 1

    @classmethod
    def from_string(cls, stats_as_string):
        return cls.split()

    def get_fined(self):
        self.totalfines += BasketTeam.fine_account

    def stats(self):
        return f"[Stats]: Nom d'équipe: {self.name} Nombre de victoires: {self.wins} Nombre de défaites: {self.loses}"

    # Méthodes de Classe
    @classmethod
    def set_fine_account(cls, amount):
        cls.fine_account = amount
        print(cls)

    @classmethod
    def split(cls):
        pass


# Programme Principal

L_A = BasketTeam("Los Angeles Lakers", 23, 5)
Warriors = BasketTeam("GOlden states Warriors", 32, 3)

BasketTeam.set_fine_account(75000)

print(BasketTeam.fine_account)
print(L_A.totalfines)
for i in range(2):
    L_A.get_fined()
print(L_A.totalfines)

print(L_A.stats())

BasketTeam.from_string("Red Cavaliers-18-6")