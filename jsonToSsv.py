import os
import csv
import json
from src.helper import *
import time

# Đường dẫn tới thư mục chứa các file JSON
json_dir = 'data/json'

# Đường dẫn tới thư mục chứa các file CSV
csv_dir = 'data/csv'


# Sắp xếp danh sách các tệp tin theo thời gian sửa đổi gần nhất
json_files = sorted(os.listdir(json_dir), key=lambda x: os.path.getmtime(os.path.join(json_dir, x)), reverse=True)

# Lặp qua tất cả các file JSON trong thư mục json
for json_file in json_files:
    # Đường dẫn tới file JSON
    json_path = os.path.join(json_dir, json_file)
    
    # Đọc dữ liệu từ file JSON
    with open(json_path, 'r') as f:
        data = json.load(f)

    
    #     if check_for_null(data):
    #         print(json_path)
    #         continue



    # Tạo tên file CSV tương ứng
    csv_file = os.path.splitext(json_file)[0] + '.csv'
    
    # Đường dẫn tới file CSV
    csv_path = os.path.join(csv_dir, csv_file)

    # Mở file CSV để ghi dữ liệu
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Ghi tiêu đề cho các cột trong file CSV
        initColumn(writer)
        # writer.writerow(['Name', 'Link', 'Full Name', 'Image Source', 'Model', 'Part No', 'Part Description', 'Sale Price'])

        # Lặp qua tất cả các mục trong file JSON và ghi vào file CSV
        groupProductCount=0
        for item in data:
            print(item['name'])
            model=item['model']
            # if model is None:
            #     print(json_path)
            #     break
            SKU=getSKU(model)
            if len(item)>0:
                SKU=SKU+ str(groupProductCount)
                groupProductCount= groupProductCount+1
            Grouped_products = list(set([i["parts_list_PartNo"] for i in item['infor']]))
            Grouped_products=list_to_string(Grouped_products)
            breadcrumb_menu=item['breadcrumb_menu']
            Categories='OEM Parts, PWC Parts & Supplies, PWC Parts & Supplies >'+ breadcrumb_menu.split(" / ")[1]
            Attribute_1_values=breadcrumb_menu.split(" / ")[2]
            Attribute_3_values=breadcrumb_menu.split(" / ")[0]
            Model=getModel(item['model'])
            writer.writerow([
                    'grouped',
                    SKU,
                    Grouped_products,
                    item['nameChildren'], #name
                    '1',
                    '0',
                    'hidden',
                    '',
                    '',
                    '',
                    '',
                    'taxable',
                    '',
                    '1',
                    '',
                    '',
                    '0',
                    '0',
                    '',
                    '',
                    '',
                    '',
                    '1',
                    '',
                    '',
                    '',
                    '',
                    Categories,
                    '',
                    '',
                    item['image_src'],
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '0',
                    'Year Model',
                    Attribute_1_values,
                    '1',
                    '1',
                    'Model OEM',
                    Model,
                    '1',
                    '1',
                    'Brands OEM',
                    Attribute_3_values,
                    '1',
                    '1',])

            for simple in item['infor']:
                  # Đọc dữ liệu từ file JSON
                if check_null_elements(simple.values()):
                    continue


                simpleName= simple['parts_list_descrip'].replace(simple['parts_list_PartNo'], '').lstrip('. ')
                # RegularPrice = (float(simple['parts_list_SalePrice'].replace(",", ""))/float(simple['parts_list_QtyReq'].replace(",", ""))) if (simple['parts_list_QtyReq'].isdigit() and simple['parts_list_QtyReq'] != 0 )else float(simple['parts_list_SalePrice'].replace(",", ""))
                # RegularPrice = "{:.2f}".format(RegularPrice)
                if simple['parts_list_QtyReq'].isdigit():
                    RegularPrice = (float(simple['parts_list_SalePrice'].replace(",", ""))*150)
                else:
                    RegularPrice = 0

                RegularPrice = "{:.2f}".format(RegularPrice)
                print(RegularPrice)
                if RegularPrice==0:
                    print('waiting-------')
                    time.sleep(10)
                # time.sleep(10)
                writer.writerow(
                    [   'simple',
                        simple['parts_list_PartNo'],
                        '',
                        simpleName,
                        '1',
                        '0',
                        'hidden',
                        '',
                        '',
                        '',
                        '',
                        'taxable',
                        '',
                        '1',
                        '',
                        '',
                        '0',
                        '0',
                        '',
                        '',
                        '',
                        '',
                        '1',
                        '',
                        '',
                        RegularPrice,
                        simple['parts_list_QtyReq'],
                        'OEM Parts, PWC Parts & Supplies',
                        '',
                        '',
                        simple['image_main'],
                        '',
                        '',
                        '',
                        '',
                        '',
                        '',
                        '',
                        '0',
                        'Year Model',
                        Attribute_1_values,
                        '1',
                        '1',
                        'Model OEM',
                        Model,
                        '1',
                        '1',
                        'Brands OEM',
                        Attribute_3_values,
                        '1',
                        '1',]
                    )

