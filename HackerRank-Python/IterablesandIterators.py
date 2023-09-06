from itertools import combinations

def calculate_groups(iterable, group_size):
    groups = list(combinations(iterable, group_size))
    return groups

N = int(input())
lst1 = input().split()
group_sizee = int(input())

groups1 = calculate_groups(lst1, group_sizee)
total_group_count = len(groups1)

count = 0
for group in groups1:
    if "a" in group:
        count += 1

result = count / total_group_count
formatted_result = f"{result:.4f}"
print(formatted_result)