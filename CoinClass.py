class Coins:

    halfdollar = 0.5
    quarter = 0.25
    dime = 0.1
    nickel = 0.05
    penny = 0.01

    def __init__(self, numCoins, value):
        self.numCoins = numCoins
        self.value = value
        self.coinValue = 0
        self.coinCount = 0
        self.halfDollarCount = 0
        self.quarterCount = 0
        self.dimeCount = 0
        self.nickelCount = 0
        self.pennyCount = 0

    def reset(self):
        self.coinCount = 0
        self.halfDollarCount = 0
        self.quarterCount = 0
        self.dimeCount = 0
        self.nickelCount = 0
        self.pennyCount = 0

    def findCoinCombinations(self):

        i=1
        while(self.coinCount <= self.numCoins):
            if(Coins.halfdollar*i < self.value):
                self.halfDollarCount = i
                self.coinValue = Coins.halfdollar*i

        halfDollarCount = self.value / Coins.halfdollar
        self.coinValue = self.value % Coins.halfdollar

        quarterCount = self.value / Coins.quarter
        self.coinValue = self.value % Coins.quarter

        dimeCount = self.value / Coins.dime
        self.coinValue = self.value % Coins.dime

        dimeCount = self.value / Coins.dime
        self.coinValue = self.value % Coins.dime

        nickelCount = self.value / Coins.nickel
        self.coinValue = self.value % Coins.nickel

        pennyCount = self.value / Coins.penny
        self.coinValue = self.value % Coins.penny

        if(self.numCoins == self.coinCount and "self.coinValue == self.value):
            #print("Half-dollar(s): %2d, Quarter(s): %2d, Dime(s): %2d, Nickel(s): %2d Dime(s): %2d, Nickel(s): %2d, Pennies: %2d" %(self.halfDollarCount, self.quarterCount, self.dimeCount, self.nickelCount, self.pennyCount))
            #self.reset()