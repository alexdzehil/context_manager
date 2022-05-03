class HelloContextManager:
    def __enter__(self):
        print('Entering the context...')
        return 'Hello, World!'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Leaving the context...')
        if isinstance(exc_val, IndexError):
            print(f'An exception occured in your with block: {exc_type}')
            print(f'Exception message: {exc_val}')
            return True


with HelloContextManager() as hello:
    print('Hello')
    hello[100]

print('Continue normally from here...')
