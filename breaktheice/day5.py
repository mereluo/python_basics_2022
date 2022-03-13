# Question 16
# num = input("comma-separated numbers: ").split(',')

# result = [str(int(i)*int(i)) for i in num if int(i) % 2 != 0]

# print(','.join(result))

# Question 17
# argv
# record = input('deposit or withdrawal:  ').split(' ')
# res = 0

# for i in range(len(record)):
#     if record[i] == 'D':
#         res += int(record[i+1])
#     elif record[i] == 'W':
#         res -= int(record[i+1])
#     i += 1

# print(res)

# Alternative Solution
account = 0
while True:
    action = input("Deposite/Withdrawal/Balance/Quit? D/W/B/Q:  ").lower()
    if action == 'd':
        deposit = input("How much would you like to deposit?  ")
        account += int(deposit)
    elif action == 'w':
        withdrawal = input("How much would you like to withdrawal?  ")
        account -= int(withdrawal)
    elif action == 'b':
        print(account)
    else:
        quit()
