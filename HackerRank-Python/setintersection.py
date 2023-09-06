englsh_nwsppr = int(input())
englsh_student = set(map(int, input().split()))

french_nwsppr = int(input())
french_student = set(map(int, input().split()))

print(len(englsh_student.intersection(french_student)))