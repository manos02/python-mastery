

lines = open('../../Data/portfolio.csv')

def convert_csv(lines, function):
    lines = lines.read().split()  
    headers = lines[0].split(",")
    final_list = []
    for l in range(1, len(lines)):
        row = lines[l].split(",")
        final_list.append(function(headers, row)) 
    return final_list                
       
def make_dict(headers, row):
    return dict(zip(headers, row))


# print(convert_csv(lines, make_dict))

def convert_csv_map(lines, function):
    lines = lines.read().split()  

    lines = list(map(lambda x: x.split(","), lines))
    headers = lines.pop(0)
    return [function(headers, row) for row in lines]
 
print(convert_csv_map(lines, make_dict))

