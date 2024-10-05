def print_rangoli(size):
    # your code goes here
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    
    for i in range(1, 2*size):
        index = size-i
        pattern = alphabets[index:size][::-1]
        if (i>size):
            pattern = alphabets[-index:size][::-1]
        pattern += pattern[:-1][::-1]
        
        line = "-".join(pattern)
        print(line.center(4*size-3,"-"))   

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)