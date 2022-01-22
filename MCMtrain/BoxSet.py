import pandas as pd

io = r'D:\Users\shenhui.chen\PycharmProjects\Scrapy\code\OS\packing\装车问题.xlsx'
sheet1 = pd.read_excel(io, sheet_name = 0)

# 定义boxes列表，把box数据都写成字典
boxes = []
# 获取列表行数
nrows = sheet1.shape[0]
# 将box词典写进boxes
for i in range(nrows):
    quantity = sheet1.iloc[i,4]
    if quantity == 0:
        continue
    else:
        box = {}
        box['器具型号'] = sheet1.iloc[i, 0]
        box['长'] = sheet1.iloc[i, 1]
        box['宽'] = sheet1.iloc[i, 2]
        box['高'] = sheet1.iloc[i, 3]
        boxes.append(box)
        for j in range(quantity-1):
            boxes.append(box)

stack = [] # 每一垛
stacks = [] # 垛的合集
# 用了两个迭代，进行堆垛判断
# 用迭代的方法，按照boxes列表顺序进行逐一堆垛
for k1 in range(len(boxes)):
    i = 0
    j = 0
    l = len(boxes)
    if l == 0: # 每完成一次堆垛，将box从boxes中删除，如果boxes都堆垛完了，那么跳出循环
        break
    else:
        stack = [boxes[i]]
        stackh1 = 0 # 定义一个高度增加的中间变量
        stackh = boxes[i]['高'] # 定义一个堆垛高度的变量
        if l > 1:
            # 通过迭代，将boxes的箱子box逐一与第一个箱子进行堆垛，判断是否满足条件。
            for k2 in range(1, len(boxes)):
                l = len(boxes)
                j = j + i + 1
                if l > 1:
                    if boxes[i]['长'] == boxes[j]['长'] and boxes[i]['宽'] == boxes[j]['宽']: # 判断长宽是否一致，一致才允许堆垛
                        stackh = stackh + boxes[j]['高'] # 满足长宽一致的，计算堆垛的总高度
                        if stackh < 2400: # 卡车车厢高2400mm，如果堆垛高度小于卡车车厢高度，那么代表可以堆垛
                            stack.append(boxes[j]) # 卡车车厢高2400mm，如果堆垛高度小于卡车车厢高度，那么代表可以堆垛
                            stackh1 = boxes[j]['高'] # 增加高度
                            del boxes[j] # 将已满足堆垛条件的箱从boxes列表中删除
                            j = j - 1
                        else:
                            stackh -= boxes[j]['高'] # 如果不满足堆垛，那么回复堆垛前的高度
    del boxes[i] # 第一垛完成后，把第一个箱子删除，然后boxes剩下的是还没有完成堆垛的箱子
    stacks.append(stack)

print(stacks)
# 打印出堆垛情况
print('堆垛数', len(stacks))
for i in range(len(stacks)):
    print('第', i+1, '堆器具数量', len(stacks[i]))
    for item in stacks[i]:
        print('第', i+1, '堆器具型号', item['器具型号'])