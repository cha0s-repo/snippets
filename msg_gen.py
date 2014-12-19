#!/usr/bin/env python

def test_GenerateXml(filename):
    import xml.dom.minidom
    dom = GenerateXml();
    filename = "./" + filename
    f= open(filename, 'w')
    dom.writexml(f, addindent='  ', newl='\n',encoding='utf-8')
    f.close()

def GenerateXml():
    import xml.dom.minidom
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, 'xml', None)
    root = dom.documentElement  
    
    nameE=dom.createElement('name')
    nameT=dom.createTextNode('linux')
    nameE.appendChild(nameT)
    root.appendChild(nameE)
    
    ageE=dom.createElement('age')
    ageT=dom.createTextNode('30')
    ageE.appendChild(ageT)
    root.appendChild(ageE)
    print(dom.toprettyxml())
    return dom

if __name__ == "__main__":
    test_GenerateXml("new.xml")
