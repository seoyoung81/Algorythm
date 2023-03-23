1. DFS
    
    > 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회 방법
    > 
    - 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 **후입선출** 구조의 **스택** 사용
    - 재귀 사용 할 때 주의 할 점(파이썬에서 재귀 깊이 늘려주기)
    
    ```python
    import sys
    sys.setrecursionlimit(10**6)
    ```
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d63f901f-1201-422b-851c-a8091d2a6322/Untitled.png)
    
    ```python
    def dfs(v): # 지금 현재 탐색하는 정점 v
    	visited[v] = 1 # 정점 방문기록 찍기
    	print(v, end = ' ')  # 방문을 한 경우 출력
    	# 현재 v는 시작정점, 인접한 정점 중 방문을 안한 곳
    	for w in range(1, V+1):
    		if arr[v][w] == 1 and visited[w] == 0: # 지금 현재 정점이 1이고, 방문을 안한 곳이라면
    			dfs(w)
    
    dfs(1)
    ```
    
    ```python
    def DFS(v,lines, visited):
        print(v, end = ' ')
        visited[v] = 1 # 방문체크
    
        # 방문할 노드 리스트에 담기
        nodes = []
        for i in range(0, len(lines), 2):
            if lines[i] == v:
                nodes.append(lines[i+1])
    
        print(nodes)
        # nodes.sort() #오름차순으로 방문하기위해 정렬
    
        # 방문시작
        for node in nodes:
            if not visited[node]: # 방문 안했으면
                print(f'{node} 방문시작')
                DFS(node, lines, visited)
    
    # 간선정보
    lines = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
    # 방문체크용 리스트
    visited = [0]*(max(lines) + 1)
    DFS(1,lines,visited)
    # print(visited)
    
    # 출력
    1 [2, 3]
    2 방문시작
    2 [4, 5]
    4 방문시작
    4 [6]
    6 방문시작
    6 [7]
    7 방문시작
    7 []
    5 방문시작
    5 [6]
    3 방문시작
    3 [7]
    ```
    
2. BFS
    
    > 너비 우선 탐색: 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
    > 
    - 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선 탐색을 진행해야 하므로 , **선입선출** 형태의 자료구조인 큐를 활용
    - 거리가 같은 곳 순서로 방문
    - 큐 구현
  ```python
    from collections import deque

    queue = deque()
    queue.append(5)   # 삽입
    queue.popleft()   # 삭제  
    ```

    ```python
    def BFS(G, v, n): # 그래프 G, 탐색 시작점 v
	visited = [0] * (n+1) # n: 정점의 개수
	queue = [] # 큐 생성
	queue.append(v)  # 시작점 v를 큐에 삽입(enqueue)
	visited[v] = 1   # 시작점 인큐되었음을 표시
	while queue:    # 큐가 비어있지 않은 경우
		t = queue.pop(0)  # 큐의 첫번째 원소 반환(dequeue)
		visit(t)    # 정점 t에서 할 일
		for i in G[t]:    # t와 연결된 모든 정점에 대해
			if not visited[i]:    # 방문되지 않은 곳이라면
				queue.append(i)    # 큐에 넣기
				visited[i] = visited[n] + 1   # n으로부터 1만큼(누구로부터 인큐되었는가)
    ```