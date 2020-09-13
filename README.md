# DIP_REAL_TIME_CROWD_DENSITY_MONITOR
Design &amp; Innovative Project

## How to run server:
1. open terminal, run following command:
<pre><code>ssh user@128.199.208.181</code></pre>
2. enter the password, then you will be directed to the home directory.
3. run the following command to run server:
<pre><code>bash run.sh</code></pre>
if there is no error, the output should be:
<pre><code>Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
August 26, 2020 - 08:19:47
Django version 3.1, using settings 'dip.settings'
Starting development server at http://0:8000/
Quit the server with CONTROL-C.
</code></pre>
4. open this url in browser:
<pre><code>http://128.199.208.181:8000/</code></pre>
or
<pre><code>http://dipwinner.sg:8000/</code></pre>

## Resources:
1. Backend framework: Django
https://docs.djangoproject.com/en/3.1/
2. Frontend framework: Bootstrap
https://getbootstrap.com/docs/4.5/getting-started/introduction/

## TODO:
1. 404 notfound page
2. reorganize the codes in templates/interface/*.html, use {% extends './something.html' %}
3. database setup
4. make .shp map
5. raspberry pi client set up (usage: capture frame and send to server)
6. server opencv model set up (usage: receive frame from raspberry pi, recognize people and send data to API)
7. API (usage: receive request from opencv part and update the bokeh map)