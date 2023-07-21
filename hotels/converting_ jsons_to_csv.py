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




                                                                
