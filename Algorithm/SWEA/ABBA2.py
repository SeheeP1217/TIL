import sys
sys.stdin = open('input.txt')

def check(lst):
    for i in range(len(lst)//2):
        if lst[i] != lst[-i-1]:
            return False
    return True


T = int(input())
for tc in range(1, T+1):
    arr1 = [list(input()) for _ in range(100)]
    arr2 = list(zip(*arr1))

    mx = 0
    for length in range(100, 1, -1):
        if mx > length:
            break
        for i in range(100-length+1):
            if mx == length:
                break
            for lst1, lst2 in zip(arr1, arr2):
                if check(lst1[i:i+length]) or check(lst2[i:i+length]):
                    mx = length
                    break
    print(f"#{tc} {mx}")


