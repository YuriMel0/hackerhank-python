num = int(input().strip())

if num % 2 == 1:
    print("Weird")
elif num % 2 == 0:
    print("Not Weird") if ((num >= 2 and num <= 5) or (num > 20)) else print("Weird")
    
    