<!--
pyPrize
Copyright (C) 2015 Catalyst IT Ltd

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
-->

<html>
    <head>
        <meta charset="UTF-8">
        <title>PyPrizes</title>
        <link rel="shortcut icon" href="static/images/favicon.ico">
        <link href="https://fonts.googleapis.com/css?family=Inconsolata:400,700|Open+Sans:400italic,700italic,400,700" rel="stylesheet" type="text/css">
        <link rel="stylesheet" href="static/css/main.css">
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.0.0-alpha1/jquery.min.js"></script>
        <script type="text/javascript" src="static/js/pyprize.js"></script>
    </head>
    <body>
        <div id='charcoal_bar'>Kiwi PyCon 2016
        </div>
        <div id='blue_bar'></div>
        <div id='white_bar'>
            <img src="http://static.nzpug.org/NZPUG_Horizontal_Full_Extended_600x61.png">
        </div> <!-- Plug the PUG ;-) -->
        <div id='main'>
            <button class='button' id="next_button">
                Next Winner&nbsp;&nbsp;&#x25BA;
            </button>
            <div id='winner_details'>
                <p id='winner_name'>&nbsp;&nbsp;</p>
            </div>
            <hr>
            <p id='feedback'></p>
            <button class='button'  id="freshen_import">Fresh Import</button>
            <button class='button'  id="wipe_data">Empty Database</button>
            <img id='catalyst_logo' src="http://catalyst.net.nz/sites/all/themes/sauce/images/catalyst-logo.svg">
        </div>
    </body>
</html>
