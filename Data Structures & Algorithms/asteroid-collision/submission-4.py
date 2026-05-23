class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            aDestroyed = False
            while stack and stack[-1] > 0 and a < 0:
                lSize = abs(stack.pop())
                rSize = abs(a)
                if lSize > rSize:
                    stack.append(lSize)
                    aDestroyed = True
                    break
                elif lSize < rSize:
                    continue
                else:
                    aDestroyed = True
                    break
            
            if not aDestroyed:
                stack.append(a)

        return stack
        
            