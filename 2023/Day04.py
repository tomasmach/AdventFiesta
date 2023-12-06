import pandas as pd
import numpy as np
import time

def part1():
    df = pd.read_csv("2023/input.txt", header=None, sep="\s+")
    margin = (df.iloc[0, :] == "|").idxmax()
    win = df.iloc[:, 2:margin].to_numpy()
    card = df.iloc[:, margin + 1 :].to_numpy()
    wins = np.array([np.sum(np.isin(win[i], card[i])) for i in range(win.shape[0])])
    wins = wins[wins != 0]
    print(np.sum(2 ** (wins - 1)))


def part2():
    start_time = time.time()

    df = pd.read_csv("2023/input.txt", header=None, sep="\s+")
    margin = (df.iloc[0, :] == "|").idxmax()
    win = df.iloc[:, 2:margin].to_numpy()
    card = df.iloc[:, margin + 1 :].to_numpy()
    wins = np.array([np.sum(np.isin(win[i], card[i])) for i in range(win.shape[0])])

    piles = np.ones(len(wins), dtype=int)
    for i, cs in enumerate(piles):
        for w in range(wins[i]):
            piles[i + 1 + w] += cs

    end_time = time.time()
    print(sum(piles))
    print("Time taken:", end_time - start_time, "seconds")


part1()
part2()

