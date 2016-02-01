
<h1>Icecast Ratings System</h1>

<h2>This is meant to be a dynamic ratings system developed for KRMA Internet Radio.  </h2>

Written in Python, HTML, and CSS. My goal was to make this a simple an reusable system for people using Icecast2 to stream their feed. 

usage: <i>python main.py access.log </i>

<i>or </i>

<i>tail -n access.log | python main.py </i>(to produce a continuous / live-ish feed post log generation.) 

<i>or </i>

For a slightly less IOPS intensive solution, create a cron job to process the logs hourly.

<h3>Functionality:</h3>

<b>Admin.html is an interface for users to define shows and time slots. </b>
Pulls information form MySQL database and populate fields in CGI page.

<b>Shows.html hasn't been created yet</b> 
It will present a layout very similar to Admin.html, but instead include relevant show data 

such as:<ul>
<li>Current listeners</li>
<li>Today's listeners</li>
<li>Week's listeners</li>
<li>Month's listeners</li>
<li>Year's listners</li>
<li>All time listeners</li>
</ul>






