class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #method without using stack
        fleet=0
        lastfleet=0
        stack=sorted(zip(position, speed), reverse=True)
        for pos, spd in stack:
            time=(target-pos)/spd
            if time > lastfleet:
                fleet+=1
                lastfleet=time
        return fleet