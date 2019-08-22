import requests
import sys
import os
from time import localtime, strftime
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

# Set in your bash profile, get from Google:  https://console.developers.google.com/apis/credentials
SPD_API_KEY = os.environ.get('SPD_API_KEY')

# Documentation: https://developers.google.com/speed/docs/insights/v5/get-started
def main(strategy="mobile"):
    try:
        strategy = sys.argv[1]
    except IndexError:
        print("You can pass 'mobile' or 'desktop' as parameter. Running mobile by default.")
    # Pull URLS from 'pagespeed.txt' to query against API.
    with open('pagespeed.txt') as pagespeedurls:
        stamp = strftime("%Y-%m-%d_at_%H.%M.%S", localtime())
        csv_out = Path("results/")
        download_dir = csv_out / f'{strategy}-{stamp}.csv'
        file = open(download_dir, 'w')
        content = pagespeedurls.readlines()
        content = [line.rstrip('\n') for line in content]
        columnTitleRow = "URL, Score, First Contentful Paint, First Interactive\n"   # CSV header
        file.write(columnTitleRow)

        def get_speed(line):
            # Query API.
            x = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={line}&strategy={strategy}&key={SPD_API_KEY}'
            print(f'Requesting {x}...')
            r = requests.get(x)
            final = r.json()
            
            try:
                urlid = final['id']
                split = urlid.split('?') # This splits the absolute url from the api key parameter
                urlid = split[0] # This reassigns urlid to the absolute url
                ID = f'URL ~ {urlid}'
                ID2 = str(urlid)
                # JSON paths: https://developers.google.com/speed/docs/insights/v4/reference/pagespeedapi/runpagespeed
                urlfcp = final['lighthouseResult']['audits']['first-contentful-paint']['displayValue']
                FCP = f'First Contentful Paint ~ {str(urlfcp)}'
                FCP2 = str(urlfcp[:-2])
                urlfi = final['lighthouseResult']['audits']['interactive']['displayValue']
                FI = f'First Interactive ~ {str(urlfi)}'
                FI2 = str(urlfi[:-2])
                urlscore = final['lighthouseResult']['categories']['performance']['score']
                SC = f'Score ~ {str(urlscore)}'
                SC2 = str(urlscore)
            except KeyError:
                print(f'<KeyError> One or more keys not found {line}.')
            
            try:
                row = f'{ID2},{SC2},{FCP2},{FI2}\n'
                file.write(row)
            except NameError:
                print(f'<NameError> Failing because of KeyError {line}.')
                file.write(f'<KeyError> & <NameError> Failing because of nonexistant Key ~ {line}.' + '\n')
            
            try:
                print(ID)
                print(SC) 
                print(FCP)
                print(FI)
            except NameError:
                print(f'<NameError> Failing because of KeyError {line}.')
        with ThreadPoolExecutor() as executor:  # Make multithreaded, 5x your processors by default
            executor.map(get_speed, content)

        file.close()
if __name__ == '__main__':
    main()
