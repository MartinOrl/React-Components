import sys, os

args = sys.argv
os.system('cls')

legend = {
    'ß': 'importStatements',
    '*': 'background',
    '/': 'color',
    '×': 'styledComponent',
    '÷': 'componentStructure',
    '¤': 'reduxConnect'
}

coreNavbar = """
    import React from 'react'
    ß

    const Header = () => {
        return(
            ÷
        )
    }

    export default Header;
"""

basicNavbar = """
            <div display={{display: 'flex', flexDirection:'row', padding:'16px 32px'}}>
                <a href='#'>Brand</a>
                <ul style={{listStyle: 'none', display:'flex', flexDirection:'row'}}>
                    <li style={{margin:'0 8px'}} ><a href='#'>Home</a></li>
                    <li style={{margin:'0 8px'}} ><a href='#'>About</a></li>
                    <li style={{margin:'0 8px'}} ><a href='#'>Contact</a></li>
                </ul>
            </div>
"""

NavbarStyles = """
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

def productionReady(target, keys):
    targetList = list(target)
    for key in keys:
        if(key in targetList):
            targetList[targetList.index(key)] = ''
    return "".join(targetList)

def help():
    print("Help Menu")
    print("Basic syntax: createComponent.bat [type] [special tags]")
    print("""
    Types:
        navbar - simple navbar

    Special Tags:
        basic - basic component, no styling or functionality
        print - prints desired component structure into console
        darkMode - creates component with dark mode toggle         #! Not Deployable
        search - adds searchbar into component                     
        help - prints options for desired component                #! Not Deployable
        logo - adds logo from assets
        styled - imports styled components
        redux - connects into Redux
    """)

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


def build(component, options=''):
    if(component.lower() == 'navbar'):
        if(len(options) > 0):
           print("Complex Build Started")
        else:
           temp = insertItem(basicNavbar, coreNavbar, "÷")
           temp = productionReady(temp, ["ß","÷"])
           print(temp)


if len(args) == 1:
    print("Not Enough Arguments")
    opt = input("Do you wish to open help menu? (Y/N): ")
    if opt.lower() == 'y':
        help()
    else:
        print("Task Failed Successfully!")
        print()
        print("Thanks for trying me.\nHave a nice day!")

if len(args) > 1:
    specials = []
    if(args[2:] == []):
        opt = input("Do you want to add some parameters? (Y/N): ")
        if(opt.lower() == 'y'):
            print("Type -help if you wish to know the arguments")
            newOpt = input(">:")
            if(newOpt.lower() == '-help'):
                help()
                newOpt = input(">:")
            else:
                specials = newOpt.split(" ")
        else:
            build(args[1], specials)
    else:
        specials = args[2:]
        print("Paste Success")
        build(args[1], specials)
            


