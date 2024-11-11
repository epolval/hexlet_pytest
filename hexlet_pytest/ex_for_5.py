
def example_for_test(x):
    print('Hello!')
    stack = []
    stack.append(x)
    print(f'Stack is empty: {not stack}')
    result = stack.pop()
    print(f'Stack is empty: {not stack}')
    return result

#example_for_test()