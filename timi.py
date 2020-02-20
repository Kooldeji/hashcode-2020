class Library:
    def __init__(self, libBooks, signupTime, booksPerDay):
        self.books = libBooks
        self.signupTime = signupTime
        self.booksPerDay = booksPerDay

    def select(self, step):
        global scanned
        daysToScan = (noScanDays - step) - self.signupTime
        for i in range(min(daysToScan * self.booksPerDay, len(self.books))):
            scanned.add(self.books[i])

        return step + self.signupTime



print("timi")

