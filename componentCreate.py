import os
import sys
legend = {
    'ß': 'import statements'
}

basicHeader = """
import React from 'react'
ß


const Header = () => {
    return(
        <div>
        </div>
    )
}

export default Header;
"""

def insertItem(item, target, key):
    targetList = list(target)
    try:
        index = targetList.index(key)
    except Exception as e:
        print("Invalid key.")
    else:
        targetList.insert(index, item)
        print("Insertion Succesful")
        return "".join(targetList)

a = insertItem('Lol', basicHeader, 'ß')

print('Arguments: ', str(sys.argv))
print()
print('Path: ', os.getcwd())
