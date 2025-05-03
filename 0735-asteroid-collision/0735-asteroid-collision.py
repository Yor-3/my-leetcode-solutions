class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
            
        stack = []
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    stack.pop()   # Right asteroid smaller → explode
                    continue
                elif stack[-1] == -a:
                    stack.pop()   # Both same → both explode
                break             # Left asteroid destroyed
            else:
                stack.append(a)
        return stack
