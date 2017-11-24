from ModelApp import App
from start import app

def main():
    aapp = App()
    aapp.id = 1
    aapp.ename = 'Magic iNvert'
    aapp.get_icon_filename()
    with app.app_context():
        aapp.set_icon_url()

if __name__ == '__main__':
    main()