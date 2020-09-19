import sys, os
from pprint import pprint

args = sys.argv[1:]
os.system('cls')    

styledTemplate = """import styled from 'styled-components';"""

def make(filename, text):
    temp = open(filename, "w")
    temp.write(text)
    temp.close()


def build(name, connect="", typeClass=''):
    componentName = name.title()
    styleImport = "import {} from " + f"'/{componentName}Styles.jsx'"
    connectImport = ""
    export = f'export default {componentName};'
    component = f"""const {componentName}""" + """ = () => {
    return(
        <div>
        
        </div>
    )
}
    """

    if(connect):
        connectImport = """import { connect } from 'redux'\nimport { createStructuredSelector } from 'reselect'"""
        export = """const mapState = createStructuredSelector({\n    \n});\n\nconst mapDispatch = dispatch => ({\n    \n});\n\nexport default connect(mapState,mapDispatch)"""+f"""({componentName})"""
    if(typeClass):
        component = f"""class {componentName}""" + """ extends React.Component{
    constructor(){
        super();
        this.state = {

        }
    }
    componentDidMount(){

    }

    render(){
        return(
            <div>

            </div>
        )
    }
};
        """
    
    template = f"""import React from 'react';
{connectImport}

{styleImport}

{component}

{export}    
    """
    return template
    

for file in args:
    props = file.split(":")
    file = props[0]
    typeClass = False
    connect = False
    print(file)
    if 'class' in props:
        typeClass = True
    if 'connect' in props:
        connect = True
    componentStructure = build(file, connect, typeClass)
    filename = file.lower() + ".jsx"
    stylesname = file.lower() + "Styles.jsx"
    os.chdir("src/components")
    os.mkdir(file.lower())
    os.chdir(file.lower())
    make(filename, componentStructure)
    make(stylesname, styledTemplate)
    print("Made", file, "component")
    os.chdir("../../..")