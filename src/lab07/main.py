import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.lab07.app import AppManager
from src.lab07.cli import CLI
from src.lab07.storage import load, save

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

def main() -> None:
    app = AppManager()
    raw_data = load(DATA_FILE)
    app.load_data(raw_data)
    print(f"--- Загружено {len(app.get_all())} объектов из базы ---")
    
    cli = CLI(app)
    cli.run()
    save(app.get_raw_data(), DATA_FILE)

if __name__ == "__main__":
    main()