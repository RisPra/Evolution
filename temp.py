def recur(num: int) -> int:
    if num == 0:
        return num
    _ = num - 1
    recur(_)
    print(num)
    
recur(10)