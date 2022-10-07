import base64
import xlrd

workbook = xlrd.open_workbook("imge3.xls")
worksheet = workbook.sheet_by_name("Sheet1")
count = 0 
for idx in range(1, worksheet.nrows+1):
    excel_data = worksheet.cell(idx-1,1).value  #base64
    imge_name = worksheet.cell(idx-1,0).value  #imge name
    
    imge_name = imge_name +'.JPG'
    print(imge_name)
    count= count + 1
    if excel_data.startswith('data:image/jpeg;base64,'):
        with open(imge_name, 'wb') as jpg:
            jpg.write(base64.b64decode(excel_data.strip()[22:] + '===='))
            
print(count)


