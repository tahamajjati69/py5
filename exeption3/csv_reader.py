

class CsvException(Exception):
    def __init__(self, message):
        super().__init__(message)


class FichierIntrouvableException(CsvException):
    """Fichier CSV introuvable."""
    pass


class LigneInvalideException(CsvException):
    pass


class PrixNegatifException(CsvException):
    pass



def charger_csv(chemin):
  
    
    articles = []

  
    return articles
