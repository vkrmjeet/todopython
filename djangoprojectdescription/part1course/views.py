'''
     views is a python function that takes requests and returns a response.
         the return response can be a html document or a redirect it can also
         be a xml document, an image or anything that can be displayed by a browser.

         url patters comes in it looks for releavant view to display that then
         view looks for releavant models which then looks for templates to process that.

         example of a simple view :
             from django.http import HttpResponse
             import datetime

             def current_datetime(request)
                 now = datetime.datetime.now()
                 html = "<html><body>The time is now %s. </body></html>" %now
                 return HttpResponse(html)
            the above function will display the time and date of the instant at
            which the program is ran.
            the default django timezone is america , chicago.

'''