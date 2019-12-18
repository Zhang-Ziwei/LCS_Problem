# 作者：张子威
# 完成日期：2019/12/18
# 输入：两串字串
# 功能：计算最长共有字子串（可以有间隔）
# 输出：最长子子串长度、值、执行时间
# 注意事项：1.如需更改数据来源，记得更改主程序中的资料读取部分

from numpy import zeros
from sys import exit
from time import perf_counter

############
# LCS表格生成函数
############
def LCS_Length(seq1,seq2,len1,len2):
    # 记录max的LCS大小,这里生成大小为(len1+1)*(len2+1)的table，因为这里需要包含边界值
    LcsT = [[0 for q in range(len2+1)] for w in range(len1+1)]
    # 记录方向，LcsD[i][j]用于记录seq1[i]、seq2[j]是否对于LCS有影响，
    # seq1[i]的加入有影响，seq2[j]加不加无所谓(向左找)设为1，反之设为2，seq1[i]seq2[j]均有影响设为3，反之为0。
    LcsD = zeros((len1, len2))
    # 初始化边界预设值
    # for q in range(len1):
    #     LcsT[q][0] = 0
    # for w in range(1, len2):
    #     LcsT[0][w] = 0
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if seq1[i-1] == seq2[j-1]:
                LcsT[i][j] = LcsT[i - 1][j - 1] + 1
                LcsD[i-1][j-1] = 3      # 这里遍历的是LcsT，LcsD比它小1，LcsT相当于LcsD上方和左边各加了一行
            elif LcsT[i - 1][j] >= LcsT[i][j - 1]:
                LcsT[i][j] = LcsT[i - 1][j]
                LcsD[i-1][j-1] = 1
            else:
                LcsT[i][j] = LcsT[i][j - 1]
                LcsD[i-1][j-1] = 2
    # print(LcsD, LcsT)
    return LcsT,LcsD

############
# LCS结果列出函数
############
def Print_LCS(LcsD,seq1,len1,len2,LcsL):
    if len1==0 or len2==0:
        return 0
    if LcsD[len1-1][len2-1]==3:
        Print_LCS(LcsD,seq1,len1-1,len2-1,LcsL)
        LcsL.append(seq1[len1-1])
    elif LcsD[len1-1][len2-1]==2:
        Print_LCS(LcsD,seq1,len1-1,len2,LcsL)
    else:
        Print_LCS(LcsD, seq1, len1, len2-1,LcsL)

############
# 主程序
############
# 资料读取
# 注意！！！要运行的话记得改这里的address！！！
# 如果放在根目录请执行以下这行
f = open("hw2_lcs2.txt")
# f = open("test.txt") # 测试档
# 如果在其他目录请更改
# f = open("D:\program code/Pycharm/algorithm_hw3/hw2_lcs.txt")
temp = f.readline()     # 去掉意义不明的符号
seq1 = f.readline()
temp = f.readline()
seq2 = f.readline()
len1=len(seq1)
len2=len(seq2)
LcsL=[]     # 储存LCS结果

# 读取错误判断
if len1==0 or len2==0:
    print("输入错误：数组不存在。")
    exit()
# 1. sys.exit(n) 退出程序引发SystemExit异常, 可以捕获异常执行些清理工作. n默认值为0, 表示正常退出. 其他都是非正常退出. 还可以sys.exit("sorry, goodbye!"); 一般主程序中使用此退出.
# 2. os._exit(n), 直接退出, 不抛异常, 不执行相关清理工作. 常用在子进程的退出.
# 3. exit()/quit(), 跑出SystemExit异常. 一般在交互式shell中退出时使用.

# 计算执行时间
start = perf_counter()
LcsT,LcsD=LCS_Length(seq1,seq2,len1,len2)
Print_LCS(LcsD,seq1,len1-1,len2-1,LcsL)
end = perf_counter()

# 结果显示
print("字串长度：",len(LcsL))
print("字串内容：",LcsL)
print('time cost:',(end-start)*1000,'ms')
