class Cache:
    def __init__(self):
        self.cache = []
    
    def push(self, item):
        self.cache.append(item)
    
    def pop(self):
        if not self.size():
            raise BufferError
        self.cache.pop()
    
    def size(self):
        return len(self.cache)
    

def inspect(brackets):
    cache = Cache()
    
    for bracket in brackets:
        if bracket == '(':
            cache.push(bracket)
        elif bracket == ')':
            try:
                cache.pop()
            except BufferError:
                return False
        else:
            raise ValueError(f'Unknown simbol -> "{bracket}"')
    
    return False if cache.size() else True


if __name__ == '__main__':
    assert inspect('()()()()(((()))())') , '()()()()(((()))()) == True'
    assert not inspect('(((('), '(((( == False'
    assert inspect(''), 'Empty string -> True'
    assert not inspect('())'), '()) == False'
    try:
        inspect('(((d)))')
    except ValueError:
        print('Test - ok!')
