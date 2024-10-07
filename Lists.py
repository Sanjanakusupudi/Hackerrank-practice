if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        command, *arg = input().split()
        
        if(command.lower() == 'insert'):
            list.insert(int(arg[0]),int(arg[1]))
        if(command.lower() == 'print'):
            print(list)
        if(command.lower() == 'remove'):
            list.remove(int(arg[0]))
        if(command.lower() == 'append'):
            list.append(int(arg[0]))
        if(command.lower() == 'sort'):
            list.sort()
        if(command.lower() == 'pop'):
            list.pop()
        if(command.lower() == 'reverse'):
            list.reverse()
