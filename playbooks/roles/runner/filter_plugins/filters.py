#!/usr/bin/python

import toml
import json

class FilterModule(object):

    def filters(self):
        return {
            'to_toml': self.to_toml,
            'from_toml': self.from_toml
        }

    def to_toml(self, variable):
        s = json.dumps(dict(variable))
        d = json.loads(s)
        return toml.dumps(d)

    def from_toml(self, variable):
        s = toml.loads(variable)
        d = json.dumps(dict(s), default=str)
        return json.loads(d)
