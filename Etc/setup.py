import random
BUG = 'BUG'

def insert_bug(line):    
    total_bugs = 3
    positions = [random.randrange(line.index(':')+1, len(line)) for _ in range(total_bugs)]
    positions.sort(reverse = True)
    for pos in positions:
        line = line[:pos] + BUG + line[pos:]
    return line

src = open('Exercise2/lyrics.txt')
cnt = 1
while line := src.readline():
    print (cnt)
    dst = open(f'Exercise1/{cnt}.txt', 'w')
    dst.write(insert_bug(line))
    dst.close()
    cnt += 1
