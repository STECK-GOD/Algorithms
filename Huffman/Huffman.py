import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def build_tree(text):
    # считаем, сколько раз встречается каждая буква
    freqs = Counter(text)
    
    heap = []
    # закидываем все в кучу. id(node) нужен, чтобы heapq не ломался при одинаковых частотах
    for ch, f in freqs.items():
        node = Node(ch, f)
        heapq.heappush(heap, (f, id(node), node))
        
    # строим дерево, пока не останется один корень
    while len(heap) > 1:
        f1, id1, left_node = heapq.heappop(heap)
        f2, id2, right_node = heapq.heappop(heap)
        
        # создаем внутренний узел без символа, частота = сумме двух детей
        merged = Node(None, f1 + f2)
        merged.left = left_node
        merged.right = right_node
        
        heapq.heappush(heap, (merged.freq, id(merged), merged))
        
    # возвращаем сам узел корня
    return heap[0][2] if heap else None

def get_codes(node, current_str, codes_dict):
    if not node:
        return
    
    # если дошли до листа (есть символ), сохраняем готовый код
    if node.char is not None:
        codes_dict[node.char] = current_str
        return
        
    # идем влево - пишем 0, вправо - пишем 1
    get_codes(node.left, current_str + "0", codes_dict)
    get_codes(node.right, current_str + "1", codes_dict)

def huffman_encode(text):
    if not text:
        return "", None
        
    root = build_tree(text)
    codes = {}
    get_codes(root, "", codes)
    
    # кодируем текст по словарю
    res = ""
    for ch in text:
        res += codes[ch]
        
    return res, root

def huffman_decode(encoded_text, root):
    if not encoded_text or not root:
        return ""
        
    res = ""
    curr = root
    
    # бежим по нулям и единицам
    for bit in encoded_text:
        if bit == '0':
            curr = curr.left
        else:
            curr = curr.right
            
        # если наткнулись на букву
        if curr.char is not None:
            res += curr.char
            curr = root # прыгаем обратно в корень дерева для поиска следующей
            
    return res

# проверка работы
if __name__ == "__main__":
    s = "hello world"
    print("Текст:", s)
    
    encoded, tree = huffman_encode(s)
    print("Закодировано:", encoded)
    
    decoded = huffman_decode(encoded, tree)
    print("Декодировано:", decoded)
