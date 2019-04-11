import requests
import json

# Documentation: https://developers.google.com/speed/docs/insights/v5/get-started

# JSON paths: https://developers.google.com/speed/docs/insights/v4/reference/pagespeedapi/runpagespeed

# Create a local file called 'pagespeed.txt' and populate it with URLs to test
with open('pagespeed.txt') as pagespeedurls:
    download_dir = 'pagespeed-results.csv'
    file = open(download_dir, 'w')
    content = pagespeedurls.readlines()
    content = [line.rstrip('\n') for line in content]

    columnTitleRow = "URL, First Contentful Paint, First Interactive\n"
    file.write(columnTitleRow)


    for line in content:
        # This is the google pagespeed api url structure, using for loop to insert each url in .txt file
        x = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={line}&strategy=mobile'
        r = requests.get(x)
        final = r.json()
        
        try:
            urlid = final['id']
            split = urlid.split('?') # This splits the absolute url from the api key parameter
            urlid = split[0] # This reassigns urlid to the absolute url
            ID = f'URL ~ {urlid}'
            ID2 = str(urlid)
            urlfcp = final['lighthouseResult']['audits']['first-contentful-paint']['displayValue']
            FCP = f'First Contentful Paint ~ {str(urlfcp)}'
            FCP2 = str(urlfcp)
            urlfi = final['lighthouseResult']['audits']['interactive']['displayValue']
            FI = f'First Interactive ~ {str(urlfi)}'
            FI2 = str(urlfi)
        except KeyError:
            print(f'<KeyError> One or more keys not found {line}.')
        
        try:
            row = f'{ID2},{FCP2},{FI2}\n'
            file.write(row)
        except NameError:
            print(f'<NameError> Failing because of KeyError {line}.')
            file.write(f'<KeyError> & <NameError> Failing because of nonexistant Key ~ {line}.' + '\n')
        
        try:
            print(ID) 
            print(FCP)
            print(FI)
        except NameError:
            print(f'<NameError> Failing because of KeyError {line}.')

    file.close()