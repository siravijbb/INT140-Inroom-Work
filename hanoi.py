def tower_of_hanoi(n, source, temp_tower, target,step=0):
    if n == 0:
        return step
    step = tower_of_hanoi(n-1,source,temp_tower,target,step)
    step = step + 1
    print(f"step{step} Move disk {n} from {source} to {target}")
    step = tower_of_hanoi(n - 1, temp_tower, source, target,step)
    return step

def tower2(disk,step=0):
    if disk == 0:
        return step
    tower2(disk-1,step)
    step = step + 1
    tower2(disk-1,step)
    return print(step)



x =5
tower2(x)
tower_of_hanoi(x, 'A', 'C', 'B')  # A is source, B is auxiliary, C is target
