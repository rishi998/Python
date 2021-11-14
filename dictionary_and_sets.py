myDict={
    "Fast":"In a quick manner",
    "Rishi":"A coder",
    "anotherdict":{'Rishi':'Smart',
                    'superman':'Marvel'}
}
# print(myDict['Rishi'])
# print(myDict.keys()) #prints the keys of the dictionary
# print(myDict.values())#prints the values of the dictionary
# print(myDict.items())# prints the (keys,values) of the dictionary
# print(myDict['anotherdict']['Rishi'])
updatedict={
    "YashGarg":"friend",
    "Ishita":"friend"
}
myDict.update(updatedict)
# print(myDict)

print(myDict.get("Rishi2"))