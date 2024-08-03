import socket
import threading

host = socket.gethostbyname(socket.gethostname())

def portscanner(host,port,results):
    s_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        result = s_socket.connect_ex((host,port))
        if result == 0:
            results[port]=0
        else:
            results[port]=1
    except Exception as e:
        print(f"port {port} encountered an error\n")
    finally:
        s_socket.close()

def main():
    global host
    x = int(input("enter till what port you want to scan:"))
    result = [None]*(x+1)
    threads = []

    for port in range(1,x+1):
        thread_ps = threading.Thread(target=portscanner,args=(host,port,result))
        threads.append(thread_ps)
        thread_ps.start()
    
    for i in threads:
        i.join()
    
    for port in range(1,x+1):
        if result[port] == 0:
            print(f"port {port} is open\n")
        else:
            print(f"port {port} is closed\n")
                    
main()

