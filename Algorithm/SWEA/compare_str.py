#보이어 무어
def boyer_moore(pattern, text):
    M = len(pattern)
    N = len(text)
    i = 0
    while i <= N-M:
        j = M - 1
        while j >= 0:
            if pattern[j] != text[i+j]:
                move = find(pattern, text[i+M-1])
                break
            j = j - 1
        if j == -1:
            return 1
        else:
            i += move
    return 0

def find(pattern, char):
    for i in range(len(pattern)-2, -1, -1):
        if pattern[i] == char:
            return len(pattern) -i-1
    return len(pattern)

T = int(input())
for test_case in range(1, T+1):
    N = input()
    M = input()
    print(f"#{test_case} {boyer_moore(N, M)}")
