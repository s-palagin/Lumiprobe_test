def maximum_occurrence(string):
    if type(string) is not str or not len(string):
        return (())
    frequency = {}
    string = string.lower()
    for char in set(string):
        frequency[char] = string.count(char)
    sorted_frequency = sorted(frequency.items(), key=lambda item: item[1])
    return sorted_frequency.pop()

if __name__ == '__main__':
    assert maximum_occurrence('aaaaAAbc') == ('a', 6), '("aaaAAAbc") == ("a", 6)'
    assert maximum_occurrence('') == (), 'Empty tuple'
    print('Test - ok!')
