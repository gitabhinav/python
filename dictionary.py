def read_file(filename):
    import string
    
    try:
        fhandle = open(filename)

    except:
        print("Error opening file",filename,"file not found")
        
    filedata = []
    listofwords = []
    for line in fhandle:
        line = line.translate(str.maketrans("","",string.punctuation))
        line = line.lower()
        listofwords.append(line.split())
    return listofwords

def createdictonary(listofwords):
    
    counts = dict() 
    for item in listofwords:
        for word in item:
            for char in word:
                if char not in counts:
                    counts[char]= 1
                else:
                    counts[char] +=1
    sumval = 0
    for lkey, lval in counts.items():
        sumval = sumval + int(lval)

    wordfreq = []
    for lkey, lval in counts.items():
        wordfreq.append((lkey, (str((lval/sumval)*100))+"%"))

    wordfreq.sort()    
    return wordfreq

print(createdictonary(read_file("E:/news.txt")))
