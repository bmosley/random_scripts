class CoolDict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__



some_dict = {"bryan": "best", "matt": "better", "human": "good"}

some_dict = CoolDict(some_dict)

print(some_dict.bryan)
print(some_dict.matt)