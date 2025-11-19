# acm_main.py
import sys
from io import TextIOWrapper

def solve(stdin: TextIOWrapper, stdout):
    """
    在这里写你的题解：
    从 stdin 读，向 stdout 写。
    下面是一个示例：读取n、两行数组，输出某个值。
    """
    data = stdin.read().strip().split()
    if not data:
        return
    it = iter(data)

    n = int(next(it))
    A = [int(next(it)) for _ in range(n)]
    B = [int(next(it)) for _ in range(n)]

    # 示例逻辑：如果 sum(A)!=sum(B) 输出 -1，否则输出正差和
    if sum(A) != sum(B):
        print(-1, file=stdout)
        return
    ans = sum(max(b - a, 0) for a, b in zip(A, B))
    print(ans, file=stdout)

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
