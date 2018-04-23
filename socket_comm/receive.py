import socket
import threading

class ListenThread(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.kill = False
        self.prev_data = []

    def run(self):
        TCP_IP = '127.0.0.1'
        TCP_PORT = 5005
        BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((TCP_IP, TCP_PORT))
        while True:
            s.listen(1)

            conn, addr = s.accept()
            print 'Connection address:', addr
            while 1:
                data = conn.recv(BUFFER_SIZE)
                if not data: break
                print "received data:", data
                if self.prev_data != data:
                    conn.send(data)  # echo
                else: break
            conn.close()


if __name__ == "__main__":
    thread_1 = ListenThread(1)
    #thread_2 = Server(2)
    thread_1.start()
    #thread_2.start()
    thread_1.join()
    #thread_2.join()
    print ("Exiting Main Thread")

#
# import socket
# from threading import Thread, Lock
# import time
#
# class ListenThread(Thread):
#
#     def __init__(self, app, lock):
#         Thread.__init__(self)
#         self._app = app
#         self._lock = lock
#         self._terminating = False
#
#     def destroy(self):
#         self._terminating = True
#
#     def run(self):
#         s = socket.socket()
#         host = '127.0.0.1'
#         port = 5005
#         address = (host, port)
#
#         while True:
#
#             if self._terminating:
#                 break;
#
#             if s.recv(BUFFER_SIZE).decode() != "":
#                 self._lock.acquire()
#                 self._app.post_new_data(s.recv(1024))
#                 self._lock.release()
#             time.sleep(0.1)
#
