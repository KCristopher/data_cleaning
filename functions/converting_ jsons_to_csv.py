import json
import csv

def load_json_with_one_outermost_key_and_iterab_of_jsons(json_file, items_name : str):
    """
    Loads a json file and returns the data.

    Parameters
    ----------
    json_file : str.
        The path to the json file.
    items_name : str.
        The name of the outermost key in the json file, which is like
        a name for all items.
    
    Returns
    -------
    list.
        A list of dictionaries.
    
    Example
    -------
    print(load_json_with_one_outermost_key_and_iterab_of_jsons('C:\\Users\\Predator\\Desktop\\sample_json.json', 'names'))

        [{'firstname': 'Jan', 'age': 11}, {'firstname': 'Krysia', 'age': 14}]
    
    """
    with open(json_file, "r") as f :
        content = json.load(f)
        data_under_key = content[items_name]
    
    return data_under_key

def write_data_to_csv(file_name : str, data : list, fieldnames : list) -> None :
    """
    Writes data to a csv file.

    Parameters
    ----------
    file_name : str.
        The name of the csv file.
    
    Returns
    -------
    None.
    
    Example
    -------
    write_data_to_csv()
    """
    with open(file_name, 'w', newline = '') as csvfile :
        
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(data)



def write_json_with_one_outermost_key_and_iterab_of_jsons_to_csv(json_file, items_name : str, csv_file_name : str, fieldnames : list) -> None :
    """
    Writes data from a json file with one outermost key and
    a list of jsns under that key to a csv file.

    Parameters
    ----------
    json_file : str.
        The path to the json file.
    items_name : str.
        The outermost key in the json file, which is like the name of the items.
    csv_file_name : str.
        The path of the csv file to be created.
    fieldnames : list.
        The names of the columns in the csv file to be created.
    data : list.
        The data to be written to the csv file.
    
    Returns
    -------
    None.
    
    Example
    -------
    write_json_with_one_outermost_key_and_iterab_of_jsons_to_csv(json_file='C:\\Users\\Predator\\Desktop\\sample_json.json', items_name='names',\
    csv_file_name='C:\\Users\\Predator\\Desktop\\sample_csv.csv', fieldnames=['firstname', 'age'])

    """
    data = load_json_with_one_outermost_key_and_iterab_of_jsons(json_file = json_file, items_name = items_name)
    write_data_to_csv(file_name = csv_file_name, data = data, fieldnames = fieldnames)



def get_iterab_of_dictions_given_file_of_jsons(file_name : str) -> List[dict] :
    """"
    Given a file of JSON objects, return a list of dictionaries.
    Each dictionary is one JSON object from the file.

    Parameters
    ----------
    file_name : str. The name of the file containing JSON objects.

    Returns
    -------
    list. A list of dictionaries. Each dictionary is one JSON object from the file.

    Example
    -------
    >>> get_iterab_of_dictions_given_file_of_jsons('tweets.json') [ : 5 ]
    
        [{'keyword': 'COVID-19',
        'likes': 1,
        'tweet': 'The headline kinda makes it sound like the AP acknowledges that the “emergency measures” taken during the COVID-19 crisis  killed more than 1 million Americans.'},
        {'keyword': 'COVID-19',
        'likes': 0,
        'tweet': "ATLANTIC CITY — The city's Police Athletic League has received $65,000 from the state to restart a youth boxing program shuttered during the COVID-19 pandemic."},
        {'keyword': 'COVID-19',
        'likes': 0,
        'tweet': "I feel like Diana's line she draws is if his school experience was interpreted by Covid-19 or not"},
        {'keyword': 'COVID-19',
        'likes': 1,
        'tweet': 'COVID-19 was the single most fatal communicable disease in living memory.  It could literally kill you for going to the grocery store.
        But sure, call it a "civili liberties" attack if that makes you sleep better at night.'},
        {'keyword': 'COVID-19',
        'likes': 0,
        'tweet': 'Studies: Dogs can detect COVID-19 with greater than 80% sensitivity | CIDRAP'}]
    """

    data_list = []
    current_json_lines = []

    with open(file_name, 'r') as file_js:
        for line in file_js:
            # Strip any leading or trailing whitespace from the line
            line = line.strip()

            if line.startswith('{') and line.endswith('}'):
                # This line contains a complete JSON object
                current_json_lines.append(line)
                data = json.loads(''.join(current_json_lines))
                data_list.append(data)
                current_json_lines = []
            elif line.startswith('{'):
                # This line starts a JSON object that spans multiple lines
                current_json_lines.append(line)
            elif line.endswith('}'):
                # This line ends a JSON object that spans multiple lines
                current_json_lines.append(line)
                data = json.loads(''.join(current_json_lines))
                data_list.append(data)
                current_json_lines = []
            else:
                # This line is part of a JSON object that spans multiple lines
                current_json_lines.append(line)

    # Now you have a list of JSON objects in data_list
    return data_list
                                                                
