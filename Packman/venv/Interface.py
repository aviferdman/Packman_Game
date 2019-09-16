import ReadFiles
import Game_Manager
import Visitor
from Visitor import Observer
'''
class Observer:

    def init_the_game(self):
        pass

    def print_game(self):
        pass

    def print_next_level(self):
        pass
'''

class Interface(Observer):

    def __init__(self):

        self.game_manager = Game_Manager.Game_Manager()
        self.game_manager.register(self)
        self.level = 1

    def init_the_game(self):

        print("")
        print("")
        print(
            " __          __         _   _                                       _               _     _                _____                   _                                                              _       _ ")
        print(
            " \ \        / /        | | | |                                     | |             | |   | |              |  __ \                 | |                                                            | |     | |")
        print(
            "  \ \  /\  / /    ___  | | | |   ___    ___    _ __ ___     ___    | |_    ___     | |_  | |__     ___    | |__) |   __ _    ___  | | __  _ __ ___     __ _   _ __     __      __   ___    _ __  | |   __| |")
        print(
            "   \ \/  \/ /    / _ \ | | | |  / __|  / _ \  | '_ ` _ \   / _ \   | __|  / _ \    | __| | '_ \   / _ \   |  ___/   / _` |  / __| | |/ / | '_ ` _ \   / _` | | '_ \    \ \ /\ / /  / _ \  | '__| | |  / _` |")
        print(
            "    \  /\  /    |  __/ | | | | | (__  | (_) | | | | | | | |  __/   | |_  | (_) |   | |_  | | | | |  __/   | |      | (_| | | (__  |   <  | | | | | | | (_| | | | | |    \ V  V /  | (_) | | |    | | | (_| |")
        print(
            "     \/  \/      \___| |_| |_|  \___|  \___/  |_| |_| |_|  \___|    \__|  \___/     \__| |_| |_|  \___|   |_|       \__,_|  \___| |_|\_\ |_| |_| |_|  \__,_| |_| |_|     \_/\_/    \___/  |_|    |_|  \__,_|")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("use the keys: a,s,d,w to move")
        print("The Dictionary:")
        print("O - the player")
        print("@ - monster")
        print(". - point to collect")
        print("+ - wall ")
        print("$ - bonus point")
        print("when you collect the $ you have 10 moves to kill monsters")
        print("collect all the points to move to the next level!")
        print("good luck :)")
        print("")
        print("")
        print("")

    def print_game(self, board):

        for row in board:
            for col in row:
                try:
                    print(col.to_string(), end="")
                except:
                    pass
            print("")
        ability = None
        if self.game_manager.player.power:
            ability = "on"
        else:
            ability = "off"
        print("killing monsters ability is "+ability)
        print("pick a move: ")

    def print_next_level(self):
        print("")
        print("")
        print("__     __                                                           _     _               _     _                                      _       _                         _   _ ")
        print("\ \   / /                                                          | |   | |             | |   | |                                    | |     | |                       | | | |")
        print(" \ \_/ /    ___    _   _     _ __ ___     ___   __   __   ___    __| |   | |_    ___     | |_  | |__     ___     _ __     ___  __  __ | |_    | |   ___  __   __   ___  | | | |")
        print("   \   /    / _ \  | | | |   | '_ ` _ \   / _ \  \ \ / /  / _ \  / _` |   | __|  / _ \    | __| | '_ \   / _ \   | '_ \   / _ \ \ \/ / | __|   | |  / _ \ \ \ / /  / _ \ | | | |")
        print("    | |    | (_) | | |_| |   | | | | | | | (_) |  \ V /  |  __/ | (_| |   | |_  | (_) |   | |_  | | | | |  __/   | | | | |  __/  >  <  | |_    | | |  __/  \ V /  |  __/ | | |_|")
        print("    |_|     \___/   \__,_|   |_| |_| |_|  \___/    \_/    \___|  \__,_|    \__|  \___/     \__| |_| |_|  \___|   |_| |_|  \___| /_/\_\  \__|   |_|  \___|   \_/    \___| |_| (_)")
        print("")
        print("")
        print("")
        print("")
        self.level += 1


    def print_end_game(self):
        print("")
        print("")
        print("")
        print("")
        print("   _____    ____    _   _    _____   _____                _____   _    _   _                   _______   _____    ____    _   _    _____   _ ")
        print("  / ____|  / __ \  | \ | |  / ____| |  __ \      /\      / ____| | |  | | | |          /\     |__   __| |_   _|  / __ \  | \ | |  / ____| | |")
        print(" | |      | |  | | |  \| | | |  __  | |__) |    /  \    | |  __  | |  | | | |         /  \       | |      | |   | |  | | |  \| | | (___   | |")
        print(" | |      | |  | | | . ` | | | |_ | |  _  /    / /\ \   | | |_ | | |  | | | |        / /\ \      | |      | |   | |  | | | . ` |  \___ \  | |")
        print(" | |____  | |__| | | |\  | | |__| | | | \ \   / ____ \  | |__| | | |__| | | |____   / ____ \     | |     _| |_  | |__| | | |\  |  ____) | |_|")
        print("  \_____|  \____/  |_| \_|  \_____| |_|  \_\ /_/    \_\  \_____|  \____/  |______| /_/    \_\    |_|    |_____|  \____/  |_| \_| |_____/  (_)")
        print("")
        print("")
        print("")
        print("  / ____|     /\     |  \/  | |  ____|    / __ \  \ \    / / |  ____| |  __ \  | |                                                           ")
        print(" | |  __     /  \    | \  / | | |__      | |  | |  \ \  / /  | |__    | |__) | | |                                                           ")
        print(" | | |_ |   / /\ \   | |\/| | |  __|     | |  | |   \ \/ /   |  __|   |  _  /  | |                                                           ")
        print(" | |__| |  / ____ \  | |  | | | |____    | |__| |    \  /    | |____  | | \ \  |_|                                                           ")
        print("  \_____| /_/    \_\ |_|  |_| |______|    \____/      \/     |______| |_|  \_\ (_)                                                           ")
        print("")
        print("")
        print("")
        print("  _           __     __                   __          __                           _ ")
        print(" | |  ______  \ \   / /                   \ \        / /                  ______  | |")
        print(" | | |______|  \ \_/ /    ___    _   _     \ \  /\  / /    ___    _ __   |______| | |")
        print(" | |  ______    \   /    / _ \  | | | |     \ \/  \/ /    / _ \  | '_ \   ______  | |")
        print(" |_| |______|    | |    | (_) | | |_| |      \  /\  /    | (_) | | | | | |______| |_|")
        print(" (_)             |_|     \___/   \__,_|       \/  \/      \___/  |_| |_|          (_)")
        print("                                                                                     ")
        print("")
        print("")

    def print_lose(self):
        print("")
        print("")
        print("")
        print("  / ____|     /\     |  \/  | |  ____|    / __ \  \ \    / / |  ____| |  __ \  | |                                                           ")
        print(" | |  __     /  \    | \  / | | |__      | |  | |  \ \  / /  | |__    | |__) | | |                                                           ")
        print(" | | |_ |   / /\ \   | |\/| | |  __|     | |  | |   \ \/ /   |  __|   |  _  /  | |                                                           ")
        print(" | |__| |  / ____ \  | |  | | | |____    | |__| |    \  /    | |____  | | \ \  |_|                                                           ")
        print("  \_____| /_/    \_\ |_|  |_| |______|    \____/      \/     |______| |_|  \_\ (_)                                                           ")
        print("")
        print("")
        print("")
        print(" __     __                    _                                    __")
        print(" \ \   / /                   | |                              _   / /")
        print("  \ \_/ /    ___    _   _    | |        ___    ___    ___    (_) | | ")
        print("   \   /    / _ \  | | | |   | |       / _ \  / __|  / _ \       | | ")
        print("    | |    | (_) | | |_| |   | |____  | (_) | \__ \ |  __/    _  | | ")
        print("    |_|     \___/   \__,_|   |______|  \___/  |___/  \___|   (_) | | ")
        print("                                                                  \_\                                                                     :(")
        print("                                                                     ")
        self.game_manager.game_won = True

interface = Interface()
interface.game_manager.start_the_game()