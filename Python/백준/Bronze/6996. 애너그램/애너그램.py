import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    word1, word2 = input().rstrip().split()
    if sorted(word1) == sorted(word2):
        print(f"{word1} & {word2} are anagrams.")
    else:
        print(f"{word1} & {word2} are NOT anagrams.")