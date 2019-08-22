# Google Pagespeed API Bulk Query

This Python3 script queries Google's PageSpeed Insights for a list of URLs, then prints selected results and saves to CSV.

You can specify whether to test for Desktop or Mobile (it defaults to mobile). It is set to select only the performance Score, First Contentful Paint, and First Interactive values. You can easily change that.

## Install

This program requires Python 3. Assuming you have it, simply git clone or download this project and then run it from the command line.

## Use

### Setup

List all the URLs on a single line in a txt file named `pagespeed.txt`. Assuming you're analyzing a single large website, your `sitemap.xml` is a good place to get each URL you want the search engines to care about.

To avoid running afoul of Google's API rate limits, get an [API key from Google](https://console.developers.google.com/apis/credentials).

Best practice is to add the key to your bash profile if you're on Mac or Linux. For example:

```bash
 $ nano ~/.bash_profile
 ```
 and then add the following line:
 ```
 export SPD_API_KEY=YOUR_API_KEY
 ```
Restart your terminal after you save it.

If you're not a naturally paranoid person, you're not sharing this program, and you're not committing it to any repositories, you can just put the key directly into `pagespeed-api.py` as `SPD_API_KEY`. This is a bad practice and I don't recommend it.

### Running it

From the project root directory, to get Mobile results:
```
 $ python3 pagespeed-api.py
```
```
 $ python3 pagespeed-api.py mobile
```
To get Desktop results:
```
 $ python3 pagespeed-api.py desktop
```

You will have something like the following printed to your screen:
```
Requesting https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://www.example.com&strategy=mobile&key=YOUR_API_KEY...
Requesting https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://www.example.com&strategy=mobile&key=YOUR_API_KEY...
URL ~ https://www.example.com/
Score ~ 1.0
First Contentful Paint ~ 0.8 s
First Interactive ~ 0.8 s
URL ~ https://www.example.com/
Score ~ 1.0
First Contentful Paint ~ 0.8 s
First Interactive ~ 0.8 s
```
And you should have a file named `pagespeed-results-mobile-2019-08-21_23:33:59.csv` in your directory. It's results will look like:

```
URL, Score, First Contentful Paint, First Interactive
https://www.example.com/,1.0,0.8 s,0.8 s
https://www.example.com/,1.0,0.8 s,0.8 s
https://www.example.com/,1.0,0.8 s,0.8 s
https://www.example.com/,1.0,0.8 s,0.8 s
https://www.example.com/,1.0,0.8 s,0.8 s
https://www.example.com/,1.0,0.8 s,0.8 s
https://www.example.com/,1.0,0.8 s,0.8 s
https://www.example.com/,1.0,0.8 s,0.8 s
https://www.example.com/,1.0,0.8 s,0.8 s
https://www.example.com/,1.0,0.8 s,0.8 s
```

## Credit

This is a fork of [ibebeebz pagespeed project](https://github.com/ibebeebz/google-pagespeed-api-script).