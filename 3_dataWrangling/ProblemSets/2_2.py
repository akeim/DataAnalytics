#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from bs4 import BeautifulSoup
html_page = "options.html"


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        soup = BeautifulSoup(html)
        airports = soup.find(id="AirportList").find_all('option')
        for air_code in airports:
            data.append(air_code["value"])
        for value in data:
            if "All" in value:
                data.remove(value)

    return data[1:]


def test():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

test()
