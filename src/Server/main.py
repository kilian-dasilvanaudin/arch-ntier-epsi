
from store import Store
from user import User
from menu import Menu
from persist import PersistJson
from application import Application
from server import Server

if __name__ == '__main__':
    persist = PersistJson()
    application = persist.load()
    if application == None:
        user = User(name='user1')
        store = Store()
        application = Application(store, user, persist)
    menu = Menu(application)
    server = Server(menu)
    server.run()

