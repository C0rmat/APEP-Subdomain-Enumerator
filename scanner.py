#!/usr/bin/env python3


import dns.resolver
import argparse
import threading
from queue import Queue
def get_argument(): #Argument Parser let the user chose and see their options
        parser = argparse.ArgumentParser(description='Subdomain Enumerator')
        parser.add_argument("--domain", help="enter a domain e.g. example.com")
        parser.add_argument("--wordlist", help="add a wordlist e.g. path to wordlist file")
        parser.add_argument("--threads", help="not required default of 10", type = int, default = 10)
        parser.add_argument("--output", help="not required, save the output to a file default = results.txt", default = "results.txt")
        return parser.parse_args()

def load_wordlist(path): #Load,read and cleanse the given wordlist
        with open(path) as file:
                words = [line.strip() for line in file.readlines() if line.strip() != ""]
        return words
                 
def check_subdomain(subdomain, output): #look for subdomains except dns.resolver.NXDOMAIN, dns.resolver.NoAnswer and give a feedback after succesful DNS search
        try:
                dns.resolver.resolve(subdomain, "A")
                print("Found ",subdomain)
                open(output, "a").write(subdomain + "\n")
                
        except(dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
                pass
      
def worker(domain, queue, output): 
        while not queue.empty():
                word = queue.get()
                subdomain = word + "." + domain
                check_subdomain(subdomain, output)
                queue.task_done()
                        
def main():
        print("""    ____      ____      ____      ____      ____      ____        
    ---/    \----/    \----/    \----/    \----/    \----/    \---    
      ( SSSS )  ( UUUU )  ( BBBB )  ( SSSS )  ( CCCC )  ( AAAA )   
    ---\____/----\____/----\____/----\____/----\____/----\____/---    
                                                                      
        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~          
       /;;\    APEP - Subdomain Enumerator v1.0     /;;\             
      / ;; \~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / ;; \            
     | (@@) |        [ by C0rmat ]            | (@@) |           
      \ ;; /~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\ ;; /           
       \;;/                                           \;;/            
        ~~                                             ~~             
        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~   """)
        
        args = get_argument()
        words = load_wordlist(args.wordlist)
        q = Queue()
        for word in words:
                q.put(word)
        threads = []

        for i in range(args.threads):
                t = threading.Thread(target=worker, args=(args.domain, q, args.output))
                t.start()
                threads.append(t)
        for i in threads:
                i.join()                


                
if __name__ == "__main__":
        main()
      





                
                               
               
      
            
           

               




