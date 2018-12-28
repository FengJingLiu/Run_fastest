import Licensing
import Player
import rule

'''
1.发牌
2.判断是否第一把 如果是则黑桃3出 如果不是则上把赢家出
3.顺序出牌 判断出牌是否和规矩
4.判断是否能接

'''

p1_card, p2_card, p3_card = Licensing.Licensing()
player1 = Player.Player(Licensing.sort(p1_card),'player1')
player2 = Player.Player(Licensing.sort(p2_card),'player2')
player3 = Player.Player(Licensing.sort(p3_card),'player3')
less_card_player = min([len(player1.card),len(player1.card),len(player1.card)])

# while True:
#     count = 0
#     winner = None
#     while
#     if count == 0:
#         print('player',rule.who_go_first(p1_card,p2_card),'出牌')
#         if rule.who_go_first(p1_card,p2_card) == 1:
#             player1.drop_pick_card(player1.pick_drop_card())
#         elif rule.who_go_first(p1_card,p2_card) == 2:
#             player2.drop_pick_card(player2.pick_drop_card())
#         else:
#             player3.drop_pick_card(player3.pick_drop_card())
#     if count != 0:
#         pass
#     player1.yes_or_not_get(player2)
def process1():
    """
    判断持有黑桃三玩家 并出牌
    :return:
    """
    first_go = rule.who_go_first(p1_card, p2_card)
    if first_go == 1:
        drop = player1.pick_drop_card()
        player1.drop_pick_card(drop)
        return drop,1
    elif first_go == 2:
        drop = player2.pick_drop_card()
        player2.drop_pick_card(drop)
        return drop,2
    else:
        drop = player3.pick_drop_card()
        player3.drop_pick_card(drop)
        return drop,3

def process2(process):
    last_player_drop_card,last_drop_player = process
    if last_drop_player == 1:
        if player2.yes_or_not_get(last_player_drop_card):
            drop = player2.pick_drop_card()
            player2.drop_pick_card(drop)
            return drop, 2
        elif player3.yes_or_not_get(last_player_drop_card):
            drop = player3.pick_drop_card()
            player3.drop_pick_card(drop)
            return drop, 3
        else:
            return 1
    if last_drop_player == 2:
        if player3.yes_or_not_get(last_player_drop_card):
            drop = player3.pick_drop_card()
            player3.drop_pick_card(drop)
            return drop, 3
        elif player1.yes_or_not_get(last_player_drop_card):
            drop = player1.pick_drop_card()
            player1.drop_pick_card(drop)
        else:
            return 2
    if last_drop_player == 3:
        if player1.yes_or_not_get(last_player_drop_card):
            drop = player1.pick_drop_card()
            player1.drop_pick_card(drop)
            return drop, 1
        elif player2.yes_or_not_get(last_player_drop_card):
            drop = player2.pick_drop_card()
            player2.drop_pick_card(drop)
            return drop , 2
        else:
            return 3

print(process2(process1()))





# player1 = Player.Player(Licensing.sort(p1_card, player1))
# player2 = Player.Player(Licensing.sort(p2_card, p2))
# player3 = Player.Player(Licensing.sort(p3_card, p3))
# player1.hand_card()
# rule.yes_or_not_drop()
