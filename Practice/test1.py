n=6
card = [_ for _ in range(1, n+1)]
print(card)
card_a, card_b = [0 for _ in range(n // 2)], [0 for _ in range(n // 2)]
print(card_a, card_b)

for i in range(0, n):
    if i < n // 2:
        card_a[i] = card[i]
    else:
        card_b[i-n] = card[i]
print(card_a, card_b)