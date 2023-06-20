import heapq

def huffman(f):
    H = []
    for x in range(len(f)):
        heapq.heappush(H, (f[x], str(x)))  # O(n log n)

    while len(H) > 1:
        a = heapq.heappop(H)  # 가장 작은 빈도수 , 해당문자 O( log n)
        b = heapq.heappop(H)  # 두 번째로 작은 빈도수, 해당문자 O( log n)
        heapq.heappush(H, (a[0] + b[0], '(' + a[1] + ' ' + b[1] + ')')) # O( log n)

    tree_string = heapq.heappop(H)[1]
    return tree_string

def repeat_huf(tree_string):
    depth = 0
    bit_lengths = {}

    temp = ""

    for char_List in tree_string:
        if char_List.isdigit():
            temp += char_List
        elif char_List == " ":
            if temp:
                bit_lengths[temp] = depth
                temp = ""
        elif char_List == "(":
            depth += 1
        elif char_List == ")":
            if temp:
                bit_lengths[temp] = depth
                temp = ""
            depth -= 1

    return bit_lengths


f = [int(x) for x in input().split()]
tree_string = huffman(f)
bit_lengths = repeat_huf(tree_string)
bit_count = 0



for char_List, length in bit_lengths.items():
    if char_List == " ":
        continue
    else:
        bit_count += length * int(f[int(char_List)])

print(bit_count)

