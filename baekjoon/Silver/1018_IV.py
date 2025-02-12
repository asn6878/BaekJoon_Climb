H, W = list(map(int,input().split()))
board = [list(input()) for _ in range(H)]

min_answer = 64
for h in range(H - 7):
    for w in range(W - 7):
        black_odd = 0
        black_even = 0
        cnt = 0
        # h가 홀수일때 검은색이 홀수? 짝수? 이거 기준으로 더 작은거 비교 필요
        for tmp_h in range(h, h + 8):
            for tmp_w in range(w, w + 8):
                if tmp_h % 2 == 0:
                    if tmp_w % 2 == 0:
                        if board[tmp_h][tmp_w] == "B":
                            black_odd += 1
                        else:
                            black_even += 1
                    else:
                        if board[tmp_h][tmp_w] == "B":
                            black_even += 1
                        else:
                            black_odd += 1
                else:
                    if tmp_w % 2 == 1:
                        if board[tmp_h][tmp_w] == "B":
                            black_odd += 1
                        else:
                            black_even += 1
                    else:
                        if board[tmp_h][tmp_w] == "B":
                            black_even += 1
                        else:
                            black_odd += 1
                cnt += 1 
        
        min_answer = min(min_answer, min(black_odd, black_even))

print(min_answer)