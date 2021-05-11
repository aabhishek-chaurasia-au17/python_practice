class Phone():
    def set_color(self,color):
        self.color = color

    def set_cost(self,cost):
        self.cost = cost

    def show_Color(self):
        print(self.color)

    def show_Cost(self):
        print(self.cost)
        
    def make_Call(self):
        print("making a call")

    def play_Game(self):
        print("playing a game")    

p2 = Phone()

p2.set_color("Red")

p2.set_cost(5000)

p2.show_Cost()

p2.show_Color()

p2.make_Call()

p2.play_Game()

