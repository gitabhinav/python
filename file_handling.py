
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


file_handle = file_open('E:/ping.txt')
    
fileread = file_read(file_handle)
print(fileread)
file_close(file_handle)
                        
        


