class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink,count = numBottles,1
        while numBottles > 0:
            numBottles -= 1
            if count % numExchange == 0:
                drink += 1
                numBottles += 1
            count += 1
        return drink
            
            
        