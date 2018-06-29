from lxml import html
import requests
import re
import math

errors = []
for i in range(4,19):
    try:
        if( i<10):
         page = requests.get('https://sanskritdocuments.org/mirrors/mahabharata/mbhK/telugu/mahabharata-k-0'+str(i)+'-telugu.html')
        else:
         page = requests.get('https://sanskritdocuments.org/mirrors/mahabharata/mbhK/telugu/mahabharata-k-'+str(i)+'-telugu.html')

        tree = html.fromstring(page.content)

        htmlfile = page.content.decode('utf8')
        
        text = re.sub(r'<.*?>','',htmlfile)
        #text = re.sub(r'[a-zA-Z]','',text)
        print text
        f= open("./Telugu/" + str(i) + ".utf8","w")
        f.write(text.encode('utf-8'))
        print("processed page number " + str(i))
    except requests.exceptions.ConnectionError:
        errors.append(str(i))
        print("Error at page number " + str(i))

log = open("errors.txt","w")
log.write(",".join(errors))


