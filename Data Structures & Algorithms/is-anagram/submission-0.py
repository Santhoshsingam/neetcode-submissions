class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        if sorted(s) == sorted(t):
            return True
            exit()
        return False