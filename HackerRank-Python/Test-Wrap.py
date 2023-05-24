import textwrap

def wrap(string, max_width):

    t = "\n".join(textwrap.wrap(string,width=max_width))
    return t

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)