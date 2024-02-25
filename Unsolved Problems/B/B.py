n = int(input())
str = input()
edges = []
for t in range(n - 1):
    edges.append(input().split())

adj = {}
left_map = "{[("
right_map = ")]}"

#Initialize adjacency list
for i in range(1, n + 1):
    adj[i] = []

for i in range(len(edges)):
    edge = edges[i]
    a = int(edge[0])
    b = int(edge[1])
    adj[a].append(b)

def dfs(node, p_left, p_right, b_left, b_right, c_left, c_right, adj):
    
    num = 0
    p_left_temp = p_left + (str[node - 1] == "(")
    p_right_temp = p_right + (str[node - 1] == ")")
    b_left_temp = b_left + (str[node - 1] == "{")
    b_right_temp = b_right + (str[node - 1] == "}")
    c_left_temp = c_left + (str[node - 1] == "[")
    c_right_temp = c_right + (str[node - 1] == "]")
    
    if p_left_temp == p_right_temp and b_left_temp == b_right_temp and c_left_temp == c_right_temp:
        num += 1
    
    for n in adj[node]:
        #num += dfs(n, p_left, p_right, b_left, b_right, c_left, c_right, adj)
        num += dfs(n, p_left_temp, p_right_temp, b_left_temp, b_right_temp, c_left_temp, c_right_temp, adj)

    return num

def check_balance(s):
    stack = []

    balanced_map = {
        "{" : "}",
        "(" : ")",
        "[" : "]"
    }   

    for i in range(len(s)):
        if len(stack) > 0 and stack[-1] in balanced_map and balanced_map[stack[-1]] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    
    return len(stack) == 0  

ways = 0
for i in range(1, n + 1):
    ways += dfs(i, 0, 0, 0, 0, 0, 0, adj)

print(ways)

    