
def save_to_json(data, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving to JSON: {e}")
        return False
    
def load_from_json(filename):
    try:
        with open(filename, 'r') as f:   
            return json.load(f)
    except Exception as e:
        print(f"Error loading from JSON: {'e'}")
        return None
   

import json
def save_contacts_to_file(contacts, filename="contacts.json"):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(contacts, f, indent=4)
        return True
    except Exception as e:
        print("error:", e)
        return False
        

import json
import os
def load_contacts_from_file(filename="contacts.json"):
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            contacts= json.load(f)
            return contacts
    except Exception as e:
        print("error:", e)
    return []   


import json
import os  
def append_contact_to_file(contact, filename="contacts.json"):
    try:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                contacts=json.load(f)
        else:
            contacts = []
        contacts.append(contact)

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(contacts, f, indent=4)
        return True
    except Exception as e:
        print ("error:",e)
        return False

import shutil
def backup_file(source_filename, backup_filename):
    try:
        shutil.copy(source_filename, backup_filename)
        return True
    except Exception as e:
        print("error:",e)
        return False
    


import json
import os

def get_file_stats(filename):
    if not os.path.exists(filename):
        return {'exists': False, 'type': None, 'count': 0, 'size_bytes': 0}

    try:
        size_bytes = os.path.getsize(filename)

        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if isinstance(data, list):
            data_type = 'list'
            count = len(data)  
        elif isinstance(data, dict):
            data_type = 'dict'
            count = len(data.keys()) 
        else:
            data_type = 'other'
            count = 0

        return {
            'exists': True,
            'type': data_type,
            'count': count,
            'size_bytes': size_bytes
        }

    except Exception as e:
        print("Erreur :", e)
        return None

   

import json
import os
def merge_json_files(file1, file2, output_file):
    
    try:
       
        if os.path.exists(file1):
            with open(file1, 'r', encoding='utf-8') as f1:
                data1 = json.load(f1)
        else:
            data1 = []

        if os.path.exists(file2):
            with open(file2, 'r', encoding='utf-8') as f2:
                data2 = json.load(f2)
        else:
            data2 = []

        
        if not isinstance(data1, list) or not isinstance(data2, list):
            print(" Les fichiers ne contiennent pas des listes JSON.")
            return False

        merged_data = data1 + data2

        with open(output_file, 'w', encoding='utf-8') as f_out:
            json.dump(merged_data, f_out, indent=4)

        return True  

    except Exception as e:
        print("Error :", e)
        return False



import json
import os

def search_json_file(filename, key, value):
   
    if not os.path.exists(filename):
        print("not found :", filename)
        return []

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

       
        if not isinstance(data, list):
            print("no dictionary in the file")
            return []


        matches = []
        for item in data:
            if isinstance(item, dict) and key in item and item[key] == value:
                matches.append(item)

        return matches

    except Exception as e:
        print("Erreur lors de la recherche :", e)
        return []



# Test cases
if __name__ == "__main__":
    print("Testing JSON File Operations...")
    print("-" * 50)

    # Test 1: save_to_json and load_from_json
    print("Test 1: save_to_json and load_from_json")
    test_data = {'name': 'Alice', 'age': 25, 'city': 'Paris'}
    save_to_json(test_data, 'test_data.json')
    loaded_data = load_from_json('test_data.json')
    print(f"Saved and loaded: {loaded_data}")
    assert loaded_data == test_data
    print("✓ Passed\n")

    # Test 2: save_contacts_to_file and load_contacts_from_file
    print("Test 2: save and load contacts")
    contacts = [
        {'name': 'Alice', 'phone': '555-0001', 'email': 'alice@email.com'},
        {'name': 'Bob', 'phone': '555-0002', 'email': 'bob@email.com'}
    ]
    save_contacts_to_file(contacts, 'test_contacts.json')
    loaded_contacts = load_contacts_from_file('test_contacts.json')
    print(f"Loaded {len(loaded_contacts)} contacts")
    assert len(loaded_contacts) == 2
    assert loaded_contacts[0]['name'] == 'Alice'
    print("✓ Passed\n")

    # Test 3: append_contact_to_file
    print("Test 3: append_contact_to_file")
    new_contact = {'name': 'Charlie', 'phone': '555-0003', 'email': 'charlie@email.com'}
    append_contact_to_file(new_contact, 'test_contacts.json')
    contacts = load_contacts_from_file('test_contacts.json')
    print(f"After append: {len(contacts)} contacts")
    assert len(contacts) == 3
    print("✓ Passed\n")

    # Test 4: backup_file
    print("Test 4: backup_file")
    backup_file('test_contacts.json', 'test_contacts_backup.json')
    backup_data = load_from_json('test_contacts_backup.json')
    print(f"Backup created with {len(backup_data)} items")
    assert len(backup_data) == 3
    print("✓ Passed\n")

    # Test 5: get_file_stats
    print("Test 5: get_file_stats")
    stats = get_file_stats('test_contacts.json')
    print(f"File stats: {stats}")
    assert stats is not None
    assert stats['exists'] == True
    assert stats['type'] == 'list'
    assert stats['count'] == 3
    print("✓ Passed\n")

    # Test 6: merge_json_files
    print("Test 6: merge_json_files")
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    save_to_json(list1, 'list1.json')
    save_to_json(list2, 'list2.json')
    merge_json_files('list1.json', 'list2.json', 'merged.json')
    merged = load_from_json('merged.json')
    print(f"Merged list: {merged}")
    assert merged == [1, 2, 3, 4, 5, 6]
    print("✓ Passed\n")

    # Test 7: search_json_file
    print("Test 7: search_json_file")
    results = search_json_file('test_contacts.json', 'name', 'Alice')
    print(f"Search results: {results}")
    assert len(results) == 1
    assert results[0]['name'] == 'Alice'
    print("✓ Passed\n")

    # Cleanup
    print("Cleaning up test files...")
    import os
    for file in ['test_data.json', 'test_contacts.json', 'test_contacts_backup.json',
                 'list1.json', 'list2.json', 'merged.json']:
        if os.path.exists(file):
            os.remove(file)
    print("✓ Cleaned up\n")

    print("=" * 50)
    print("All tests passed! You've mastered JSON file operations!")
