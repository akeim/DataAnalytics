#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import pprint

def count_tags(filename):
    tag_dict = {}
    for event,element in ET.iterparse(filename):
        current_tag = element.tag
        if current_tag in tag_dict.keys():
            tag_dict[current_tag] += 1
        else:
            tag_dict[current_tag] = 1
    return tag_dict


def test():

    tags = count_tags('example.osm')
    pprint.pprint(tags)
    assert tags == {'bounds': 1,
                     'member': 3,
                     'nd': 4,
                     'node': 20,
                     'osm': 1,
                     'relation': 1,
                     'tag': 7,
                     'way': 1}



if __name__ == "__main__":
    test()
