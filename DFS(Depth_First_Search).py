import sys

sys.setrecursionlimit(5000)

def DFS(G, v):
    print(v, end=' ')
    global curr_time  # pre, post를 위한 time stamp
    # 그래프 G의 노드 v를 DFS 방문한다
    visited[v] = True
    pre[v] = curr_time
    curr_time += 1
    for w in G[v]:
        if visited[w] == False:
            DFS(G, w)
    post[v] = curr_time
    curr_time += 1


def DFSAll(G):
    # 그래프 G를 DFS 방문한다
    for v in range(n):
        if visited[v] == False:
            DFS(G, v)


# 입력 처리
n, m = [int(x) for x in input().split()]
G = [[] for _ in range(n)]
# G 입력 받아 처리
for i in range(m):
    v, w = map(int, input().split())
    G[v].append(w)
    G[w].append(v)
    G[w].sort()
    G[v].sort()

# visited, pre, post 리스트 정의와 초기화
visited = [False] * n
pre = [0] * n
post = [0] * n
# curr_time = 1로 초기화
curr_time = 1

DFSAll(G)

print()
for i in range(n):
    print([pre[i], post[i]], end=' ')