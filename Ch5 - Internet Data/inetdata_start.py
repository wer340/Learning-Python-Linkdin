# 
# Example file for retrieving data from the internet
# LinkedIn Learning Python course by Joe Marini
#

import urllib.request


def main():
      # this is a placeholder, do-nothing statement
    webUrl=urllib.request.urlopen("http://entekhab.ir")
    print(webUrl.getcode())
    data=webUrl.read()
    print(data)
if __name__ == "__main__":
    main()
