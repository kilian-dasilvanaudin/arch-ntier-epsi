from game import GameNone

class Menu:
    def __init__(self, application):
        self._application = application
        self._main_entries = {
            '1': self.displayGames,
            '2': self.addComment,
            '3': self.detailGame,
            '4': self.removeGame,
            '5': self.createGame,
            '6': self.deleteGame,
            '7': self.buyGame,
            '8': self.displayGamesInStore
        }

    def displayGamesInStore(self, parameters):
        result = 'List of games in store'
        result += str(self._application._store)
        return result


    def detailGame(self, parameters):
        name = parameters['name']
        game_selected = GameNone()
        for game in self._application._store._games:
            if game._name == name:
                game_selected = game
                break
        result = ''
        for comment in game_selected._comments:
            result += comment + '\n'
        return result
    
    def addComment(self, parameters):
        name = parameters['name']
        comment = parameters['comment']
        grade = parameters['grade']
        game_selected = GameNone()
        for game in self._application._user._lib._games:
            if game._name == name:
                game_selected = game
                break
        return game_selected.addComment(self._user, comment, grade)

    def removeGame(self, parameters):
        name = parameters['name']
        game_to_delete = GameNone()
        for game in self._application._store._games:
            if game._name == name:
                game_to_delete = game
                break
        self._application._store.removeGame(game_to_delete)
        return True
    
    def deleteGame(self, parameters):
        name = parameters['name']
        game_to_delete = GameNone()
        for game in self._application._user._lib._games:
            if game._name == name:
                game_to_delete = game
                break
        self._application._user._lib.removeGame(game_to_delete)
        return True

    def displayGames(self, parameters):
        result = 'List of games'
        result += str(self._application._user._lib)
        return result
    
    def createGame(self, parameters):
        name = parameters['name']
        tag = parameters['tag']
        price = parameters['price']
        image = parameters['image']
        self._application._store.createGame(name, tag, image, price)
        return 'Game created'

    def buyGame(self, parameters):
        name = parameters['name']
        self._application._store.buyGame(name, self._user)
        return True
