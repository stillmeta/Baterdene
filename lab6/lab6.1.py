def num_trees(n):
    G = [0] * (n + 1)
    G[0], G[1] = 1, 1  
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            G[i] += G[j - 1] * G[i - j]
    return G[n]
n = 3
print("bst-iin too", n, "zangilaa", num_trees(n))
