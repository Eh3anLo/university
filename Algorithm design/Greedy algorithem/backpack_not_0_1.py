def pw_sort(prices,weights):
    data_pack = []
    for i in range(0, len(prices)):
        price_on_weight = round(prices[i]/weights[i],1)
        new_data = (prices[i],weights[i],price_on_weight)
        data_pack.append(new_data)

    data_pack.sort(key=lambda item:item[2], reverse=True) # sort base on price/weight value
    return data_pack

def knapsack():
    data_pack = pw_sort(prices,weights) # sorting items base on price/weight desending
    remain_capacity = backpack_weight
    max_price = 0
    i = 0
    for item in data_pack:
        if item[1] <= remain_capacity:
            remain_capacity -= item[1]
            solution[i] = 1
            max_price += item[0]
        else:
            amount = remain_capacity/item[1]
            solution[i] = amount
            max_price += amount*item[0]
            break
        i+=1
    return max_price , data_pack

prices = list(map(int,input("Enter prices of objects (ex:1,23,45,6): ").split(','))) # -> 15,24,25
weights = list(map(int,input("Enter weights of objects (ex:1,23,45): ").split(','))) # -> 10,15,18
backpack_weight = int(input("Backpack weight: ")) # -> 20
solution = [0 for i in range(len(prices))]   

max_price , data_pack = knapsack()
print(f"{max_price=}") ## max_price=31.5
print(f"{data_pack=}") ## data_pack=[(24, 15, 1.6), (15, 10, 1.5), (25, 18, 1.4)]
print("output : " , solution) ## [1, 0.5, 0]




