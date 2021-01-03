from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from collections import deque
db = SQLAlchemy()
from twilio import account_sid, auth_token, client


class Queue:

    def __init__(self):
        self._queue = []
        self._mode = 'FIFO'
        self.account = account_sid
        self.token = auth_token
        self.client = client
        

    def enqueue(self, item):
        self._queue.append(items)
        message = client.messages.create(
                body= str(item['name'])item + ' tu hora de comer se acerca, aun tiene ' + len(self._queue)-1 +' personas delante',
                from_='+12025194871',
                to='+56994433896'
            )

        return message.sid
       
        

    def dequeue(self):
        
        if self.size() > 0:
            if self.mode == 'FIFO':
                item = self._queue.pop()
                return item
            elif self._mode == 'LIFO':
                item = self._queue.pop(-1)
                return item
        else:
            msg = {
                "msg": "NO hay elementos en fila"
            }
            return msg
            
       

    def get_queue(self):
        return self._queue

    def size(self):
        return len(self._queue)