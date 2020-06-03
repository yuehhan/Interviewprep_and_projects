# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character but a character may map to itself.

def isIsomorphic(self, s: str, t: str) -> bool:
    if len(s) != len(t): return False
    save = {}
    for i in range(len(t)):
        if s[i] in save:
            if save[s[i]] != t[i]:
                return False
        elif t[i] in save.values():
            return False
        else:
            save[s[i]] = t[i]
    return True