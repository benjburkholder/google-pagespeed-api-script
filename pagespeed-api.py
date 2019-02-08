import requests
import json
from datetime import datetime

# Documentation: https://developers.google.com/speed/docs/insights/v5/get-started

# JSON paths: https://developers.google.com/speed/docs/insights/v4/reference/pagespeedapi/runpagespeed

with open('pagespeed.txt') as pagespeedurls: # Create a local file called 'pagespeed.txt' and populate it with URLs to test
    content = pagespeedurls.readlines()
    content = [line.rstrip('\n') for line in content]

    for line in content:
        file = open('pagespeed-results.csv', 'a') # csv will be created automatically on local machine
        x = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={line}&strategy=mobile' # This is the google pagespeed api url structure, using for loop to insert each url in .txt file
        r = requests.get(x)
        final = r.json()
        
        try:
            urlid = final['id']
            split = urlid.split('?') # This splits the absolute url from the api key parameter
            urlid = split[0] # This reassigns urlid to the absolute url
            ID = f'URL: {urlid}'
            urlfcp = final['lighthouseResult']['audits']['first-contentful-paint']['displayValue']
            FCP = f'First Contentful Paint: {str(urlfcp)}'
            urlfi = final['lighthouseResult']['audits']['interactive']['displayValue']
            FI = f'First Interactive: {str(urlfi)}'
        except KeyError:
            print(f'<KeyError> One or more keys not found {line}.')
        
        try:
            file.write('Timestamp: ' + str(datetime.now()) + '\n')
            file.write(ID + '\n')
            file.write(FCP + '\n')
            file.write(FI + '\n')
            file.write('\n')
        except NameError:
            print(f'<NameError> Failing because of KeyError {line}.')
            file.write(f'<KeyError> & <NameError> Failing because of nonexistent Key - {line}.' + '\n')
            file.write('\n')
        
        file.close()
        
        try:
            print('Timestamp: ' + str(datetime.now()))
            print(ID)
            print(FCP)
            print(FI)
            print('\n')
        except NameError:
            print(f'<NameError> Failing because of KeyError {line}.')
        