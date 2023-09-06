T = int(input())

for i in range(T):
    size = int(input())
    blocks = list(map(int, input().split()))

    for i in range(size-1):
        if blocks[0] >= blocks[len(blocks)-1]:
            a = blocks[0]
            blocks.pop(0)
        elif blocks[0] < blocks[len(blocks)-1]:
            a = blocks[len(blocks)-1]
            blocks.pop(len(blocks)-1)
        else:
            pass

        if len(blocks) == 1:
            print("Yes")
            break

        if((blocks[0] > a) or (blocks[len(blocks)-1] > a)):
            print("No")
            break