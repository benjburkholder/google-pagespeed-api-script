import requests
import json

# Documentation: https://developers.google.com/speed/docs/insights/v5/get-started

with open('pagespeed.txt') as pagespeedurls: # Create a local file called 'pagespeed.txt' and populate it with URLs to test
    content = pagespeedurls.readlines()
    content = [line.rstrip('\n') for line in content]

    for line in content:
        file = open('pagespeed-results.txt', 'a') # csv will be created automatically on local machine
        x = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={line}?AIzaSyDcig6xGXax1iw02L5AyN0HRPfTUN_JSPY' # This is the google pagespeed api url structure, using for loop to insert each url in .txt file
        r = requests.get(x)
        final = r.json()
        urlid = final['id']
        ID = urlid
        urlfcp = final['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']
        FCP = f'First Contentful Paint: {urlfcp}'
        urlinput = final['loadingExperience']['metrics']['FIRST_INPUT_DELAY_MS']
        INPUT = f'First Input Delay: {urlinput}'
        file.write(ID + '\n')
        file.write(FCP + '\n')
        file.write(INPUT + '\n')
        file.close()

        print(ID) 
        print(FCP)
        print(INPUT)