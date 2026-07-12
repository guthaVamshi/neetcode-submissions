class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ''.join(ch.lower() for ch in s if ch.isalnum() )
        n = ns[::-1]
        return ns == n