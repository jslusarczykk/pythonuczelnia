class Telephone():
    def __init__(self,country,gender,number):
        self.country = country
        self.gender = gender
        self.number = number
        self.owners = 1
        self.is_rooted = False
    def root(self):
        self.is_rooted = True
    def nroot(self):
        self.is_rooted = False
    def change_owner(self,owner):
        self.owners +=1

telephone = Telephone(
        "Poland",
        "male",578001830)

print(f"My favourite book is {telephone.title}, ",end="")
print(f"written by {book.author}. ",end="")
print(f"This book has {book.pages} pages.")

book.open()
for i in range(10):
    num=int(input("Podaj numer: "))
    book.change_page(num)
    if book.is_open:
        print(f"Reading the book, page {book.current_page}")
    else:
        print("I am going to read the book later.")
