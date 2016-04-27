#User Class

class User:
    def __init__(self,realMoney = 0,teamList = [], leagueList = []):
        self.realMoney = realMoney
        if realMoney == 0:
            self.realMoney = int(input('Enter your initial amount: '))
        self.teamList = teamList

        


    
