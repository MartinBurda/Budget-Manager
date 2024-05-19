import os
import sys
# Cesty ke backendu
BACKEND_DIR = os.path.join(os.path.dirname(__file__), "backend")
sys.path.append(BACKEND_DIR)

# Cesty ke frontendu
FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "frontend")
sys.path.append(FRONTEND_DIR)

# Nastavení databáze
DATABASE_NAME = "budget_database.sqlite"
DATABASE_PATH = os.path.join(BACKEND_DIR, "budget_database.sqlite")

# Jiné nastavení
