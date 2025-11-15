import unittest
from csv_reader import (
    charger_csv,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException
)

class TestCSV(unittest.TestCase):

    def test_csv_valide(self):
        """CSV normal avec trois articles."""

    def test_fichier_absent(self):
        """Doit lever FichierIntrouvableException."""
        with self.assertRaises(FichierIntrouvableException):
            charger_csv("fichier_qui_n_existe_pas.csv")

    def test_prix_texte(self):
        """Ligne avec prix non numérique ('abc')."""

    def test_prix_negatif(self):
        """Ligne avec prix < 0."""


if __name__ == "__main__":
    unittest.main()
