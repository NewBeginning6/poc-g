import argparse
import requests
from termcolor import cprint
import colorama
colorama.init(autoreset=True)
from tkinter import *
from tkinter import messagebox

args = {}

def M_Get(args):
    url = 'args.url'
    if args['status']  and not args['response'] :
        with open(args['output'], 'w', encoding='utf-8') as f:
            f.write(f"""import requests
import argparse
import urllib3
from termcolor import cprint
import colorama
colorama.init(autoreset=True)

def vul(args):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    vulurl = {url}+'{args['path'] }'
    response = requests.{args['method'].lower()}(vulurl, verify=False)
    if response.status_code == {args['status'] }:
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
    elif args['response']  and not args['status'] :
        with open(args['output'], 'w', encoding='utf-8') as f:
            f.write(f"""import requests
import argparse
import urllib3
from termcolor import cprint
import colorama
colorama.init(autoreset=True)

def vul(args):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    vulurl = {url}+'{args['path'] }'
    response = requests.{args['method'].lower()}(vulurl, verify=False)
    if '{args['response'] }' in response.text :
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
    elif args['status']  and args['response'] :
        with open(args['output'], 'w', encoding='utf-8') as f:
            f.write(f"""import requests
import argparse
import urllib3
from termcolor import cprint
import colorama
colorama.init(autoreset=True)

def vul(args):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    vulurl = {url}+'{args['path'] }'
    response = requests.{args['method'].lower()}(vulurl, verify=False)
    if response.status_code == {args['status'] } and '{args['response'] }' in response.text :
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
    headers = {'Content-Type': args['ctype'] }
    if args['status']  and not args['response'] :
        with open(args['output'], 'w', encoding='utf-8') as f:
            f.write(f"""import requests
import argparse
import urllib3
from termcolor import cprint
import colorama
colorama.init(autoreset=True)

def vul(args):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    vulurl = {url}+'{args['path'] }'
    response = requests.{args['method'].lower()}(vulurl, data='{args['data'] }', headers={headers}, verify=False)
    if response.status_code == {args['status'] }:
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
    elif args['response']  and not args['status'] :
        with open(args['output'], 'w', encoding='utf-8') as f:
            f.write(f"""import requests
import argparse
import urllib3
from termcolor import cprint
import colorama
colorama.init(autoreset=True)

def vul(args):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    vulurl = {url}+'{args['path'] }'
    response = requests.{args['method'].lower()}(vulurl, data='{args['data'] }', headers={headers}, verify=False)
    if '{args['response'] }' in response.text :
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
    elif args['status']  and args['response'] :
        with open(args['output'], 'w', encoding='utf-8') as f:
            f.write(f"""import requests
import argparse
import urllib3
from termcolor import cprint
import colorama
colorama.init(autoreset=True)

def vul(args):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    vulurl = {url}+'{args['path'] }'
    response = requests.{args['method'].lower()}(vulurl, data='{args['data'] }', headers={headers}, verify=False)
    if response.status_code == {args['status'] } and '{args['response'] }' in response.text :
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
    if args['status']  and not args['response'] :
        with open(args['output'], 'w', encoding='utf-8') as f:
            f.write(f"""import requests
import argparse
import urllib3
from termcolor import cprint
import colorama
colorama.init(autoreset=True)

def vul(args):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    vulurl = {url}+'{args['path'] }'
    response = requests.{args['method'].lower()}(vulurl, files={{'file':('{args['file'] }','{args['data'] }')}}, verify=False)
    if response.status_code == {args['status'] }:
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
    elif args['response']  and not args['status'] :
        with open(args['output'], 'w', encoding='utf-8') as f:
            f.write(f"""import requests
import argparse
import urllib3
from termcolor import cprint
import colorama
colorama.init(autoreset=True)

def vul(args):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    vulurl = {url}+'{args['path'] }'
    response = requests.{args['method'].lower()}(vulurl, files={{'file':('{args['file'] }','{args['data'] }')}}, verify=False)
    if '{args['response'] }' in response.text :
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
    elif args['status']  and args['response'] :
        with open(args['output'], 'w', encoding='utf-8') as f:
            f.write(f"""import requests
import argparse
import urllib3
from termcolor import cprint
import colorama
colorama.init(autoreset=True)

def vul(args):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    vulurl = {url}+'{args['path'] }'
    response = requests.{args['method'].lower()}(vulurl, files={{'file':('{args['file'] }','{args['data'] }')}}, verify=False)
    if response.status_code == {args['status'] } and '{args['response'] }' in response.text :
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



def P_UI():
    root = Tk()
    root.geometry("690x520")
    
    method_label = Label(root, text="method", font=("Arial", 14))
    method_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    method_options = ["get", "post", "put"]
    method_var = StringVar(root)
    method_var.set(method_options[0])
    method_dropdown = OptionMenu(root, method_var, *method_options)
    method_dropdown.config(width=10, font=("Arial", 14))
    method_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky=W)
    args['method'] = method_var
    
    path_label = Label(root, text="path", font=("Arial", 14))
    path_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
    path_entry = Entry(root, width=50, font=("Arial", 14))
    path_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)
    args['path'] = path_entry
    
    data_label = Label(root, text="data", font=("Arial", 14))
    data_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
    data_entry = Text(root, width=50, height=2, font=("Arial", 14))
    data_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)
    args['data'] = data_entry
    
    ctype_label = Label(root, text="Content-Type", font=("Arial", 14))
    ctype_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
    ctype_options = ["application/x-www-form-urlencoded", "application/json"]
    ctype_var = StringVar(root)
    ctype_var.set(ctype_options[0])
    ctype_dropdown = OptionMenu(root, ctype_var, *ctype_options)
    ctype_dropdown.config(width=30, font=("Arial", 14))
    ctype_dropdown.grid(row=3, column=1, padx=10, pady=10, sticky=W)
    args['ctype'] = ctype_var
    
    file_label = Label(root, text="filename", font=("Arial", 14))
    file_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)
    file_entry = Entry(root, width=50, font=("Arial", 14))
    file_entry.grid(row=4, column=1, padx=10, pady=10, sticky=W)
    args['file'] = file_entry
    
    status_label = Label(root, text="status", font=("Arial", 14))
    status_label.grid(row=5, column=0, padx=10, pady=10, sticky=W)
    status_entry = Entry(root, width=50, font=("Arial", 14))
    status_entry.grid(row=5, column=1, padx=10, pady=10, sticky=W)
    args['status'] = status_entry
    
    response_label = Label(root, text="response", font=("Arial", 14))
    response_label.grid(row=6, column=0, padx=10, pady=10, sticky=W)
    response_entry = Text(root, width=50, height=2, font=("Arial", 14))
    response_entry.grid(row=6, column=1, padx=10, pady=10, sticky=W)
    args['response'] = response_entry
    
    output_label = Label(root, text="output", font=("Arial", 14))
    output_label.grid(row=7, column=0, padx=10, pady=10, sticky=W)
    output_entry = Entry(root, width=50, font=("Arial", 14))
    output_entry.grid(row=7, column=1, padx=10, pady=10, sticky=W)
    args['output'] = output_entry
    generate_button = Button(root, text="生成", command=lambda: [check(method_var.get(), path_entry.get(), data_entry.get("1.0", END).strip(), ctype_var.get(), file_entry.get(), status_entry.get(), response_entry.get("1.0", END).strip(), output_entry.get()), messagebox.showinfo("提示", "生成成功")], font=("Arial", 14))
    generate_button.grid(row=8, column=0, padx=10, pady=10, sticky="WE", columnspan=2)
    
    root.title("poc-g")
    root.mainloop()

def check(method, path, data, ctype, file, status, response, output):
    args['method'] = method 
    args['path'] = path 
    args['data'] = data 
    args['ctype'] = ctype 
    args['file'] = file 
    args['status'] = status 
    args['response'] = response 
    args['output'] = output 
    print(args['method'])
    if args['method'] == 'get':
        M_Get(args)
        print(args['output']+'生成成功')
    elif (args['method'] == 'post' or args['method'] == 'put') and not args['file'] :
        M_Post(args)
        print(args['output']+'生成成功')
    elif (args['method'] == 'post' or args['method'] == 'put') and args['file'] :
        M_UploadFile(args)
        print(args['output']+'生成成功')


if __name__ == '__main__':
    P_UI()
