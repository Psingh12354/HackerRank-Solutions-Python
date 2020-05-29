import datetime
def date_time():
    return datetime.datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
def main():
    t=int(input())
    for i in range(t):
        t1=date_time()
        t2=date_time()
        print(int(abs(t1-t2).total_seconds()))
main()
