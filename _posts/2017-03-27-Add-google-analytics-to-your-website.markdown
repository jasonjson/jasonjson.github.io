---
layout: post
title: Add google analytics to your website
date: 2017-03-27
tags:
- Html
categories:
- Reading Notes
author: Jason
---
Add google analytics to your website

## Adding analytics.js to your site

1. Create an account in [Google Analytics](https://analytics.google.com/).
2. Get a tracking ID, like UAXXXX-X.
3. Add following script to head html, which gets distributed to each page.

    ```javascript
    <!-- Google Analytics -->
    <script>
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

    ga('create', 'UA-XXXXX-Y', 'auto');
    ga('send', 'pageview');
    </script>
    <!-- End Google Analytics -->
    ```

## Create Google Analytics query and pageview
1. Create an account in [Account Explorer](https://ga-dev-tools.appspot.com/account-explorer/)
2. Create query based on your need
3. Find table id, like ga:xxxxxx

## Create service account for website authoriation
1. Create an account in [Google Console](https://console.developers.google.com)
2. Create a service account, download json file secret key
3. Find service account id, which is an email address

## Service side authorization
1. Go to <em>User Management</em> in <em>admin</em> secion in [Google Analytics](https://analytics.google.com/), add service account id as a user and set up permissions.
2. Install the Google API Client Library

    ```python
    sudo pip install --upgrade google-api-python-client
    ```
3. Use the following code and downloaded JSON key file to get an access token.

    ```python
    from oauth2client.service_account import ServiceAccountCredentials

    # The scope for the OAuth2 request.
    SCOPE = 'https://www.googleapis.com/auth/analytics.readonly'

    # The location of the key file with the key data.
    KEY_FILEPATH = 'path/to/json-key.json'

    # Defines a method to get an access token from the ServiceAccount object.
    def get_access_token():
      return ServiceAccountCredentials.from_json_keyfile_name(
          KEY_FILEPATH, SCOPE).get_access_token().access_token
    ```
4. Load the embeded API Librarys.

    ```javascript
    <script>
    (function(w,d,s,g,js,fs){
      g=w.gapi||(w.gapi={});g.analytics={q:[],ready:function(f){this.q.push(f);}};
      js=d.createElement(s);fs=d.getElementsByTagName(s)[0];
      js.src='https://apis.google.com/js/platform.js';
      fs.parentNode.insertBefore(js,fs);js.onload=function(){g.load('analytics');};
    }(window,document,'script'));
    </script>
    ```
5. Add HTML containers and dashboard code to host the dashboard components.

    ```javascript
    <div id="chart-1-container"></div>
    <script>

    gapi.analytics.ready(function() {

      /**
       * Authorize the user with an access token obtained server side.
       */
      gapi.analytics.auth.authorize({
        'serverAuth': {
          'access_token': 'ACCESS_TOKEN_FROM_SERVICE_ACCOUNT'
        }
      });


      /**
       * Creates a new DataChart instance showing sessions over the past 30 days.
       * It will be rendered inside an element with the id "chart-1-container".
       */
      var dataChart1 = new gapi.analytics.googleCharts.DataChart({
        query: {
          'ids': 'ga:100367422', // <-- Replace with the ids value for your view.
          'start-date': '30daysAgo',
          'end-date': 'yesterday',
          'metrics': 'ga:sessions,ga:users',
          'dimensions': 'ga:date'
        },
        chart: {
          'container': 'chart-1-container',
          'type': 'LINE',
          'options': {
            'width': '100%'
          }
        }
      });
      dataChart1.execute();
    });
    </script>
    ```

## References
1. [Google Analytics setup for Jekyll](https://michaelsoolee.com/google-analytics-jekyll/)
2. [Google Analytics,  Demos & Tools](https://ga-dev-tools.appspot.com/)
