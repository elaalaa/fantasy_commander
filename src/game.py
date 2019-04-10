import sys
from PyQt5.QtWidgets import QApplication

from map import *
from location import *
from creature import *
from player import *
from GUI import *


class Game():
    
    MOVESELECT = 0
    MOVEACTION = 1
    ATTACKSELECT = 2
    ATTACKACTION = 3
    
    
    def __init__(self, player1, player2, map, print_msg):
        self.player1 = player1
        self.player2 = player2
        self.map = map
        self.print_msg = print_msg
        self.squares = []
        self.turn = 0
        self.gamestate = 0
        self.currentplayer = player1
        self.statemethods = [self.move_select, self.move_action, self.attack_select, self.attack_action]
        self.print_msg("Player1, your turn")
        self.print_msg("Select creature to move")
        

    
    def move_select(self, location):
        creature = self.map.get_creature(location)
        if creature != None and creature.player == self.currentplayer:
            self.gamestate = Game.MOVEACTION
            self.currentcreature = creature
            self.print_msg("Select where to move")
            self.squares = self.currentcreature.movement_squares()
            self.highlight(self.squares)
            
            
    def move_action(self, location):
        if self.map.get_tile(location) in self.squares:
            empty = self.map.get_tile(location).is_empty()
            if empty == True:
                self.unhighlight()
                self.map.get_tile(self.currentcreature.location).remove_creature()
                self.currentcreature.location = location
                self.map.get_tile(location).set_creature(self.currentcreature)
                self.currentcreature = None
                self.gamestate = Game.ATTACKSELECT
                self.print_msg("Select creature to attack with")
            
    def attack_select(self, location):
        creature = self.map.get_creature(location)
        if creature != None and creature.player == self.currentplayer:
            self.currentcreature = creature
            self.print_msg("Select where to attack")
            self.squares = self.currentcreature.attack_squares()
            self.highlight(self.squares)
            self.gamestate = Game.ATTACKACTION
    
    def attack_action(self, location):
        if self.map.get_tile(location) in self.squares:
            self.unhighlight()
            self.currentcreature.attack(location)
            self.gamestate = Game.MOVESELECT
            self.currentcreature = None
            self.change_players()
            self.print_msg("Select creature to move")
            
    def change_players(self):
        self.turn += 1
        if self.currentplayer == self.player1:
            self.currentplayer = self.player2
            self.print_msg("\nPlayer2, your turn")
        else:
            self.currentplayer = self.player1
            self.print_msg("\nPlayer1, your turn")
        if self.currentplayer.type == Player.AI: # ai plays turn, not finished
            self.currentplayer.ai_turn()
            self.gamestate = Game.MOVESELECT
            self.change_players()
    
    def on_click(self, location):
        self.statemethods[self.gamestate](location)
        


def main():
    player1 = Player(1, Player.HUMAN)
    player2 = Player(2, Player.HUMAN)
    
    test_map = Map('maps/map2.txt')
    

    tank_location = Location(0, 0)
    tank_body = Tank('Tank1', player1, tank_location)
    test_map.add_creature(tank_body, tank_location)
    player1.add_teammember(tank_body)

    mage_location = Location(0, 1)
    mage_body = Mage('Mage1', player1, mage_location)
    test_map.add_creature(mage_body, mage_location)
    player1.add_teammember(mage_body)

    ninja_location = Location(0, 2)
    ninja_body = Ninja('Ninja1', player1, ninja_location)
    test_map.add_creature(ninja_body, ninja_location)
    player1.add_teammember(ninja_body)

    sniper_location = Location(0, 3)
    sniper_body = Sniper('Sniper1', player1, sniper_location)
    test_map.add_creature(sniper_body, sniper_location)
    player1.add_teammember(sniper_body)
    
    tank2_location = Location(0, 4)
    tank2_body = Tank('Tank2', player1, tank2_location)
    test_map.add_creature(tank2_body, tank2_location)
    player1.add_teammember(tank2_body)

    mage2_location = Location(0, 5)
    mage2_body = Mage('Mage2', player1, mage2_location)
    test_map.add_creature(mage2_body, mage2_location)
    player1.add_teammember(mage2_body)

    ninja2_location = Location(0, 6)
    ninja2_body = Ninja('Ninja2', player1, ninja2_location)
    test_map.add_creature(ninja2_body, ninja2_location)
    player1.add_teammember(ninja2_body)

    sniper2_location = Location(0, 7)
    sniper2_body = Sniper('Sniper2', player1, sniper2_location)
    test_map.add_creature(sniper2_body, sniper2_location)
    player1.add_teammember(sniper2_body)
    
    p2_tank_location = Location(13, 0)
    p2_tank_body = Tank('Tank1', player2, p2_tank_location)
    test_map.add_creature(p2_tank_body, p2_tank_location)
    player2.add_teammember(p2_tank_body)

    p2_mage_location = Location(13, 1)
    p2_mage_body = Mage('Mage1', player2, p2_mage_location)
    test_map.add_creature(p2_mage_body, p2_mage_location)
    player2.add_teammember(p2_mage_body)

    p2_ninja_location = Location(13, 2)
    p2_ninja_body = Ninja('Ninja1', player2, p2_ninja_location)
    test_map.add_creature(p2_ninja_body, p2_ninja_location)
    player2.add_teammember(p2_ninja_body)

    p2_sniper_location = Location(13, 3)
    p2_sniper_body = Sniper('Sniper1', player2, p2_sniper_location)
    test_map.add_creature(p2_sniper_body, p2_sniper_location)
    player2.add_teammember(p2_sniper_body)
    
    p2_tank2_location = Location(13, 4)
    p2_tank2_body = Tank('Tank2', player2, p2_tank2_location)
    test_map.add_creature(p2_tank2_body, p2_tank2_location)
    player2.add_teammember(p2_tank2_body)

    p2_mage2_location = Location(13, 5)
    p2_mage2_body = Mage('Mage2', player2, p2_mage2_location)
    test_map.add_creature(p2_mage2_body, p2_mage2_location)
    player2.add_teammember(p2_mage2_body)

    p2_ninja2_location = Location(13, 6)
    p2_ninja2_body = Ninja('Ninja2', player2, p2_ninja2_location)
    test_map.add_creature(p2_ninja2_body, p2_ninja2_location)
    player2.add_teammember(p2_ninja2_body)

    p2_sniper2_location = Location(13, 7)
    p2_sniper2_body = Sniper('Sniper2', player2, p2_sniper2_location)
    test_map.add_creature(p2_sniper2_body, p2_sniper2_location)
    player2.add_teammember(p2_sniper2_body)
    
    

    # Every Qt application must have one instance of QApplication.
    global app # Use global to prevent crashing on exit
    app = QApplication(sys.argv)
    
    gui = Gamewindow(test_map, 50)
    game = Game(player1, player2, test_map, gui.print_message)
    gui.scene.click_handler = game.on_click
    game.highlight = gui.highlight_squares
    game.unhighlight = gui.remove_highlighted
    
    # Start the Qt event loop. (i.e. make it possible to interact with the gui)
    sys.exit(app.exec_())

    # Any code below this point will only be executed after the gui is closed.

if __name__ == '__main__':
    main()
