import Player
import Licensing
import rule

type1 = ['d1']
type2 = ['d1', 'd1']
type3 = ['d3', 'd4', 'd5', 'c6', 'd7', 'h8']
type4 = ['d3', 'h3', 'd4', 'c4', 's4']
type5 = ['d3', 'h3', 's3', 'c3']
type6 = ['d3', 'h3', 'd4', 'c4', 's5','d5']
type7 = [ 'd4', 'c4', 's4']
type8 = ['d3', 'd4', 'c4', 's4']

player1 = Player.Player(Licensing.sort(p1_card, player1))
player2 = Player.Player(Licensing.sort(p2_card, p2))
player3 = Player.Player(Licensing.sort(p3_card, p3))

player1.pick_drop_card()

