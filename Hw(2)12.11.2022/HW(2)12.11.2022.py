data = input("Enter The message: ")

conversion_code = {

    '1': '2', '3': '4', '5': '6', '7': '8', '9': '10',
    '11': '12', '13': '14', '15': '16', '17': '18', '19': '20', '21': '22',
    '23': '24', '25': '26', '27': '28', '29': '30'



}


converted_data = ""

for y in range(0, len(data)):
    if data[y] in conversion_code.keys():
        converted_data += conversion_code[data[y]]
    else:
        converted_data += data[y]


print(converted_data)