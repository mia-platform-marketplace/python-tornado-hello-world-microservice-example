"""
 * Copyright 2020 Mia srl
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
"""

import tornado.ioloop
import tornado.web
from tornado import gen
import requests
from functools import lru_cache
import logging
import os
import psutil
import json


@lru_cache(maxsize=None)
def calc_fib(n):
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return calc_fib(n - 1) + calc_fib(n - 2)


class HelloHandler(tornado.web.RequestHandler):
  def get(self):
    hello = {'message': "Hello World"}
    self.finish(json.dumps(hello))

class Fibonacci(tornado.web.RequestHandler):
  def get(self, num):
    logging.info('Memory before: ' +
                  str(process.memory_info().rss/1000000))
    start_num = int(num.strip())
    logging.info('Calculating fibonacci for n=%d', start_num)
    res = str(calc_fib(start_num))
    logging.info('Result is %s', res)
    logging.info('Memory after: ' + str(process.memory_info().rss/1000000))
    self.finish(res)


class Cars(tornado.web.RequestHandler):
  def get(self):
    logging.info('Request stress')
    r = requests.get('http://crud-service/cars/', '')
    logging.info('Result is %s', r.text)
    self.finish(json.dumps(r.json()))


class ReadyResource(tornado.web.RequestHandler):
  def get(self):
    ready = {'statusOK': True}
    self.finish(json.dumps(ready))

class HealthResource(tornado.web.RequestHandler):
  def get(self,):
    health = {'statusOK': True}
    self.finish(json.dumps(health))

def make_app():
  return tornado.web.Application([
    (r"/hello", HelloHandler),
    (r"/-/ready", ReadyResource),
    (r"/-/healthz", HealthResource),
    (r"/fib/([^/]+)?", Fibonacci),
    (r"/crud/cars", Cars),
  ])


if __name__ == "__main__":
  logging.basicConfig(level=logging.INFO)
  process = psutil.Process(os.getpid())
  app = make_app()
  server = tornado.httpserver.HTTPServer(app)
  server.bind(3000)
  server.start(0)
  logging.info('Python Tornado Server is up and running!!!')
  tornado.ioloop.IOLoop.current().start()
