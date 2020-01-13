from view.view_book import ViewBook
from view.input_book import InputBook
from core.search_helper import SearchHelper
from core.baseapp import BaseApp

class MainApp():
    jumlah_book = 0
    def __init__(self):
        self.books = []


if __name__ == "__main__":
    app = MainApp()
    app.run()



    def list_book(self):
        self.view = ViewBook()
        self.view.list()


    def input_book(self):
        self.input = InputBook()
        self.input.input()
        InputBook.jumlah_book += 1


    def search_book(self):
        self.input = InputBook()
        self.input.search()
        self.search_helper = SearchHelper()
        self.search_helper.search_title()
        self.view = SearchHelper()
        self.view.list()


