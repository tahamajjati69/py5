from csv_reader import (
    charger_csv,
    CsvException,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException
)

def main():
    chemin = "articles.csv"  

    try:
        articles = charger_csv(chemin)
        print("Import effectué avec succès.")
        print(articles)

    except FichierIntrouvableException:
        print("Erreur : fichier introuvable.")
    
    except LigneInvalideException:
        print("Erreur : format de ligne incorrect.")

    except PrixNegatifException:
        print("Erreur : prix invalide (non numérique ou négatif).")

    except CsvException as e:
        print("Erreur CSV générale :", e)

if __name__ == "__main__":
    main()
