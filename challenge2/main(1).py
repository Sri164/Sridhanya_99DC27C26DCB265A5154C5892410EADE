class player:
 def play(self):
    print("The Player is playing cricket")
class Batsman(player):
 def play(self):
    print("The Batsman is batting")
class Bowler(player):
 def play(self):
    print("The bowler is bowing")
batsman = Batsman()
bowler = Bowler()
batsman.play()
bowler.play()
