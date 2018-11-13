import collections


def in_list(collection, key, list):
    '''
    extract x for every item x in the collection if x[key] is in the list
    '''

    return [x for x in collection if x[key] in list]


def not_in_list(collection, key, list):
    '''
    extract x for every item x in the collection if x[key] is not in the list
    '''

    return [x for x in collection if x[key] not in list]


def flatten(d, parent_key='', sep='.'):
    '''
    Flatten a nested python dictionary compressing the keys
    '''

    items = []

    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))

    return dict(items)

class FilterModule(object):
    '''
    custom jinja2 filters for working with collections
    '''

    def filters(self):
        return {
            'in_list': in_list,
            'not_in_list': not_in_list,
            'flatten_collection': flatten
        }