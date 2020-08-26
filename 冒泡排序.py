#冒泡排序法
# def bobble_sort(a_ilst):
#     n=len(a_ilst)
#     '遍历次数'
#     for j in range(n):#要遍历的次数
#         count=0
#         for i in range(n-1-j):#遍历到的位置
#             if a_ilst[i] > a_ilst[i+1]:
#                 a_ilst[i],a_ilst[i+1]=a_ilst[i+1],a_ilst[i]
#                 count+=1
#             if count==0:
#                 return 0
#
# ls=[45,54,84,5,854,684,4]
# print(ls)
# bobble_sort(ls)
# print(ls)


#选择排序法
#从未被排序的部分找出最小值放在前面\\对于相同数值位置可能发生交换， 不稳定
# def select_sort(a_list):
#     n=len(a_list)
#     for j in range(n):
#     #min_index=j
#         for i in range(1+j,n):
#             if a_list[j]>a_list[i]:
#                 a_list[i],a_list[j]=a_list[j],a_list[i]
#
# ls=[4,54,84,4,854,4,4,4]
# print(ls)
# select_sort(ls)
# print(ls)

#插入排序算法
# def insert_algorithem(a_list):
#     n=len(a_list)
#     for j in range(1,n):
#         i=j
#         while i>0:
#             if a_list[i] < a_list[i-1]:
#                 a_list[i],a_list[i-1]=a_list[i-1],a_list[i]
#                 i-=1
#             else:
#                 break

# if __name__=="__main__":
#     ls=[5,4,6,8,9,1]
#     insert_algorithem(ls)
#     print(ls)

#希尔顿排序
#通过规定一定步长使用插入排序，然后减小步长
def xier_sort(alist):
    n=len(alist)
    gap=n//2
    while gap>0:
        for i in range(gap,n):
            while i>0:
                if alist[i]<alist[i-gap]:
                    alist[i],alist[i-gap]=alist[i-gap],alist[i]
                    i-=1
                else:
                    break
        gap=gap//2
if __name__=="__main__":
    ls=[5,4,6,8,9,1]
    xier_sort(ls)
    print(ls)

#快速排序
