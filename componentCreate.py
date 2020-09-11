import sys, os

legend = {
    'ß': 'importStatements',
    '*': 'background',
    '/': 'color',
    '×': 'styledComponent',
    '÷': ''
}

basicHeader = """
import React from 'react'

const Header = () => {
    return(
        <div>
        </div>
    )
}

export default Header;
"""

headerStyles = """
import styled from 'styled-components'



const HeaderContainer = styled.div`
    width: 100%;
    display: flex;
    flex-direction: row;
    padding: 16px 32px;
    background: *;
`

const Brand = styled.div`
    display: flex;
    flex-direction: row;
    width: 20%;
    margin-right: auto;
    @media screen and (max-width: 768px){
        width: 80%;
    }
`

const BrandLogo = styled.img`
    height: 50px;
    width: auto;
    object-fit: contain;
    margin-right: 8px;
`

const BrandText = styled.h1`
    font-size: 1.5rem;
    margin: 0;
`
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

args = sys.argv

os.system('cls')

def help():
    print("Help Menu")
    print("Basic syntax: createComponent.bat [type] [special tags]")
    print("""
    Types:
        navbar - simple navbar

    Special Tags:
        basic - basic component, no styling or functionality
        print - prints desired component structure into console
        darkMode - creates component with dark mode toggle
        search - adds searchbar into component
        help - prints options for desired component
        logo - adds logo from assets
        styled - imports styled components
    """)



if len(args) == 1:
    print("Not Enough Arguments")
    opt = input("Do you wish to open help menu? (Y/N): ")
    if opt.lower() == 'y':
        help()
    else:
        print("Task Failed Successfully!")
        print()
        print("Thanks for trying me.\nHave a nice day!")
