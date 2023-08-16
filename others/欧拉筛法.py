from typing import List


def oularshaifa(n: int) -> List[int]:
    prime = [0] * n
    visited = [False] * (n + 1)
    for i in range(2, len(visited)):
        if visited[i] != True:
            prime[0] += 1
            prime[prime[0]] = i

        for j in range(1, prime[0] + 1):
            if i * prime[j] <= n:
                visited[i * prime[j]] = True
                if i % prime[j] == 0:
                    break

    print(prime)


if __name__ == "__main__":
    print(oularshaifa(10))
