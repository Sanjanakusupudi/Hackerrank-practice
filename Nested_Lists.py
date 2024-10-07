if __name__ == '__main__':
    arr = []
    dict1 = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
   
    arr.sort(key=lambda e:e[1])
    
    unique_score = set()
    for name,score in arr:
        if score not in unique_score:
            unique_score.add(score)
    sorted_scores = sorted(unique_score)
    
    second_largest = sorted_scores[1]
    
    names = []
    for i in arr:
        if(i[1] == second_largest):
            names.append(i[0])
    
    names.sort()
    [print(name) for name in names]
