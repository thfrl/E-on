doc_q = int(input("작업 수 : "))
doc_n = int(input("작업 번호 : "))
priority = list(map(int, input("작업 우선순위 : ").split(' ')))
priority = [(i, idx) for idx, i in enumerate(priority)]

count = 0
while True:
    if priority[0][0] == max(priority, key = lambda x : x[0])[0]:
        count += 1
        if priority[0][1] == doc_n:
            print(count,"분")
            break
        else:
            priority.pop(0)
    else:
        priority.append(priority.pop(0))