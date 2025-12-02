prices = [100,200,300,400,500]


while True:
    choice = int(input("how many items: "))
    if choice <= len(prices):
        break
    print("invalid choice")



total_sum = 0
count = 0

for i in prices:
    if count >= choice:
        break
    total_sum+=i
    count = count +1
print(total_sum)