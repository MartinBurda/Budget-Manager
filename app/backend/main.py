# Importy
from app.backend.cashFlow import createDatabase
from app.frontend.index import run_gui

def main():
    """
    Metoda pro main.py (s inicializací databáze)
    """
    createDatabase()

    # GUI pro budget manager
    run_gui()


# Propojení s main.py
if __name__ == "__main__":
    main()

