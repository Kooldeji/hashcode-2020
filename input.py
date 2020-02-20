import main
import timi

books = []
noScanDays = 0
scanned = {}


def main(fileName, idx):
    global books, noScanDays
    file = open(fileName+".txt")
    noBooks, noLibs, noScanDays = map(int, file.readline().split(" "))
    books = list(map(int, file.readline().split(" ")))
    libs = set()
    for libId in range(len(noLibs)):
        noBooks, signupTime, booksPerDay = map(int, file.readline().split(" "))
        libBooks = list(map(int, file.readline().split(" ")))
        libBooks.sort(key=lambda b: books[b], reverse=True)
        lib = Library(libId, libBooks, signupTime, booksPerDay)
        libs.add(lib)
    outputLibs = selectLibraries(libs)
    submit(outputLibs, fileName, idx)


def submit(outputLibs, fileName, idx):
    file = open(idx+"_"+fileName+".txt", "w")
    for lib in outputLibs:
        print(lib.id, file=file)
        for b in range(len(lib.books)-1):
            book = lib.books[b]
            print(book, file=file, sep=" ")
        print(lib.books[-1], file=file)









