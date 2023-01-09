from collections import  deque
bank=deque(["shafin","ahmed","Mohammad"])
bank.append("sha")
print(bank)
bank.popleft()
print(bank)