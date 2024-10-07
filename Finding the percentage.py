if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    value = student_marks[query_name]
    result = (value[0]+value[1]+value[2])/3
    print(format(result,".2f"))
        
        
