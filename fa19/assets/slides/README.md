Slides
------

This directory contains all lecture slides materials that will be posted on the website.

Publishing
----------

In order for slides to get published on the website, it must follow a strict naming convention:

`[lecture number]-[name of lecture][_1pp/_6pps].[pdf/ipynb]`

For example, if you want to post slides and notebooks for lecture #2 and 
the name of the lecture on the website is "Controls, Loops, Functions", then
your files should look like this:
* `02-Control,_Loops,_Functions.ipynb`
* `02-Control,_Loops,_Functions_1pp.pdf`
* `02-Control,_Loops,_Functions_6pps.pdf`

If the file name does not follow this convention and match the lecture name on the website
exactly (see `cs88/src/web/data/calendar.py`), then it will not get linked on the website.
