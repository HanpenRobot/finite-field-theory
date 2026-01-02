import numpy as np
import tqdm


import itertools


def get_latin_square(N: int, alpha: int) -> np.ndarray[np.float64]:
    """ラテン方陣の次数Nと直線の傾きalphaに対応するラテン方陣を求める関数

    ラテン方陣の定義: 次数のNの正方行列の
    「行」と「列」に重複なく1,2,...,Nの数字が一回ずつ出現している時、その行列を「ラテン方陣」とよぶ
    """

    L = range(0, N)
    res = np.ones((N, N))  # サイズN×Nの2次元配列
    for item in tqdm.tqdm(itertools.product(L, repeat=2)):
        ans = (lambda x: (x[1] - alpha * x[0]) % N)(
            item
        )  # L(y-ax)=(y-ax) mod N を計算している L(y-ax)=(y-ax) mod N (直線の式)
        res[item[0]][item[1]] = ans

    return res


N = 3
alpha = 1
res = get_latin_square(N=N, alpha=1)
print(f"{N=}次、{alpha=}のラテン方陣:")
print(f"{res}")


# N=3、alpha=1の時の結果:
# N=3次、alpha=1のラテン方陣:
# [[0. 1. 2.]
#  [2. 0. 1.]
#  [1. 2. 0.]]
