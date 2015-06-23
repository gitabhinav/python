
def file_open(file_name):
    filename = file_name
    try:
        f_handle = open(file_name)
    except:
        print("Error opening file, please check the file name and path")
    return f_handle

def file_read (fhandle):
    file_data =[]
    f_handle = fhandle
    for line in f_handle:
        file_data.append(line)
        
    return file_data

def file_close(fhandle):
    try:
        fhandle.close()
        rtn = 1
    except:
        print("Error closing file")
        rtn = -1
    return rtn
def uniquelist (file_data):
    uniquewords=[]
    # loop through the file
    for i in range(len(file_data)):  
        #loop through each line
        words = file_data[i].split()
        for j in range(len(words)):
            # pick unique words
            #print("in uniquelist", j, words[j])
            if words[j] in uniquewords :
                continue
            else:
                uniquewords.append(words[j])        
                    
    return uniquewords
            

file_handle = file_open('E:/romeo.txt')
    
fileread = file_read(file_handle)
print(fileread)
un_list = uniquelist(fileread)
un_list.sort()
print(un_list)




file_close(file_handle)
                        
        


