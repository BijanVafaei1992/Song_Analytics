#!/usr/bin/env python
# coding: utf-8

import json


class JsonObj:

    def get_config_obj(self,key_to_search):
        with open('Configs.json') as json_file:
            config = json.load(json_file)
        return config[key_to_search]

