T = int(input())
ymd = {'01':'31', '02':'28', '03':'31', '04':'30', '05':'31', '06':'30', '07':'31', '08':'31', '09':'30', '10':'31', '11':'30', '12':'31'}
for test_case in range(1, T + 1):
    n = input()
    if n[4:6] in ymd and ymd[n[4:6]] >= n[6:]:
        print(f'#{test_case} {n[:4]}/{n[4:6]}/{n[6:]}')
    else:
        print(f'#{test_case} -1')