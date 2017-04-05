# Ordering a set of people. each one knows who they should follow but lost
order = [{"name": 'a', "value": ''}, 
         {"name": 'd', "value": 'c'},
         {"name": 'c', "value": 'b'},
         {"name": 'b', "value": 'a'},]

for a in order:
    if not a.get("value"):
        startDict = a
orderList = []
orderList.append(startDict)
j = 0
i = 0
while i < len(order):
    for dict1 in order:
        if dict1.get('value') == orderList[j].get('name'):
            orderList.append(dict1)
            j += 1
    i += 1
print orderList