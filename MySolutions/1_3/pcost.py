


def portfolio_cost(file_name):
    with open(file_name) as f:
        f = f.read().split()
        total = 0
        for i in range(0, len(f)-3, 3):

            try:
                total += int(f[i+1]) * float(f[i+2])
            except ValueError as e:
                print("Couldn't parse:", f[i+1], f[i+2])
                print(e) 

        return total

print(portfolio_cost('../../Data/portfolio.dat'))
print(portfolio_cost('../../Data/portfolio3.dat'))

