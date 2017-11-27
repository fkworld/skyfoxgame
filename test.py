from ModelApp import App
from start import app

def main():
    aapp = App()
    with app.app_context():
        aapps = aapp.search_all()
        print(aapps)
        aapp.order_by_sequence(aapps)
        print(aapps)

if __name__ == '__main__':
    main()