/*
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
*/

jQuery(document).ready(function($){
    $('#next_button').click(function() {
        $.ajax({
            url: '/next',
            type: 'GET',
            success: function (result) {
              var res = JSON.parse(result);
              $('#winner_name').html(res['name']);
              $('#feedback').text(res['feedback']);
            }
        });
    });
    $('#freshen_import').click(function() {
        $.ajax({
            url: '/freshen',
            type: 'GET',
            success: function (result) {
              $('#feedback').text(result);
            }
        });
    });
    $('#wipe_data').click(function() {
        $.ajax({
            url: '/wipe',
            type: 'GET',
            success: function (result) {
              $('#feedback').text(result);
            }
        });
    });
});

