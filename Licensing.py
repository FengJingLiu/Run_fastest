import random


def Licensing():
    '''
    洗牌发牌
    :return:玩家手牌 list
    '''
    Card = []
    Flowers = ['s', 'h', 'c', 'd']
    Points = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
    for i in Flowers:
        for j in Points:
            Card.append(i + j)
    Card.remove('s1')
    Card.remove('s2')
    Card.remove('h2')
    Card.remove('c2')
    random.shuffle(Card)
    p1 = Card[:16]
    p2 = Card[16:32]
    p3 = Card[32:]
    # print('player1 card is {}'.format(p1))
    # print('player2 card is {}'.format(p2))
    # print('player3 card is {}'.format(p3))
    return p1, p2, p3


def sort(player):
    '''
    排序 从小到大
    :param player:
    :return:带花色 不带花色 list
    '''
    d = {}
    p = []
    for i in player:
        d[i] = int(i[1:])
    d = sorted(d.items(), key=lambda d: d[1])
    for j in d:
        p.append(j[0])
    return p


if __name__ == '__main__':
    p1, p2, p3 = Licensing()
    p11 = sort(p1)
    print(p11)

