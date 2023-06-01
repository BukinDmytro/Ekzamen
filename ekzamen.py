##2 3
class Book():
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def get_info(self):
        print(f"Назва: {self.title} , Автор: {self.author}")
book = Book("2014" , "Джордж Белфорд")
book.get_info()