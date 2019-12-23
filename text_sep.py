vocSize, sentCount = map(int, input().split())
Voc = dict()
max_word_size = 0
total = 0.0
for i in range(vocSize):
    count, word = input().split()
    Voc[word] = int(count)
    max_word_size = max(max_word_size, len(word))
    total += int(count)
for i in range(sentCount):
    S = input()
    s = len(S)
    d, ans, value = [0] * s, [''] * s, [0] * s
    d[0], ans[0], value[0] = 1, S[0], 1
    for y in range(s):
        if y >= 1:
            d[y] = d[y - 1]
            ans[y] = ans[y - 1]
            ans[y] += ' ' + S[y]
            value[y] = value[y - 1] + 1
        if y < max_word_size and S[:y + 1] in D:
            substr = S[:y + 1]
            if Voc[substr] * (total ** (value[y] - 1)) > d[y]:
                d[y] = Voc[substr]
                ans[y] = substr
                value[y] = 1
        for j in range(max(y - max_word_size, 0), y):
            substr = S[j + 1:y + 1]
            if substr in Voc:
                if d[j] * Voc[substr] * (total ** (value[y] - value[j] - 1)) > d[y]:
                    d[y] = d[j] * Voc[substr]
                    ans[y] = ans[j]
                    ans[y] += ' ' + substr
                    value[y] = value[j] + 1
    print(ans[s - 1])
