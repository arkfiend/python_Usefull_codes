#Libraries
import requests #To request Url and other options to use Html
import urllib.request as req #To download some stuffs
import os #To see if some directory exists
import sys #Used in this code, only to stop the script in errors
import argparse #Used to explore arguments

#Receives a list with all Url source, from an Url
# Returns a list with all formats required as ssecond param
def gettingLink(All, format):
    #List with all links
    links = []
    #Loading all letters from Url 
    for i in range(0, len(All)-1):
        if All[i]==chr(34) and All[i+1]=='h':
            #Getting all links in page
            pos = i+1
            tmp = ''
            while All[pos] != chr(34):
                tmp = tmp + All[pos]
                pos +=1
            #cutting different formats.
            if tmp[-3:]== format:
                links.append(tmp)
    return links
        

#Receives a list of strings, where each element is a string that corresponds to un Url of one item. All of them have the same format.
#Also receives a Directory name, with full directory location. (It was onlly tested at Windows. Please, understand that linux has different ways to treat directories)
#Dont returns nothing. Just download all itens and save in that direcoty.
def downloadItens(list, dir):
    #Error
    if not os.path.exists(dir):
        print("\n\nError: - this path doesnt exist. Please make sure you have permission to download in that directory, as is an existing item.")
        sys.exit()
    #Batch with all itens
    for i in range(0, len(list)):
        end = dir +"\\"+ str(i) +""+list[0][-4:]
        #Item
        item = list[i]
        #Printing
        p = round((i+1)/len(list)*100,1)
        out = "Downloading the item "+str(i)+" de "+ str(len(list)-1)+"("+str(p)+"%)   ---"+end
        print(out)
        #Downloading
        req.urlretrieve(item, end)



#Main function
if __name__ == '__main__':
    #Geting args
    parser = argparse.ArgumentParser(description='Download a batch of files from an URL, to a directory') #help
    parser.add_argument('-d','--dir', help='full path', required=True)#dir - for directory
    parser.add_argument('-u','--url', help='Url Link', required=True)#url - To the entire url to search
    parser.add_argument('-f','--format', help='Format of itens', required=True)#format - to format that you need to pick
    args = parser.parse_args() #Creates an Object of itens, that each one has a parameter "argument"

    #Defining the URL
    url = str(args.url)
    #All Url Source
    urlSource = str(requests.get(url).content)
    #Getting all content and saving in a list
    links = gettingLink(urlSource, str(args.format))
    print("[2] - Got a list of",args.format,", with",len(links), "itens")
    #print (links)
    print("[3] - Downloading itens and putting them in directory:")
    downloadItens(links, str(args.dir))
    


#python url.py -d "c:\exit" -u "https://github.com/Microsoft/vscode-python/issues/2732" -f "png"