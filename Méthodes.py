# Classe(s)
class BasketTeam:
    # Attribut(s) de classe
    team_fine = 0

    # Constructeur
    def __init__(self, nom, wins, loses, team_fine):
        self.nom = nom
        self.wins = wins
        self.loses = loses
        self.team_fine = team_fine

    # Methode(s)
    def fine(self):
        BasketTeam.team_fine = 50_000 + self.team_fine
        return BasketTeam.team_fine

    @staticmethod
    def Team_stats(self):
        print(
            f"L'équipe {self.nom} a pour Stats de cette saison : Nombre de victoires: {self.wins}, Nombre de Défaites: {self.loses} et elle possède un compte accrédité de {self.fine()} $")


# Programme Principal

# Instanciation de Classe

Lakers = BasketTeam("Los Angeles Lakers", 23, 5, 37_000_000_000)
Golden_State_Warriors = BasketTeam("Golden State Warriors", 32, 3, 41_000_000_000)

# Appel de Méthode
for team in range(3):
    Lakers.fine()
    Golden_State_Warriors.fine()

Lakers.Team_stats()
