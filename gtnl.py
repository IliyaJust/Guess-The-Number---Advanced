
#UI
class Console:
    def __init__(self, game_dir):
        self.interpeter = Interpeter(game_dir)
        self.console()
    def console(self):
        while True:
            print("GTNL Version Alpha 0.1")
            cmd = input("Enter Command: ")
            self.interpeter.send_request(cmd)
#Main Interpeter For GTNL 
class Interpeter:
    def __init__(self, game_dir):
        self.game_dir = game_dir
    def send_request(self, cmd):
        pass

                    
