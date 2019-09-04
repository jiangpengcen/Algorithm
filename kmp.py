import numpy as np
# 需要查找的长文本串
aim = 'abccbababababbc'
# 模式串
str = 'abababb'
dp = np.zeros(len(str) + 1, dtype=int)
nextval = np.zeros(len(str), dtype=int)
dp[0] = -1
for t in range(2, len(dp)):
    i = 1  #i：前缀开始位置同时也是记录指针
    j = k = 2   #j：后缀的记录指针
    k += 1    #k：后缀开始位置
    while(j <= t):
        if(str[i - 1] == str[j - 1]):
            i += 1
            j += 1
        else:
            i = 1
            j = k
            k += 1  #k每趟比较失败后后移一位
        if(j == t + 1):
            dp[t] = i - 1
next = np.delete((dp + 1.0).astype(np.int8), -1)
dp = np.delete(dp.astype(np.int8), 0)
print(dp)
print(next)
for i in range(1, len(str)):
    if(dp[i] != next[i]):
        nextval[i] = next[i]
    else:
        nextval[i] = nextval[next[i] - 1]
print(nextval)
i = j = 0
count = 0
while i < len(aim):
    if aim[i] == str[j]:
        count += 1
        i += 1
        j += 1
    else:  #当不匹配时，只需要根据nextval回溯模式串中指针
        count += 1
        j = nextval[j] - 1
        if j < 0:
            i += 1
            j += 1
    if(j == len(str)):
        print("found!")
        break
print("一共比较 %d次" % count)