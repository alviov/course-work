from graphinfo import graphinfo

class example:
    
    city = graphinfo()
    
    def makeexamplecity(self):
        self.city.add_edge("A","B", 10)
        self.city.add_edge("A","C", 13)
        self.city.add_edge("A","F", 5)
        self.city.add_edge("A","G", 19)
        self.city.add_edge("B","H", 17)
        self.city.add_edge("C","A", 13)
        self.city.add_edge("C","B", 21)
        self.city.add_edge("C","D", 11)
        self.city.add_edge("D","E", 12)
        self.city.add_edge("D","H", 15)
        self.city.add_edge("D","I", 15)
        self.city.add_edge("E","I", 23)
        self.city.add_edge("E","J", 10)
        self.city.add_edge("E","O", 16)
        self.city.add_edge("F","A", 5)
        self.city.add_edge("F","G", 18)
        self.city.add_edge("F","K", 25)
        self.city.add_edge("F","L", 14)
        self.city.add_edge("G","A", 19)
        self.city.add_edge("G","B", 24)
        self.city.add_edge("G","H", 10)
        self.city.add_edge("G","M", 13)
        self.city.add_edge("G","L", 9)
        self.city.add_edge("H","G", 10)
        self.city.add_edge("H","B", 17)
        self.city.add_edge("H","C", 18)
        self.city.add_edge("H","D", 15)
        self.city.add_edge("H","I", 27)
        self.city.add_edge("H","M", 14)
        self.city.add_edge("I","E", 23)
        self.city.add_edge("I","J", 25)
        self.city.add_edge("I","N", 21)
        self.city.add_edge("I","M", 13)
        self.city.add_edge("J","E", 10)
        self.city.add_edge("J","O", 15)
        self.city.add_edge("K","F", 25)
        self.city.add_edge("K","L", 13)
        self.city.add_edge("K","P", 22)
        self.city.add_edge("K","U", 10)
        self.city.add_edge("L","G", 9)
        self.city.add_edge("L","M", 14)
        self.city.add_edge("L","Q", 8)
        self.city.add_edge("M","I", 13)
        self.city.add_edge("M","N", 5)
        self.city.add_edge("M","S", 18)
        self.city.add_edge("M","R", 14)
        self.city.add_edge("M","Q", 18)
        self.city.add_edge("M","L", 14)
        self.city.add_edge("N","I", 21)
        self.city.add_edge("N","J", 22)
        self.city.add_edge("N","O", 13)
        self.city.add_edge("N","T", 17)
        self.city.add_edge("N","S", 12)
        self.city.add_edge("O","J", 15)
        self.city.add_edge("O","E", 16)
        self.city.add_edge("O","T", 15)
        self.city.add_edge("O","N", 13)
        self.city.add_edge("P","K", 22)
        self.city.add_edge("P","L", 13)
        self.city.add_edge("P","Q", 17)
        self.city.add_edge("P","U", 21)
        self.city.add_edge("Q","P", 17)
        self.city.add_edge("Q","R", 15)
        self.city.add_edge("Q","V", 11)
        self.city.add_edge("R","Q", 15)
        self.city.add_edge("R","S", 19)
        self.city.add_edge("R","X", 17)
        self.city.add_edge("R","W", 18)
        self.city.add_edge("R","V", 12)
        self.city.add_edge("S","R", 19)
        self.city.add_edge("S","N", 12)
        self.city.add_edge("S","T", 23)
        self.city.add_edge("S","Y", 19)
        self.city.add_edge("S","X", 14)
        self.city.add_edge("T","Y", 21)
        self.city.add_edge("U","K", 10)
        self.city.add_edge("U","Q", 24)
        self.city.add_edge("U","V", 12)
        self.city.add_edge("V","R", 12)
        self.city.add_edge("V","W", 16)
        self.city.add_edge("W","V", 16)
        self.city.add_edge("W","R", 18)
        self.city.add_edge("W","Y", 18)
        self.city.add_edge("X","W", 9)
        self.city.add_edge("X","S", 14)
        self.city.add_edge("X","Y", 16)
        self.city.add_edge("Y","X", 16)
        self.city.add_edge("Y","T", 21)
        self.city.add_edge("Y","W", 18)
        
        self.city.add_district("A", 1)
        self.city.add_district("B", 2)
        self.city.add_district("C", 3)
        self.city.add_district("D", 2)
        self.city.add_district("E", 1)
        self.city.add_district("F", 2)
        self.city.add_district("G", 3)
        self.city.add_district("H", 4)
        self.city.add_district("I", 3)
        self.city.add_district("J", 2)
        self.city.add_district("K", 3)
        self.city.add_district("L", 4)
        self.city.add_district("M", 5)
        self.city.add_district("N", 4)
        self.city.add_district("O", 3)
        self.city.add_district("P", 2)
        self.city.add_district("Q", 3)
        self.city.add_district("R", 4)
        self.city.add_district("S", 3)
        self.city.add_district("T", 2)
        self.city.add_district("U", 1)
        self.city.add_district("V", 2)
        self.city.add_district("W", 3)
        self.city.add_district("X", 2)
        self.city.add_district("Y", 1)
        
        return self.city