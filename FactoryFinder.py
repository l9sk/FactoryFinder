import urllib2
import sys
import re





def search(html, words):

    try:
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        headers = {'User-Agent': user_agent}
        url = "http://" + str(html)
        req = urllib2.Request(url, None, headers)

        response = urllib2.urlopen(req)
        source = response.read()

        for word in words:
            expression = word
            match = re.search(expression, source)
            if (match != None):
                print ('\n' + html + " " + ( words[word]) )

    except Exception as e:
        sys.exc_clear()


def printProgress(searched, length):
    sys.stdout.write(str(searched) + " of " + str(length) + " IP adresses searched.")
    sys.stdout.write("\r")
    sys.stdout.flush()


def run():
    global addr


    print " "
    print " "
    print " "
    print "            _               _                                    "
    print "           |__. __|_ _ ._  |_o._  _| _ ._                        "
    print "           |(_|(_ |_(_)|\/ | || |(_|(/_|                         "
    print "                        /                v1.0 Community Edition  "
    print "                                                                 "
    print "                                                                 "
    print "                                   Berk Cem Goksel               "
    print " "
    print " "

    file = str(raw_input("Feed me your domain name list: "))
    iplist = list()
    a = open(file, "r")
    domains = a.read()
    print '\nHere is the list you provided: \n\n' + domains
    prompt = str(raw_input('\nDo you want to continue? (y/n): '))

    if prompt != 'y':
        sys.exit('Exiting...')

    myfile = open(file, 'r')
    data = myfile.read().split('\n')

    print(chr(27) + "[2J")
    print("Searching...")

    words = {'Apache Server Status' : '  |  Default Webpage Found  |  Apache Unknown Version',
            'Welcome to the Advanced Extranet Server, ADVX!' : '|  Default Webpage Found  | ADVX ',
           'Fedora Core Test Page' : ' |    Outdated Service Found!   |  Apache 2.0 on Fedora',
            'Apache HTTP Server on Fedora Core'  : ' |  Outdated Service Found! |  Apache 2.0 on Fedora',
            'xampp/index'  : ' |  Default Webpage Found  |  ',
            'Apache/2.0.* (Linux/SuSE)' : ' |  Outdated Service Found! | Apache2.0 on Linux SuSE' ,
            'Test Page for Apache' : '  |  Outdated Service Found!  | Apache Unknown Version',
             '404 Object Not Found' :  ' |  Outdated Service Found!  |  IIS5.0',
            'Microsoft-IIS/5.0 server at'  : ' |  Outdated Service Found!  |  IIS5.0' ,
             'index.of'  : ' |  Default Webpage Found  |  IIS Unknow Version',
            'alt="IIS7"'  : ' |  Default Webpage Found  | IIS7',
             'Welcome.png'  : ' |  Default Webpage Found  |  IIS Unknown Version',
             'The initial installation of Debian/GNU Apache' : ' |  Default Webpage Found  |  Apache Unknown Version'
             }


    for address in data:
        search(address, words)



# Ripped the following off
def query_yes_no(question, default="yes"):
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")




def start():
    try:
        run()
    except KeyboardInterrupt:
        sys.exit("Exiting...")


start()

