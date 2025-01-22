##Youtube Video download with python 
import webbrowser
url="https://www.youtube.com/watch?v=0dgYA8j9AbE&list=RD0dgYA8j9AbE&start_radio=1" #video URL here
download = url[:12]="SS"+url[12:]
webbrowser.open(download)
