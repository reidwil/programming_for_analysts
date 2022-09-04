from typing import List, Optional

# With this code, how could you:
# 1> Pop and push items into a "stash" within the class
# 2> Provide an example of how you could run this class 
#    to prove step 1 worked

MyDataObj: str = 'Test'

class StashBag:
    _item: Optional[MyDataObj] = None
    _item_stash: List[MyDataObj] = []

    @classmethod
    def current_item(cls):
        return cls._item

    @classmethod
    def pop_item_stash(cls) -> Optional[MyDataObj]:
        old_item = cls._item
        if cls._item_stash:
            cls._item = cls._item_stash.pop()
        else:
            cls._item = None
        return old_item
    
    @classmethod
    def push_item_stash(cls, item: MyDataObj):
        if cls._item:
            cls._item_stash.append(cls._item)
        cls._item = item

class Item:
    def __enter__(self):
        StashBag.push_item_stash(self)
        return self
    def __exit__(self, _type, _value, _tb):
        StashBag.pop_item_stash()


if __name__=='__main__':
    with Item() as item:
        StashBag.push_item_stash(item)
        print(StashBag.current_item())
    