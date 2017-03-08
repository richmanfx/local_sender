# coding: utf8
import enaml
import requests
from enaml.qt.qt_application import QtApplication
import json
import random

from requests import ConnectionError

grabber_url = 'http://localhost:7777'


if __name__ == '__main__':
    with enaml.imports():
        from local_view import Main

    app = QtApplication()
    view = Main(message="Локальный посылатель")
    view.show()

    app.start()


def ping_to_grabber():
    print 'Run: ping_to_grabber() - GET to localhost:7777.'
    try:
        requests.get(grabber_url)
    except ConnectionError:
        print 'Connection Error. Grabber is running?'


def many_ping_to_grabber():
    print 'Run: many_ping_to_grabber() - many GET to localhost:7777.'
    i = 50     # Количество запросов
    j = 0
    try:
        while j < i:
            requests.get(grabber_url)
            j += 1
    except ConnectionError:
        print 'Connection Error. Grabber is running?'


def exit_to_grabber():
    print 'Run: exit_to_grabber() - DELETE to Grabber.'
    try:
        requests.delete(grabber_url)
    except ConnectionError:
        print 'Connection Error. Grabber is running?'


def grab_to_grabber():
    print 'Run: grab_to_grabber() - POST to Grabber.'
    request_headers = {'content-type': 'application/json'}
    grab_request = {'requestId': 77, 'version': 1, 'queries': ['sqa', 'testing', 'Москва'],
                    'period': {'fromDate': '2008-01-01', 'toDate': '2015-12-31'}}
    try:
        requests.post(grabber_url, data=json.dumps(grab_request), headers=request_headers)
    except ConnectionError:
        print 'Connection Error. Grabber is running?'


def many_grab_to_grabber():
    print 'Run: many_grab_to_grabber() - many POST to Grabber.'
    request_headers = {'content-type': 'application/json'}
    queries_list = [u'selenium', u'selenide', u'qa', u'sqa', u'testing', u'mobile testing', u'application testing',
                    u'test design', u'тестировщик', u'автоматизированные тесты', u'нагрузочное тестирование',
                    u'функциональное тестирование', u'тестирование', u'чеклист', u'инструменты тестирования']

    i = 2  # Количество запросов
    j = 0
    while j < i:
        random.seed()
        request_id = random.choice(range(1, 1000))
        random.seed()
        request_1 = get_random_object(queries_list)
        random.seed()
        request_2 = get_random_object(queries_list)

        grab_request = {'requestId': request_id, 'version': 1,
                        'queries': [request_1.encode("utf-8"), request_2.encode("utf-8")],
                        'period': {'fromDate': '2017-01-01', 'toDate': '2017-01-31'}}
        try:
            requests.post(grabber_url, data=json.dumps(grab_request), headers=request_headers)
        except ConnectionError:
            print 'Connection Error. Grabber is running?'
        j += 1


# Выдача случайного объекта из списка
def get_random_object(objects_list):
    random.seed()                       # Инициализация
    return random.choice(objects_list)
