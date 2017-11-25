from ModelApp import App
from start import app

def main():
    aapp = App()
    with app.app_context():
        aapp = aapp.search_by_id(1)
        print(aapp.etext)

if __name__ == '__main__':
    main()