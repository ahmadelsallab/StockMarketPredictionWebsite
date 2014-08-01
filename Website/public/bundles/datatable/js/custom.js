/*
* stop the auto search function
* do it on enter only
*/
jQuery.fn.dataTableExt.oApi.fnSetFilteringPressEnter = function (oSettings) {
    var _that = this;
 
    this.each(function (i) {
        $.fn.dataTableExt.iApiIndex = i;
        var $this = this;
        var anControl = $('input', _that.fnSettings().aanFeatures.f);
        anControl.unbind('keyup').bind('keypress', function (e) {
            if (e.which == 13) {
                $.fn.dataTableExt.iApiIndex = i;
                _that.fnFilter(anControl.val());
            }
        });
        return this;
    });
    return this;
}
 
$(document).ready(function() {
    $('.dataTable').dataTable().fnSetFilteringPressEnter();
} );



/*
* create search/clear icons
* make search/clear functions
*/
if ( typeof $.fn.dataTable == "function" && typeof $.fn.dataTableExt.fnVersionCheck == "function" && $.fn.dataTableExt.fnVersionCheck('1.9.2')/*older versions should work too*/ )
{
    $.fn.dataTableExt.oApi.clearSearch = function ( oSettings )
    {
 
        var table = this;
         
        //no image file needed, css embedding must be supported by browser
        var clearSearch = $('<img title="Delete" alt="" src="data:image/png;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAD2SURBVHjaxFM7DoMwDH2pOESHHgDPcB223gKpAxK34EAMMIe1FCQOgFQxuflARVBSVepQS5Ht2PHn2RHMjF/ohB8p2gSZpprtyxEHX8dGTeMG0A5UlsD5rCSGvF55F4SpqpSm1GmCzPO3LXJy1LXllwvodoMsCpNVy2hbYBjCLRiaZ8u7Dng+QXlu9b4H7ncvBmKbwoYBWR4kaXv3YmAMyoEpjv2PdWUHcP1j1ECqFpyj777YA6Yss9KyuEeDaW0cCsCUJMDjYUE8kr5TNuOzC+JiMI5uz2rmJvNWvidwcJXXx8IAuwb6uMqrY2iVgzbx99/4EmAAarFu0IJle5oAAAAASUVORK5CYII=" style="vertical-align:text-bottom;cursor:pointer;margin-bottom:4px;position:relative;left: -37px;" />');

		var doSearch = $('<img title="Delete" alt="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAABx0RVh0U29mdHdhcmUAQWRvYmUgRmlyZXdvcmtzIENTM5jWRgMAAAAVdEVYdENyZWF0aW9uIFRpbWUAMi8xNy8wOCCcqlgAAAQRdEVYdFhNTDpjb20uYWRvYmUueG1wADw/eHBhY2tldCBiZWdpbj0iICAgIiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+Cjx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDQuMS1jMDM0IDQ2LjI3Mjk3NiwgU2F0IEphbiAyNyAyMDA3IDIyOjExOjQxICAgICAgICAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp4YXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iPgogICAgICAgICA8eGFwOkNyZWF0b3JUb29sPkFkb2JlIEZpcmV3b3JrcyBDUzM8L3hhcDpDcmVhdG9yVG9vbD4KICAgICAgICAgPHhhcDpDcmVhdGVEYXRlPjIwMDgtMDItMTdUMDI6MzY6NDVaPC94YXA6Q3JlYXRlRGF0ZT4KICAgICAgICAgPHhhcDpNb2RpZnlEYXRlPjIwMDgtMDMtMjRUMTk6MDA6NDJaPC94YXA6TW9kaWZ5RGF0ZT4KICAgICAgPC9yZGY6RGVzY3JpcHRpb24+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyI+CiAgICAgICAgIDxkYzpmb3JtYXQ+aW1hZ2UvcG5nPC9kYzpmb3JtYXQ+CiAgICAgIDwvcmRmOkRlc2NyaXB0aW9uPgogICA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDUdUmQAAAJXSURBVDiNpZNdSJNhFMd/77vN2drrKuc+0oVCYJqadBWmZRdCBBFhEHlj0l1CdCFRN16EBEVBN0GQ1JXaXWGgGJhdyCIzMD+JLvyYzjnnnHPfH+/TxWawBkV04PCc58D/x3nOnwf+M6TfG13Dc41Tnt1XP/yRclcwrgU47TCt11mNj55drHv6R8CVgcmxseXt5paKQ3TUH+Z4iRF3KM6bBS/Pv65SXWJcP1d+8FRPS9VK3ihXBibHjjz5IJxLmyIWi+Wle3tXNLxwiqZepztP3DU816j0jIiJFd8vQTgaE/5wVPjDURGOZnrf1vziwIP3ovPd9O09rQwwvRF6ef6omTqLEYBIWuBNqKxn05tQiaQFlcUGWqssTHlCd3IA37fCFW01NgDSAnZSAl9SxRNX2Yir+JIqOylBWsDVaitOV8C+B9ACrAbj2pN2BYC4KoiogmBKsJlQs2uW2a8RxFWB2VCQ83x5r9iKJPPtkTKnlPVKksC5GqCsqDCVA2hwmNx9Mx4A9LKEQZZQtBIWnYylQEbRZHpaoG/GwzGzYTEHUG9THvbPevCGE2gkMGklzDoZm17GWiBj1smYdBKji34m1oKcsCrXcyYFaOp1un2RpP11ay2VxQbSIrMPScosanTRz43BeUqL9AvTnWeq8wD3RuYd467A51lvyN5Wa+NajY19Wg1OV4D+WQ9f3EFKFb1reSfmAN4CHdy/EMj7CzcHp2/NeEN3x1cyVpUVFaYqiw1L9Tal/fGn5TlgCigHloDLeYC/RvfQWeBj9tb8z/ospJ3uoUsAPwFpwBY3vgOzSAAAAABJRU5ErkJggg==" style="vertical-align:text-bottom;cursor:pointer;margin-bottom:4px;position:relative;left: -42px;" />');
		        

        $(doSearch).click( function ()
        {
	        var anControl = $('input', table.fnSettings().aanFeatures.f);
            table.fnFilter(anControl.val());

        });

        $(clearSearch).click( function ()
        {
              table.fnFilter('');
        });

        $(oSettings.nTableWrapper).find('div.dataTables_filter label').append(doSearch);
        $(oSettings.nTableWrapper).find('div.dataTables_filter label').append(clearSearch);
        $(oSettings.nTableWrapper).find('div.dataTables_filter label').css('margin-right', '-16px');//16px the image width
        $(oSettings.nTableWrapper).find('div.dataTables_filter input').css('padding-right', '16px');
    }
 
    //auto-execute, no code needs to be added
    $.fn.dataTable.models.oSettings['aoInitComplete'].push( {
        "fn": $.fn.dataTableExt.oApi.clearSearch,
        "sName": 'whatever'
    } );
}
