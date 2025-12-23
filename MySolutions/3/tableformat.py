

lines = open('../../Data/portfolio.csv')

def convert_csv(lines, function):
    lines = lines.read().split()  
    headers = lines[0].split(",")
    final_list = []
    for l in range(1, len(lines)):
        row = lines[l].split(",")
        final_list.append(function(headers, row)) 
    return final_list                
       
def make_dict(headers, row): return dict(zip(headers, row))


print(convert_csv(lines, make_dict))

