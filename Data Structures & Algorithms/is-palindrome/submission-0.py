class Solution:
    def isPalindrome(self, s: str) -> bool:
        c="".join(c.lower() for c in s if c.isalnum())
        new_string=c[::-1]
        if new_string==c:
            return True
        return False