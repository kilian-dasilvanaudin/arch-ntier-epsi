from menu import Menu

if __name__ == '__main__':
    menu = Menu()
    while True:
        Menu.prompt()
        selection = input('Action: ')
        menu._main_entries[selection]()