import pandas as pd

items = pd.DataFrame({
    'id': ['ball', 'pen', 'mug'],
    'color': ['white', 'black', 'red'],
    'price': [12.00, 2.50, 7.80]
})

sales_q1 = pd.DataFrame({
    'id': ['ball', 'pen', 'pen', 'mug', 'ball'],
    'month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar'],
    'qty': [10, 35, 25, 12, 18]
})

sales_q2 = pd.DataFrame({
    'id': ['ball', 'pen', 'mug', 'mug', 'pen'],
    'month': ['Apr', 'Apr', 'May', 'May', 'Jun'],
    'qty': [20, 22, 15, 19, 14]
})


q12 = pd.concat([sales_q1, sales_q2], ignore_index=True)
print(q12)


itemsQ12 = pd.merge(q12, items, on='id')

print(itemsQ12)
print("______________________________________")

sumQ12 = itemsQ12['qty'] * itemsQ12['price']
itemsQ12['Sum'] = sumQ12
print(itemsQ12)

print("______________________________________")

sumQ12Stack = itemsQ12.stack()
print(sumQ12Stack)

print("______________________________________")

sumQ12UnStack = sumQ12Stack.unstack()
print(sumQ12UnStack)


print("______________________________________")

sumQ12Drop = sumQ12UnStack.drop('price', axis=1)
print(sumQ12Drop)


print("______________________________________")

sumQ12Drops = sumQ12Drop.drop([1,2,3,4,5,6,7,8,9])
print(sumQ12Drops)
"""
my_df.drop([])
"""