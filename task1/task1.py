import sys
N = int(sys.argv[1])
M = int(sys.argv[2])

N_pack = []

for i in range(1, N+1):
    N_pack.append(i)

k = 0
path = str()
FIRST_TRY = True

while k != 0 or FIRST_TRY:
    FIRST_TRY = False
    path += str(N_pack[k]) + ' '
    k = (k + M - 1) % N

print(path)
