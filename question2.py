ind=0
def compressed(string):

    global ind
    comp_str = ""
    len_str = len(string)
    while (ind != len_str):
        count = 1

        while ((ind < (len_str - 1)) and (string[ind] == string[ind + 1])):
            count = count + 1
            ind = ind + 1

        if (count == 1):
            comp_str = comp_str + str(string[ind])
        else:
            comp_str = comp_str + str(string[ind]) + str(count)

        ind = ind + 1

    return comp_str




def decompressed(decstr):
    a=[]
    a=list(decstr)
    r=[]
    r= a[1::2]
    k= list(map(int, r))
    a=[v for i, v in enumerate(a) if i % 2 == 0]
    c=[]
    for i in range(len(a)):
        c += [a[i]] * k[i]
    final=''.join([str(elem) for elem in c])
    return final


string = input("Enter the text to compress: ")
decstr=input("Enter the compressed text to decompress: ")

print(compressed(string))
print(decompressed(decstr))