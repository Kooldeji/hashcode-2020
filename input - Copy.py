books = []
noScanDays = 0
scanned = set()


class Library:
    def __init__(self, id, libBooks, signupTime, booksPerDay):
        self.id = id
        self.books = libBooks
        self.signupTime = signupTime
        self.booksPerDay = booksPerDay

    def score(self, step, days):
        if days - (step + self.signupTime) <= 0: return -1

        return self.booksPerDay * (2 * (days - (step + self.signupTime)))
        # score = 0
        # remDays = days - step
        # if self.signupTime >= remDays: return -1
        # remDays -= self.signupTime
        # scannable = remDays * self.booksPerDay
        #
        # i = j = 0
        # while i <= scannable and j != len(self.books):
        #     if self.books[j] not in scanned:
        #         score += books[self.books[j]]
        #         self.books[i], self.books[j] = self.books[j], self.books[i]
        #         i += 1
        #     j += 1
        # return score

    def select(self, step):
        global scanned
        daysToScan = (noScanDays - step) - self.signupTime
        for i in range(min(daysToScan * self.booksPerDay, len(self.books))):
            scanned.add(self.books[i])

        return step + self.signupTime


def selectLibraries(libs):
    selectedLibraries = []
    currentStep = 0
    while currentStep < noScanDays:
        if len(libs) == 0:
            break
        maxLibScore = 0
        maxLib = None
        for lib in libs:
            score = lib.score(currentStep, noScanDays)
            if score >= maxLibScore:
                maxLibScore = score
                maxLib = lib
        if maxLib:
            currentStep = maxLib.select(currentStep)
            libs.remove(maxLib)
            selectedLibraries.append(maxLib)
        else:
            break
    return selectedLibraries


def main(fileName, idx):
    global books, noScanDays, scanned
    scanned = set()
    file = open(fileName + ".txt")
    noBooks, noLibs, noScanDays = map(int, file.readline().split(" "))
    books = list(map(int, file.readline().split(" ")))
    libs = set()
    for libId in range(noLibs):
        noBooks, signupTime, booksPerDay = map(int, file.readline().split(" "))
        libBooks = list(map(int, file.readline().split(" ")))
        libBooks.sort(key=lambda b: books[b], reverse=True)
        lib = Library(libId, libBooks, signupTime, booksPerDay)
        libs.add(lib)
    print('Started ' + fileName)
    outputLibs = selectLibraries(libs)
    # outputLibs = sorted(libs, key=lambda x: x.booksPerDay)
    submit(outputLibs, fileName, idx)


def submit(outputLibs, fileName, idx):
    file = open(idx + "_" + fileName + ".txt", "w")
    print(len(outputLibs), file=file)
    for lib in outputLibs:
        print(lib.id, len(lib.books), file=file)
        for b in range(len(lib.books) - 1):
            book = lib.books[b]
            print(book, file=file, end=" ")
        print(lib.books[-1], file=file)


itr = 4
# files = ['a_example']
# files = ['b_read_on']
# files = ['c_incunabula']
files = ['d_tough_choices']
# files = ['e_so_many_books']
# files = ['f_libraries_of_the_world']
# files = ['a_example', 'b_read_on', 'c_incunabula', 'd_tough_choices', 'e_so_many_books', 'f_libraries_of_the_world']
#files = ['a_example', 'b_read_on', 'c_incunabula', 'e_so_many_books', 'f_libraries_of_the_world']
for file in files:
    main(file, 'out_' + str(itr))
