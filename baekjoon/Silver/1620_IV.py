N, M = map(int, input().split())

pokemons = dict()
pokeidx = dict()

for i in range(N):
    pokemon = input()
    pokemons[pokemon] = i+1
    pokeidx[i+1] = pokemon

for i in range(M):
    q = input()
    if q.isdigit():
        print(pokeidx[int(q)])
    else:
        print(pokemons[q])