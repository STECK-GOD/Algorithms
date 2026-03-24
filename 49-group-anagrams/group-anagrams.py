class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        groups = defaultdict(list)

        for s in strs:
            # Массив частот для 26 строчных букв
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            # Кортеж частот – ключ словаря
            key = tuple(count)
            groups[key].append(s)

        return list(groups.values())
