#getSPLctrs

This program will download all of 3239 SP lectures/conversations (44GB in total) from causelessmercy.com. This program took me around 5-6 hrs to download all the lectures on a 50Mbps connection. So, if you face some problem while the program is running do not hesitate to run it again. This program is idempotent which means even if you run it multiple times (provided you are running from the same folder location) it will not download the lectures again. If some lecture is already downloaded it will not download it again.

When you stop and run the program again there is a chance that some lecture might be partially downloaded. In that case this program will check all the lectures once again if the size is same as that in the website. In that case it will download those lectures again and delete the paritally downloaded copy.

I created this GitHub organization to have a common repository for codes in service for Srila Prabhupad. If you have any suggestions, comments or if someone wishes to be part of it then please msg me on facebook https://www.facebook.com/shashwath.kumar.77.

##How to run

- Install Python 2.7 (anaconda2 package recommended)
- Install git
- In the terminal go to the directory where you want to download the lectures
- git clone https://github.com/hkmCodes/Scrapers.git
- If you do not wish to install git you can download the zipped code from above link
- Enter the folder Scrapers
- Run the command 'python getSPLctrs.py'
- The lectures will be downloaded into the Scrapers folder
