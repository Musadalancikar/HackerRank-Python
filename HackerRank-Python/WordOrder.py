
N = int(input())

word_count = {}
for i in range(N):
    word = input()
    word_count[word] = word_count.get(word, 0) + 1

distinct_words = list(word_count.keys())
word_occurrences = list(word_count.values())

print(len(distinct_words))
print(*word_occurrences)


    