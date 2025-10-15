
def create_student_record(name, age, major, gpa):
    return {'name': str(name), 'age': int(age), 'major': str(major), 'gpa': float(gpa)}


   
def get_value_safely(dictionary, key, default=None):
    if key in dictionary:
        return dictionary[key]
    else:
        return default 


def merge_dictionaries(dict1, dict2): 
    merged = dict1.copy()                            # on copie le premier pour ne pas le modifier
    merged.update(dict2)                                # on ajoute dict2 (écrase les clés identiques)
    return merged


import string

def count_word_frequency(text):
    text= text.lower()                          #minuscule
    for punct in string.punctuation:
        text=text.replace(punct,"")             #enlever ponctuation
    words=text.split()                          #separer en mots
    frequencies={}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word]= 1
    return frequencies



def invert_dictionary(dictionary):
    inverted = {value: key for key, value in dictionary.items()}
    return inverted

    


def filter_dictionary(dictionary, keys_to_keep):
    result={}
    for key in keys_to_keep:
        if key in dictionary:
            result[key]=dictionary[key]
    return result



def group_by_first_letter(words):
    grouped={}
    for word in words:
        if not word:
            continue
        first_letter= word[0].lower()
        grouped.setdefault(first_letter,[]).append(word)
    return grouped


def calculate_grades_average(students):
    averages={}
    for name, grades in students.items():
        if grades:
            avg= sum(grades)/len(grades)
            averages[name] =round(avg,2)
        else:
            averages[name]= 0.0
    
    return averages
        

def nested_dict_access(data, keys):
    current=data 
    for key in keys:
        if isinstance(current, dict) and key in current:
            current=current[key]
        else: 
            return None
    return current
    

# Test cases
if __name__ == "__main__":
    print("Testing Dictionary Operations...")
    print("-" * 50)

    # Test create_student_record
    print("Test 1: create_student_record")
    result = create_student_record("Alice", 20, "CS", 3.8)
    print(f"Result: {result}")
    assert result == {'name': 'Alice', 'age': 20, 'major': 'CS', 'gpa': 3.8}
    print("✓ Passed\n")

    # Test get_value_safely
    print("Test 2: get_value_safely")
    d = {'a': 1, 'b': 2}
    assert get_value_safely(d, 'a') == 1
    assert get_value_safely(d, 'c', 'Not found') == 'Not found'
    print("✓ Passed\n")

    # Test merge_dictionaries
    print("Test 3: merge_dictionaries")
    result = merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
    print(f"Result: {result}")
    assert result == {'a': 1, 'b': 3, 'c': 4}
    print("✓ Passed\n")

    # Test count_word_frequency
    print("Test 4: count_word_frequency")
    result = count_word_frequency("hello world hello")
    print(f"Result: {result}")
    assert result == {'hello': 2, 'world': 1}
    print("✓ Passed\n")

    # Test invert_dictionary
    print("Test 5: invert_dictionary")
    result = invert_dictionary({'a': 1, 'b': 2, 'c': 3})
    print(f"Result: {result}")
    assert result == {1: 'a', 2: 'b', 3: 'c'}
    print("✓ Passed\n")

    # Test filter_dictionary
    print("Test 6: filter_dictionary")
    result = filter_dictionary({'a': 1, 'b': 2, 'c': 3, 'd': 4}, ['a', 'c'])
    print(f"Result: {result}")
    assert result == {'a': 1, 'c': 3}
    print("✓ Passed\n")

    # Test group_by_first_letter
    print("Test 7: group_by_first_letter")
    result = group_by_first_letter(['apple', 'banana', 'apricot', 'blueberry'])
    print(f"Result: {result}")
    assert result == {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}
    print("✓ Passed\n")

    # Test calculate_grades_average
    print("Test 8: calculate_grades_average")
    result = calculate_grades_average({
        'Alice': [90, 85, 88],
        'Bob': [75, 80, 78]
    })
    print(f"Result: {result}")
    assert result == {'Alice': 87.67, 'Bob': 77.67}
    print("✓ Passed\n")

    # Test nested_dict_access
    print("Test 9: nested_dict_access")
    data = {'a': {'b': {'c': 123}}}
    assert nested_dict_access(data, ['a', 'b', 'c']) == 123
    assert nested_dict_access(data, ['a', 'x']) is None
    print("✓ Passed\n")

    print("=" * 50)
    print("All tests passed! Excellent work!")
