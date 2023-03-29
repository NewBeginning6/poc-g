import argparse
import requests
from termcolor import cprint


def M_Get(args):
    url = 'args.url'
    if args.status and not args.response:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(f"""import requests
import argparse
import urllib3
from termcolor import cprint

def vul(args):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    vulurl = {url}+'{args.path}'
    response = requests.{args.method.lower()}(vulurl, verify=False)
    if response.status_code == {args.status}:
        cprint('[+]' +vulurl + ': Vulnerability exists', 'red')
    else:
        cprint('[-]' +vulurl + ': Vulnerability does not exist')
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Python code for HTTP requests')
    parser.add_argument('-u', '--url', type=str, help='HTTP url', default=None, required=False)
    parser.add_argument('-r', '--urls', type=str, help='HTTP urls', default=None, required=False)
    args = parser.parse_args()
    if args.url and not args.urls:
        vul(args)
    if args.urls and not args.url:
        for line in open(args.urls):
            url = line.strip()
            args.url = url
            vul(args)
""")
    elif args.response and not args.status:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(f"""import requests
import argparse
import urllib3
from termcolor import cprint

def vul(args):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    vulurl = {url}+'{args.path}'
    response = requests.{args.method.lower()}(vulurl, verify=False)
    if '{args.response}' in response.text :
        cprint('[+]' +vulurl + ': Vulnerability exists', 'red')
    else:
        cprint('[-]' +vulurl + ': Vulnerability does not exist')
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Python code for HTTP requests')
    parser.add_argument('-u', '--url', type=str, help='HTTP url', default=None, required=False)
    parser.add_argument('-r', '--urls', type=str, help='HTTP urls', default=None, required=False)
    args = parser.parse_args()
    if args.url and not args.urls:
        vul(args)
    if args.urls and not args.url:
        for line in open(args.urls):
            url = line.strip()
            args.url = url
            vul(args)
""")
    elif args.status and args.response:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(f"""import requests
import argparse
import urllib3
from termcolor import cprint

def vul(args):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    vulurl = {url}+'{args.path}'
    response = requests.{args.method.lower()}(vulurl, verify=False)
    if response.status_code == {args.status} and '{args.response}' in response.text :
        cprint('[+]' +vulurl + ': Vulnerability exists', 'red')
    else:
        cprint('[-]' +vulurl + ': Vulnerability does not exist')
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Python code for HTTP requests')
    parser.add_argument('-u', '--url', type=str, help='HTTP url', default=None, required=False)
    parser.add_argument('-r', '--urls', type=str, help='HTTP urls', default=None, required=False)
    args = parser.parse_args()
    if args.url and not args.urls:
        vul(args)
    if args.urls and not args.url:
        for line in open(args.urls):
            url = line.strip()
            args.url = url
            vul(args)
""")


def M_Post(args):
    url = 'args.url'
    headers = {'Content-Type': args.ctype}
    if args.status and not args.response:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(f"""import requests
import argparse
import urllib3
from termcolor import cprint

def vul(args):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    vulurl = {url}+'{args.path}'
    response = requests.{args.method.lower()}(vulurl, data='{args.data}', headers={headers}, verify=False)
    if response.status_code == {args.status}:
        cprint('[+]' +vulurl + ': Vulnerability exists', 'red')
    else:
        cprint('[-]' +vulurl + ': Vulnerability does not exist')
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Python code for HTTP requests')
    parser.add_argument('-u', '--url', type=str, help='HTTP url', default=None, required=False)
    parser.add_argument('-r', '--urls', type=str, help='HTTP urls', default=None, required=False)
    args = parser.parse_args()
    if args.url and not args.urls:
        vul(args)
    if args.urls and not args.url:
        for line in open(args.urls):
            url = line.strip()
            args.url = url
            vul(args)
""")
    elif args.response and not args.status:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(f"""import requests
import argparse
import urllib3
from termcolor import cprint

def vul(args):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    vulurl = {url}+'{args.path}'
    response = requests.{args.method.lower()}(vulurl, data='{args.data}', headers={headers}, verify=False)
    if '{args.response}' in response.text :
        cprint('[+]' +vulurl + ': Vulnerability exists', 'red')
    else:
        cprint('[-]' +vulurl + ': Vulnerability does not exist')
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Python code for HTTP requests')
    parser.add_argument('-u', '--url', type=str, help='HTTP url', default=None, required=False)
    parser.add_argument('-r', '--urls', type=str, help='HTTP urls', default=None, required=False)
    args = parser.parse_args()
    if args.url and not args.urls:
        vul(args)
    if args.urls and not args.url:
        for line in open(args.urls):
            url = line.strip()
            args.url = url
            vul(args)
""")
    elif args.status and args.response:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(f"""import requests
import argparse
import urllib3
from termcolor import cprint

def vul(args):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    vulurl = {url}+'{args.path}'
    response = requests.{args.method.lower()}(vulurl, data='{args.data}', headers={headers}, verify=False)
    if response.status_code == {args.status} and '{args.response}' in response.text :
        cprint('[+]' +vulurl + ': Vulnerability exists', 'red')
    else:
        cprint('[-]' +vulurl + ': Vulnerability does not exist')
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Python code for HTTP requests')
    parser.add_argument('-u', '--url', type=str, help='HTTP url', default=None, required=False)
    parser.add_argument('-r', '--urls', type=str, help='HTTP urls', default=None, required=False)
    args = parser.parse_args()
    if args.url and not args.urls:
        vul(args)
    if args.urls and not args.url:
        for line in open(args.urls):
            url = line.strip()
            args.url = url
            vul(args)
""")


def M_UploadFile(args):
    url = 'args.url'
    if args.status and not args.response:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(f"""import requests
import argparse
import urllib3
from termcolor import cprint

def vul(args):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    vulurl = {url}+'{args.path}'
    response = requests.{args.method.lower()}(vulurl, files={{'file':('{args.file}','{args.data}')}}, verify=False)
    if response.status_code == {args.status}:
        cprint('[+]' +vulurl + ': Vulnerability exists', 'red')
    else:
        cprint('[-]' +vulurl + ': Vulnerability does not exist')
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Python code for HTTP requests')
    parser.add_argument('-u', '--url', type=str, help='HTTP url', default=None, required=False)
    parser.add_argument('-r', '--urls', type=str, help='HTTP urls', default=None, required=False)
    args = parser.parse_args()
    if args.url and not args.urls:
        vul(args)
    if args.urls and not args.url:
        for line in open(args.urls):
            url = line.strip()
            args.url = url
            vul(args)
""")
    elif args.response and not args.status:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(f"""import requests
import argparse
import urllib3
from termcolor import cprint

def vul(args):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    vulurl = {url}+'{args.path}'
    response = requests.{args.method.lower()}(vulurl, files={{'file':('{args.file}','{args.data}')}}, verify=False)
    if '{args.response}' in response.text :
        cprint('[+]' +vulurl + ': Vulnerability exists', 'red')
    else:
        cprint('[-]' +vulurl + ': Vulnerability does not exist')
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Python code for HTTP requests')
    parser.add_argument('-u', '--url', type=str, help='HTTP url', default=None, required=False)
    parser.add_argument('-r', '--urls', type=str, help='HTTP urls', default=None, required=False)
    args = parser.parse_args()
    if args.url and not args.urls:
        vul(args)
    if args.urls and not args.url:
        for line in open(args.urls):
            url = line.strip()
            args.url = url
            vul(args)
""")
    elif args.status and args.response:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(f"""import requests
import argparse
import urllib3
from termcolor import cprint

def vul(args):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    vulurl = {url}+'{args.path}'
    response = requests.{args.method.lower()}(vulurl, files={{'file':('{args.file}','{args.data}')}}, verify=False)
    if response.status_code == {args.status} and '{args.response}' in response.text :
        cprint('[+]' +vulurl + ': Vulnerability exists', 'red')
    else:
        cprint('[-]' +vulurl + ': Vulnerability does not exist')
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Python code for HTTP requests')
    parser.add_argument('-u', '--url', type=str, help='HTTP url', default=None, required=False)
    parser.add_argument('-r', '--urls', type=str, help='HTTP urls', default=None, required=False)
    args = parser.parse_args()
    if args.url and not args.urls:
        vul(args)
    if args.urls and not args.url:
        for line in open(args.urls):
            url = line.strip()
            args.url = url
            vul(args)
""")


if __name__ == '__main__':
    cprint(f"""                             
______   ____   ____             ____  
\____ \ /  _ \_/ ___\   ______  / ___\ 
|  |_> >  <_> )  \___  /_____/ / /_/  >
|   __/ \____/ \___  >         \___  / 
|__|               \/         /_____/  
""", "yellow")
    parser = argparse.ArgumentParser(description='Generate Python code for HTTP requests')
    parser.add_argument('-m', '--method', type=str, help='HTTP method (get, post, put)', default='', required=False)
    parser.add_argument('-p', '--path', type=str, help='HTTP url path ', default='', required=False)
    parser.add_argument('-d', '--data', type=str, help='HTTP request post data ', default='', required=False)
    parser.add_argument('-c', '--ctype', type=str, help='HTTP request post Content-Type', default='application/x-www-form-urlencoded', required=False)
    parser.add_argument('-f', '--file', type=str, help='HTTP request post upload filename', default=None, required=False)
    parser.add_argument('-s', '--status', type=int, help='HTTP status code', default=None, required=False)
    parser.add_argument('-r', '--response', type=str, help='HTTP response body', default=None, required=False)
    parser.add_argument('-o', '--output', type=str, help='Output Python file', required=False)
    args = parser.parse_args()
    if args.method == 'get':
        M_Get(args)
        print(args.output+'生成成功')
    elif (args.method == 'post' or args.method == 'put') and not args.file:
        M_Post(args)
        print(args.output+'生成成功')
    elif (args.method == 'post' or args.method == 'put') and args.file:
        M_UploadFile(args)
        print(args.output+'生成成功')
