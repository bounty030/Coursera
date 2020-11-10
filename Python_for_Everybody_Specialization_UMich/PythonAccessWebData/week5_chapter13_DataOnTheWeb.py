#week 5 - Web Services and XML

#--------13.1 - Data on the Web
#send data over a network from python to java
#the data has to be in a universal format to be read by different
#programming languages ->XML and JSON (serialized documents)

#In computing, serialization (US spelling) or serialisation 
# (UK spelling) is the process of translating a data structure or 
# object state into a format that can be stored (for example, in a 
# file or memory data buffer) or transmitted (for example, across a 
# computer network) and reconstructed later (possibly in a different 
# computer environment).


#-------13.2 - eXtensible Markup Language (XML)
#XML uses tags which start with <> and end with </>
#e.g.:
"""
<people>
    <person>
        <name>Chuck</name>
        <phone>303 4456</phone>
    </person>
    <person>
        <name>Tim</name>
        <phone>622 7421</phone>
    </person>
</people>
"""

#primary purpose of XML is to share structured data
#start tag:     <person>
#end tag:       </person>
#text content:  Tim
#attribute:     <name hide="yes">Tim</name>
#self closing tag: <email hide="yes"/> (empty tag, no text content)

#intendation and whitespaces do not matter 

"""
#a simple application that parses some XML and extracts some data 
# elementsfrom the XML

import xml.etree.ElementTree as ET


#triple quoted string is a multi-line string
data='''
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes" />
</person>'''

tree=ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
print("Phone Attribute:" ,tree.find("phone").get("type"))
"""

"""
#if the xml has a tag with multiple tags such as user here:
import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user') #returns a list with all user tags
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))
"""

