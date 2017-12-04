old_pigs = 0
pig_nums = 2
last_pigs = 0

for i in range(100):
    if i == 0:
        last_pigs = pig_nums
        pig_nums = pig_nums + pig_nums / 2 * 4
    elif i == 2:
        last_pigs = pig_nums
        pig_nums = pig_nums - old_pigs + pig_nums / 2 * 4
        old_pigs = last_pigs
    elif i % 2 == 0:
        last_pigs = pig_nums
        pig_nums = pig_nums - old_pigs + pig_nums / 2 * 4
        old_pigs = last_pigs
    if i % 2 == 0:
        print(str(i) + 'Today PigNumber: ' + str(pig_nums))