import logging
import telnetlib
import time


class TelnetClient():
    def __init__(self,):
        self.tn = telnetlib.Telnet()

    # 此函數實現telnet登錄主機
    def login_host(self,host_ip,username,password):
        try:
            # self.tn = telnetlib.Telnet(host_ip,port=23)
            self.tn.open(host_ip,port=23)
        except:
            logging.warning(‘%s網絡連接失敗‘%host_ip)
            return False
        # 等待login出現後輸入用戶名，最多等待10秒
        self.tn.read_until(b‘login: ‘,timeout=10)
        self.tn.write(username.encode(‘ascii‘) + b‘\n‘)
        # 等待Password出現後輸入用戶名，最多等待10秒
        self.tn.read_until(b‘Password: ‘,timeout=10)
        self.tn.write(password.encode(‘ascii‘) + b‘\n‘)
        # 延時兩秒再收取返回結果，給服務端足夠響應時間
        time.sleep(2)
        獲取登錄結果
        # read_very_eager()獲取到的是的是上次獲取之後本次獲取之前的所有輸出
        command_result = self.tn.read_very_eager().decode(‘ascii‘)
        if ‘Login incorrect‘ not in command_result:
            logging.warning(‘%s登錄成功‘%host_ip)
            return True
        else:
            logging.warning(‘%s登錄失敗，用戶名或密碼錯誤‘%host_ip)
            return False

    # 此函數實現執行傳過來的命令，並輸出其執行結果
    def execute_some_command(self,command):
        # 執行命令
        self.tn.write(command.encode(‘ascii‘)+b‘\n‘)
        time.sleep(2)
        # 獲取命令結果
        command_result = self.tn.read_very_eager().decode(‘ascii‘)
        logging.warning(‘命令執行結果：\n%s‘ % command_result)

    # 退出telnet
    def logout_host(self):
        self.tn.write(b"exit\n")

import threading
        
if __name__ == ‘__main__‘:
    host_ip = ‘192.168.220.129‘
    username = ‘root‘
    password = ‘abcd1234‘
    command = ‘whoami‘
    telnet_client = TelnetClient()
    # 如果登錄結果返加True，則執行命令，然後退出
    if telnet_client.login_host(host_ip,username,password):
        telnet_client.execute_some_command(command)
        telnet_client.logout_host()
    
    
    
    lock = threading.Lock()
    # 子執行緒的工作函數
    def job(num):
        lock.acquire()
        print("Thread", num)
        lock.release()

    # 建立 5 個子執行緒
    threads = []
    for i in range(5):
        threads.append(threading.Thread(target = job, args = (i,)))
        threads[i].start()

    # 主執行緒繼續執行自己的工作
    # ...

    # 等待所有子執行緒結束
    for i in range(5):
        threads[i].join()

    print("Done.")
