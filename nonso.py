class Library:
    def __init__(self, id, libBooks, signupTime, booksPerDay):
        self.id = id
        self.books = libBooks
        self.signupTime = signupTime
        self.booksPerDay = booksPerDay

    def libraryScore(self, step, days):
        score = 0
        remDays = days - step
        if self.signupTime >= remDays: return -1
        remDays -= self.signupTime
        scannable = remDays * self.booksPerDay

        i = j = 0
        while i <= scannable and j != len(self.books):
            if self.books[j] not in scanned:
                score += books[self.books[j]]
                self.books[i], self.books[j] = self.books[j], self.books[i]
                i += 1
            j += 1
        self.books = self.books[:i+1]
        return score

    def select(self, step):
        global scanned
        daysToScan = (noScanDays - step) - self.signupTime
        for i in range(min(daysToScan * self.booksPerDay, len(self.books))):
            scanned.add(self.books[i])

        return step + self.signupTime
