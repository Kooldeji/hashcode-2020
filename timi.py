noScannedDays = 0
libs = []
books = []
scanned = set()

class Library:

    def __init__(self, libBooks, signupTime, booksPerDay):
        self.books = libBooks
        self.signupTime = signupTime
        self.booksPerDay = booksPerDay

    def selectLibrary(self, step):
        daysToScan = (noScannedDays - step) - self.signupTime
        for i in range(min(daysToScan * self.booksPerDay, len(self.books))):
            scanned.add(self.books[i])

        return step + self.signupTime




