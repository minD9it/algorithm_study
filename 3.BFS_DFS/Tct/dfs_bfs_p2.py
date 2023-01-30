from collections import deque

n, m = map(int, input().split())

maze = []
for i in range(n):
  maze.append(list(map(int, input())))

# 상하좌우로 움직일 수 있음
moving = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 최단 거리를 구해야 하는 것이기 때문에 bfs
# python에서 bfs는 deque를 활용
def bfs(x, y):
  queue = deque()
  # 일단 방문하면 바로 큐에 넣어야 함
  queue.append((x, y))

  # 큐가 empty인 상태일 때까지
  while queue:
    # 큐에 제일 먼저 넣은 거 꺼내기
    x, y = queue.popleft()

    # 상하좌우로 움직일 거임
    for move in moving:
      nx = x + move[0]
      ny = y + move[1]

      # 미로판을 벗어나는 경우
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      
      if maze[nx][ny] == 0: # 지나갈 수 없는 길
        continue

      if maze[nx][ny] == 1: # 지나갈 수 있는 길
        # 계속해서 증가함 +1씩
        maze[nx][ny] = maze[x][y] + 1
        queue.append((nx, ny))

  # 미로판의 마지막에 최단 경로 값이 저장되어 있기 때문
  return maze[n-1][m-1]

print(bfs(0, 0))
