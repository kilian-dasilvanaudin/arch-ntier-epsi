
from store import Store
from user import User
from menu import Menu
from persist import PersistJson

if __name__ == '__main__':
	user = User(name='user1')
	store = Store()
	
	persist = PersistJson()
	menu = persist.load()
	if menu == None:
		menu = Menu(store, user)
	while True:
		Menu.prompt()
		selection = input()
		menu._main_entries[selection]()
		persist.save(menu)
