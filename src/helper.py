def getSKU(s):
    if '[' in s:
        value = s[s.index('[')+1:s.index(']')]
    else:
        value = '-'.join(s.split()[1:])
    return value
def getModel(s):
    value = '-'.join(s.split()[1:])
    return value

def check_for_null(arr):
    for item in arr:
        for field in item:
            if item[field] is None:
                return True # Return True if any null value is found
        for infor_item in item['infor']:
            for field in infor_item:
                if infor_item[field] is None:
                    return True # Return True if any null value is found in the 'infor' list
    return False # Return False if no null values are found


def check_null_elements(lst):
    for element in lst:
        if element is None:
            return True
    return False

def list_to_string(my_list, separator=', '):
    for element in my_list:
        if not isinstance(element, str):
            return None
    return separator.join(my_list)

import os

def get_numbers_without_json(folder_path, a):
    # Tạo một danh sách các số xuất hiện trong tên file JSON
    json_numbers = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".json"):
            json_number = file_name.split("-")[1].split(".")[0]  # Lấy số trong tên file
            json_numbers.append(json_number)

    # Tạo một danh sách các phần tử của mảng a không xuất hiện trong danh sách số của các file JSON
    a_without_json_numbers = [x for x in a if str(x) not in json_numbers]

    return a_without_json_numbers



# inpit file
def initColumn(writer):
    writer.writerow([
    'Type',
    'SKU',
    'Grouped products',
    'Name',
    'Published',
    'Is featured?',
    'Visibility in catalog',
    'Short description',
    'Description',
    'Date sale price starts',
    'Date sale price ends',
    'Tax status',
    'Tax class',
    'In stock?',
    'Stock',
    'Low stock amount',
    'Backorders allowed?',
    'Sold individually?',
    'Weight (kg)',
    'Length (cm)',
    'Width (cm)',
    'Height (cm)',
    'Allow customer reviews?',
    'Purchase note',
    'Sale price',
    'Regular price',

    'Meta: qty_required',

    'Categories',
    'Tags',
    'Shipping class',
    'Images',
    'Download limit',
    'Download expiry days',
    'Parent',
    'Upsells',
    'Cross-sells',
    'External URL',
    'Button text',
    'Position',
    'Attribute 1 name',
    'Attribute 1 value(s)',
    'Attribute 1 visible',
    'Attribute 1 global',
    'Attribute 2 name',
    'Attribute 2 value(s)',
    'Attribute 2 visible',
    'Attribute 2 global',
    'Attribute 3 name',
    'Attribute 3 value(s)',
    'Attribute 3 visible',
    'Attribute 3 global',]
    )
