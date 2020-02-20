class Library:
    def __init__(self, libBooks, signupTime, booksPerDay):
        self.books = libBooks
        self.signupTime = signupTime
        self.booksPerDay = booksPerDay


books = []
libs = []


def main(fileName):
    global books, noScanDays
    file = open(fileName)
    noBooks, noLibs, noScanDays = map(int, file.readline().split(" "))
    books = list(map(int, file.readline().split(" ")))
    for _ in noLibs:
        noBooks, signupTime, booksPerDay = map(int, file.readline().split(" "))
        libBooks = list(map(int, file.readline().split(" ")))
        libBooks.sort(key=lambda b: books[b], reverse=True)
        lib = Library(libBooks, signupTime, booksPerDay)
        libs.append(lib)
    ouput = selectLibs(libs)

print(1)
