# 二分查找

# 使用循环实现
def binary(value, key):
    # 获取查找范围对应的左侧下标值/右侧
    left = 0 
    right = len(value)-1
    # 当仍存在合法的查找范围时重复该过程
    while left <= right:
        # 中间元素对应下标值
        middle = (left + right) // 2
        # 比较中间值与指定值:
        if value[middle] == key:
            # 如果相等
            # 查找成功,返回下标值
            return middle
        elif value[middle] > key:
            # 如果指定值比中间值小
            # 则在左侧继续查找
            right = middle - 1 
        else:
            # 如果指定值比中间值大
            # 则在右侧继续查找
            left = middle + 1
    # 如果遍历完所有数据仍未找到
    # 则查找失败,返回-1
    return -1


# 原始数据
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# 要查找扑克牌 6
key = 6
# 调用二分查找
res = binary(values, key)
# 根据返回值打印结果
if res == -1:
    print('查找失败')
else:
    print('查找成功,对应下标值:', res)


