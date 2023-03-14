from client import Client

class Menu:
    def __init__(self) -> None:
        self._client = Client()
        self._main_entries = {
            '1': self.displayGames,
            '2': self.addComment,
            '3': self.detailGame,
            '4': self.removeGame,
            '5': self.createGame,
            '6': self.deleteGame,
            '7': self.buyGame,
            '8': self.displayGamesInStore,
            '9': self.quit
        }

    @classmethod
    def prompt(cls):
        print('1. Display games')
        print('2. Add comment')
        print('3. Detail game')
        print('4. Remove game')
        print('5. Create game in store')
        print('6. Delete game from store')
        print('7. Buy game')
        print('8. Display games in store')
        print('9. Bye')

    def quit(self):
        print('Bye')
        exit()

    def detailGame(self):
        name = input('name: ')
        self._client.send('3', {'name': name})

    def addComment(self):
        name = input('name: ')
        comment = input('comment: ')
        grade = input('grade(1..5): ')
        self._client.send('2', {'name': name, 'comment': comment, 'grade': grade})

    def removeGame(self):
        name = input('name: ')
        self._client.send('4', {'name': name})

    def deleteGame(self, parameters):
        name = input('name: ')
        self._client.send('6', {'name': name})

    def displayGames(self):
        self._client.send('1', {})

    def createGame(self):
        name = input('name: ')
        tag = input('tag: ')
        price = input('price: ')
        image = input('image: ')
        self._client.send('5', {'name': name, 'tag': tag, 'price': price, 'image': image})

    def buyGame(self):
        name = input('name: ')
        self._client.send('7', {'name': name})

    def displayGamesInStore(self):
        self._client.send('8', {})