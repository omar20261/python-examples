#!/usr/bin/python
import urllib3

def main():
    MyUrl="https://www.google.com.eg/";
    http = urllib3.PoolManager()
    data= http.request('GET',MyUrl);
    print(data)

if __name__ == "__main__":main()
