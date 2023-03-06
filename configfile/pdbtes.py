import pdb

def example_function():
    x = 1
    y = 2
    pdb.set_trace()
    z = x + y
    print(z)

if __name__ == '__main__':
    example_function()
