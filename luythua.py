import sys
sys.set_int_max_str_digits(0) #Đặt lại giới hạn string

#chia để trị

def solution(n,k):
    if k==1:
        return n
    elif k%2==0:
        return (solution(n,k//2)**2)%(10**9+7)
    else: return (solution(n,k//2)**2*n)%(10**9+7)

#đọc file và ghi file
with open('luythua.inp', mode='r') as file_in:
    n,k = map(int, file_in.readline().split(' '))
with open('luythua.out', mode='w') as file_out:
    file_out.write(str((solution(n,k))))
