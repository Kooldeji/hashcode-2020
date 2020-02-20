# books
# noScanDays


def selectLibraries(libs):
    selectedLibraries = []
    currentStep = 0
    while currentStep < noScanDays:
        if len(libs) == 0:
            break
        maxLibScore = 0
        maxLib = None
        for lib in libs:
            score = lib.score()
            if score >= maxLibScore:
                maxLibScore = score
                maxLib = lib
        if maxLib:
            currentStep = maxLib.select()
            libs.remove(maxLib)
            selectedLibraries.append(maxLib)
        else:
            break
    return selectedLibraries


files = ['a_example', 'b_read_on', 'c_incunabula', 'd_tough_choices', 'e_so_many_books', 'f_libraries_of_the_world']
for file in files:
    main(file)
