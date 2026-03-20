class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # Словарь для подсчета разности частот
        char_count = {}
        for char_s, char_t in zip(s, t):
            char_count[char_s] = char_count.get(char_s, 0) + 1
            char_count[char_t] = char_count.get(char_t, 0) - 1
        # Проверяем, что все счетчики равны нулю
        for count in char_count.values():
            if count != 0:
                return False
        return True
