def file_read(file, place):
    with open(file, 'r', encoding='utf-8') as file:
        s = file.read()
        lst0 = s.split('\n')
        lst = list(filter(lambda x: x != '', lst0))
        k = 0
        for item in lst:
            k += 1
            if item == place: break

        lst01 = lst[k:]
        return lst


def file_write(filename, lst):
    with open(filename, 'w', encoding='utf-8') as file_w:
        file_w.write('\n'.join(lst))


def clear_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            os.remove(file_path)


def insert_title(content,lst):
    lst.insert(0,content)
    return lst

if __name__ == '__main__':

    import os
    import statistics
    import matplotlib.pyplot as plt

    before_analyse_lst = os.listdir('./before_analyse')
    print(before_analyse_lst)
    Dif=eval(input('请输入最大的误差值(参考值0.005) :  '))
    for item in before_analyse_lst:
        filename_before = 'before_analyse/' + item
        lst = file_read(filename_before, '')  #查找内容输入
        lst = [float(item) for item in lst]  #字符串转换为数组
        print(lst,f'\n共',len(lst),'组数据')

        same_num = 0
        point = 0
        list_after = []#储存数据处理数组
        plt_list = []#储存plt数组画图
        while point < len(lst) - 1:
            if abs(lst[point] - lst[point + 1]) <= Dif:
                point += 1
                same_num += 1
                list_after.append([point,])#为了有空位得到标准数据如：[1,'']
                plt_list.append(None)
                continue
            else:
                list_after.append([point,round(statistics.mean(lst[(point - same_num):point + 1]),3)])
                plt_list.append(round(statistics.mean(lst[(point - same_num):point + 1]),3))
                same_num = 0
                point += 1

        #print(list_after)
        list_after = [str(item) for item in list_after]  # 字符串转换为数组
        #print(list_after)
        list_after = [item[1:len(item)-1] for item in list_after]
        #print(list_after)
        filename_after = 'after_analyse/'+item
        file_write(filename_after, list_after)

        ##绘制图表
        #print(plt_list)
        numbers = [i for i in range(1, len(plt_list)+1)]#创建1-len(plt_list)的数组充当x横坐标
        plt.scatter( numbers, plt_list, label='test')
        plt.xlabel('times')
        plt.ylabel('V')
        plt.title('times/V')
        plt.legend()
        plt.show()
print('转换完成')
#清除模块
clear = input('输入0清空数据,输入其他继续运行: ')
if clear == '0':
    recomfirm=input('确定删除请再次输入0:')
    if recomfirm == '0':
        clear_folder('./before_analyse')
        clear_folder('./after_analyse')
    else:
        print('如需删除文件再次点击开始')
else:
    print('如需删除文件再次点击开始')
