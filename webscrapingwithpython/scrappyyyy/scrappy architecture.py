'''
    scrappy architectuer :
     data flow : data flow is controlled by the execution engine .
     execution engine control all the data flow and take and process requests.

     engine gets request from the spider and it schedule requests and then ask for any other requests if it exists.

     spider extract the data from the websites.

     scheduler receives the requests from the engine and if there are multiple requests it schedules the requests for processing.

     middleware : these works in between engine and spider or engine and downloader to perform certain tasks.

     downloader : it is responsible to download the webpages and feeds them to engine which feed them to spiders.
     once the page is downloaded it generates the response and passes it along with any data that is generated.
     downloaded takes requests and passes response from the engine.

     the processed items are sent to items pipeline .

     this process is repeated until scheduler is empty or all the requests has been compeletedd.
'''