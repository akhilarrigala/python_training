def fibo_series(stop=10):
    cur, next = 0, 1
    for i in range(stop):
        term = cur
        yield term
        cur, next = next, cur + next

for term in fibo_series():
    print(term, end = ' ')
