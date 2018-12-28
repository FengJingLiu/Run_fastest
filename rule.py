import Licensing


def who_go_first(p1, p2):
    """
    判断出牌顺序
    :param p1: 玩家手牌
    :param p2:
    :return: which player go first
    """
    if 'd3' in p1:
        return 1
    elif 'd3' in p2:
        return 2
    else:
        return 3


def three_plus_two(drop):
    """
    获取三带二的三
    :param drop:输入字典化后的列表
    :return:
    """
    #drop1 = hand_card_to_dict(drop)
    for i in drop:
        if drop.count(i) > 2:
            return i


def which_types(dropcard):
    """
    判断出牌类型
    1.single card
    2.double card
    3.straight
    4.full house
    5.bomb
    6.straight double
    7.三带二收尾单0
    8.三带二收尾单1
    :param drop: drop type list
    :return:
    """
    drop = hand_card_to_dict(dropcard)
    if len(drop) == 1:  # 单
        return 1
    elif len(drop) == 2:  # 对
        return 2
    elif len(drop) == 3:  # 三张收尾
        return 7
    elif len(drop) == 4:  # 连对 炸弹
        if drop[0] == drop[1] == drop[2] == drop[3]:
            return 5
        elif drop[0] == drop[1] and drop[2] == drop[3] and drop[2] - drop[1] == 1:
            return 6
        elif drop[0] != drop[1] == drop[2] == drop[3] or drop[0] == drop[1] == drop[2] != drop[3]:
            return 8
        else:
            return 0
    if len(drop) >= 5:  # 三带二 顺 连对
        for i in range(0, len(drop) - 2, 2):
            if drop[i] == drop[i + 1] and drop[i + 2] - drop[i] == 1:
                return 6  # 连对
            elif drop[i] + 1 == drop[i + 1] and drop[i] + 2 == drop[i + 2] and drop[-1] != 13:
                return 3  # 顺子
        if drop[0] == drop[1] == drop[2] or drop[2] == drop[3] == drop[4] or drop[2] == drop[3] == drop[1]:
            return 4  # 三带二
        else:
            return 0


def which_big(drop1, drop2):
    """
    判断出牌大小
    每种类型单独比较
    1.single card
    2.double card
    3.straight
    4.full house
    5.bomb
    6.straight double
    7.三带二收尾单0
    8.三带二收尾单1
    :return:bool if 1>2 return True,else return False
    """
    if which_types(drop1) != which_types(drop2):
        print('请输入正确牌型')
    else:
        drop1 = hand_card_to_dict(drop1)
        drop2 = hand_card_to_dict(drop2)
        if which_types(drop1) == 1:
            if drop1[0] > drop2[0]:
                return True
            else:
                return False
        elif which_types(drop1) == 2:
            if drop1[0] > drop2[0]:
                return True
            else:
                return False
        elif which_types(drop1) == 3:
            if drop1[0] > drop2[0]:
                return True
            else:
                return False
        elif which_types(drop1) == 4:
            if three_plus_two(drop1) > three_plus_two(drop2):
                return True
            else:
                return False
        elif which_types(drop1) == 5:
            if drop1[0] > drop2[0]:
                return True
            else:
                return False
        elif which_types(drop1) == 6:
            if drop1[0] > drop2[0]:
                return True
            else:
                return False
        elif which_types(drop1) == 7:
            if three_plus_two(drop1) > three_plus_two(drop2):
                return True
            else:
                return False
        elif which_types(drop1) == 8:
            if three_plus_two(drop1) > three_plus_two(drop2):
                return True
            else:
                return False


def hand_card_to_dict(cardlist):
    """
    手牌带花色转为大小列表
    :param cardlist:
    :return:
    """
    list_ = []
    dict_ = {'1': 12, '2': 13, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, '10': 8, '11': 9, '12': 10,
             '13': 11}
    for i in cardlist:
        list_.append(dict_[i[1:]])
    list_ = sorted(list_)
    return list_




if __name__ == '__main__':
    drop = ['c13', 'h13', 'd13', 'h7', 'h8']
    # print(which_types(drop))
    print(three_plus_two(drop))
