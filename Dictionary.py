#dictionary = A changeable, unordered collectionof unique "key:valeu" (pair of values)
#             Fast because they use hashing, allow us to access a value quickly
#             {'key':'value'}

capitals = {'USA':'Washington',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

print(capitals['India'])
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key,value in capitals.items():
    print(key,value)

capitals.update({'Germany':'Berlim'})
capitals.pop({'China'})

print(capitals)