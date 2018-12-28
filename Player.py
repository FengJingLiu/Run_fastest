import rule
import Licensing
from itertools import combinations


class Player(object):
    """
    初始属性 发牌牌型
    """

    def __init__(self, card, name):
        # self.player_num = player_num
        self.card = card
        self.name = name

    def hand_card(self):
        """
        现有手牌
        :return:
        """
        print('{} card is'.format(self.name), self.card)

    def pick_drop_card(self):
        """
        打出手牌
        :return:
        """
        b = True
        while b:
            self.hand_card()
            input_drop = input('{}输入打出手牌,空格分割。'.format(self.name))
            input_drop = input_drop.split(' ')
            self_list = self.card
            d = [False for i in input_drop if i not in self_list]  # 判断input是否在hand card列表 如果不在则输出True
            if False in d:
                print('{} 重新输入'.format(self.name))

            else:
                for i in input_drop:
                    if i not in self.card:
                        self.pick_drop_card()
                    else:
                        b = False
                        return input_drop

    def drop_pick_card(self, dropcard):
        if self.is_or_not_in_rule(dropcard):
            for i in dropcard:
                if i not in self.card:
                    self.pick_drop_card()
                else:
                    self.card.remove(i)
        else:
            self.pick_drop_card()

    def yes_or_not_get(self, last_player_drop):
        """
        1.single card
        2.double card
        3.straight
        4.full house
        5.bomb
        6.straight double
        7.三带二收尾单0
        8.三带二收尾单1
        判断是否接的起 符合返回true
        :param last_player_drop: 上家出牌
        :return: bool
        """
        type = rule.which_types(last_player_drop)  # 上家出牌类型
        last_player_drop_order = rule.hand_card_to_dict(last_player_drop)  # 上家出牌字典顺序
        if type == 1:
            if rule.hand_card_to_dict(self.card)[-1] > last_player_drop_order[-1]:  # 出单时比较手牌最后一张大小
                return True
            else:
                return False
        elif type == 2:  # 出对时比较手牌所有两张一样以上组合 然后比较大小
            combinations_type2 = list(combinations(self.card, 2))  # 列出所有两张组合
            count = 0
            bool = False
            while count < len(combinations_type2) + 1 and bool == False:
                for i in combinations_type2:
                    count += 1
                    list_ = rule.hand_card_to_dict(i)
                    if list_[0] == list_[1]:
                        if list_[0] > last_player_drop_order[0]:
                            bool = True
                            break
                        else:
                            bool = False
            return bool
        elif type == 3:  # 顺子比较手牌
            combinations_type3 = list(combinations(self.card, len(last_player_drop)))  # 列出所有和出牌张数一样的组合
            count = 0
            bool = False
            while count < len(combinations_type3) + 1 and bool == False:
                for i in combinations_type3:
                    count += 1
                    list_ = rule.hand_card_to_dict(i)
                    if rule.which_types(i) == 3:
                        if list_[0] > last_player_drop_order[0]:
                            bool = True
                            break
                        else:
                            bool = False
            return bool

        elif type == 4 or type == 7 or type == 8:  # 三带
            combinations_type4 = list(combinations(self.card, len(last_player_drop)))  # 列出所有和出牌张数一样的组合
            count = 0
            bool = False
            while count < len(combinations_type4) + 1 and bool == False:
                for i in combinations_type4:
                    count += 1
                    list_ = rule.hand_card_to_dict(i)
                    if rule.which_types(i) == 4 or 7 or 8:
                        if (rule.three_plus_two(list_) > rule.three_plus_two(last_player_drop_order)):
                            bool = True
                            break
                        else:
                            bool = False
            return bool

        elif type == 5:
            combinations_type5 = list(combinations(self.card, len(last_player_drop)))  # 列出所有和出牌张数一样的组合
            count = 0
            bool = False
            while count < len(combinations_type5) + 1 and bool == False:
                for i in combinations_type5:
                    count += 1
                    list_ = rule.hand_card_to_dict(i)
                    if rule.which_types(i) == 5:
                        if rule.three_plus_two(list_) > rule.three_plus_two(last_player_drop_order):
                            bool = True
                            break
                        else:
                            bool = False
            return bool
        elif type == 6:
            combinations_type6 = list(combinations(self.card, len(last_player_drop)))  # 列出所有和出牌张数一样的组合
            count = 0
            bool = False
            while count < len(combinations_type6) + 1 and bool == False:
                for i in combinations_type6:
                    count += 1
                    list_ = rule.hand_card_to_dict(i)
                    if rule.which_types(i) == 6:
                        if list_[0] > last_player_drop_order[0]:
                            bool = True
                            break
                        else:
                            bool = False
            return bool

    def is_or_not_in_rule(self, hero_drop):
        """
        出牌是否符合规则
        :param drop:
        :return:bool
        """
        drop = rule.hand_card_to_dict(hero_drop)
        if len(drop) == 1:  # 单
            return True
        elif len(drop) == 2:  # 对
            if drop[0] == drop[1]:
                return True
            else:
                return False
        elif len(drop) == 3 and drop[0] == drop[1] == drop[2] and len(self.card) == 3:  # 三张收尾
            if drop[0] != 13:
                return True
            else:
                return False
        elif len(drop) == 4:  # 连对 炸弹
            if drop[0] == drop[1] == drop[2] == drop[3]:  # 炸弹
                if drop[0] != 12 and drop[0] != 13:
                    return True
                else:
                    return False
            elif drop[0] == drop[1] and drop[2] == drop[3] and drop[2] - drop[1] == 1:  # 连对
                if drop[-1] != 13:
                    return True
                else:
                    return False
            elif drop[0] != drop[1] == drop[2] == drop[3] or drop[0] == drop[1] == drop[2] != drop[3] and len(
                    self.card) == 4:
                if rule.three_plus_two(drop) != 13:
                    return True
                else:
                    return False
            # else:
            #     self.pick_drop_card()
        if len(drop) >= 5:  # 三带二 顺 连对
            bool1 = True
            bool2 = True
            count = 0
            count1 = 0
            while bool1:
                for i in range(0, len(drop) - 2, 2):
                    if drop[i] == drop[i + 1] and drop[i + 2] - drop[i] == 1:  # 连对
                        if drop[-1] != 13:
                            bool1 = True
                        else:
                            bool1 = False
                            break
                    else:
                        bool1 = False
                        break  # 连对

            while count1 < len(drop) - 1 and bool2:
                for i in range(len(drop) - 1):
                    count1 += 1
                    if drop[i] + 1 == drop[i + 1]:
                        if i == len(drop) - 2 and drop[-1] != 13:
                            # bool2 = False
                            break
                        else:
                            continue
                    else:
                        bool2 = False
                        break

            if bool1 or bool2 is True:
                return True

            elif drop[0] == drop[1] == drop[2] or drop[2] == drop[3] == drop[4] or drop[2] == drop[3] == drop[1]:  # 三带二
                if rule.three_plus_two(hero_drop) != 13:
                    return True
                else:
                    return False
        else:
            return False

    def get_point(self, card):
        list_ = []
        for i in card:
            list_.append(int(i[1:]))
        return list_

    def get_count_of_card(self):
        return len(self.card)


if __name__ == '__main__':
    p1_card, p2_card, p3_card = Licensing.Licensing()
    player1 = Player(Licensing.sort(p1_card), 'player1')
    player2 = Player(Licensing.sort(p2_card), 'player2')
    #player1.hand_card()
    print(player1.pick_drop_card())
    # print(player1.is_or_not_in_rule(player1.pick_drop_card()))
    # playertest = Player(
    #     ['h1', 'h3', 'd3', 'c5', 's8', 'd8', 's7', 'c9', 'd10', 'c11', 'd11', 'h12', 'c12', 's3', 'c13', 'd13'],
    #     'playertest')
    # print(playertest.yes_or_not_get(['s7', 'd7', 'c8', 'c8', 'h9', 's9']))
    # player1.yes_or_not_drop(player2.drop_card())
