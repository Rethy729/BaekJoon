import collections

class TrieNode:
    def __init__(self):
        self.end = False #이 node가 단어의 끝 node임을 표시하는 bool
        self.children = collections.defaultdict(TrieNode) #default 값이 TrieNode인 dict // 한 node에 연결된 children node
        self.children_count = 0 #한 node에서 뻗어나가는 children의 개수

class Trie:
    def __init__(self):
        self.root = TrieNode()  #Root노드가 하나 존재

    def insert(self, word):
        curr_node = self.root #위에 init에서 정의된 root 노드에서부터 시작
        for char in word:     #들어온 word의 각 글자마다
            if char not in curr_node.children: #새롭게 뻗은 가지마다 children_count를 하나씩 더함
                curr_node.children_count += 1
            curr_node = curr_node.children[char] #현재 노드에 각 글자를 새로운 Trienode로 추가 (defaultdict를 사용해 코드를 깔끔하게)
        curr_node.end = True #반복이 끝나고, 이 node가 단어의 끝임을 알려주는 bool (end)를 True로 바꿈

    def integrity(self, word): #문제에서 요구하는 integrity를 검사
        curr_node = self.root
        for char in word:
            if curr_node.end and curr_node.children_count != 0 : #현재 노드가 끝인데 계속 이어진 children node가 존재하는 경우
                return False
            curr_node = curr_node.children[char]
        return True

total_case = []
n = int(input())
for _ in range(n):
    m = int(input())
    test_case = []
    for _ in range(m):
        num = input()
        test_case.append(num)
    total_case.append(test_case)

for case in total_case:
    phone_num_trie = Trie()
    for number in case:
        phone_num_trie.insert(number)

    integrity_check = False
    for number in case:
        if not phone_num_trie.integrity(number):
            integrity_check = True
            break

    if integrity_check:
        print ("NO")
    else:
        print ("YES")

#타임아웃 ㅠ

