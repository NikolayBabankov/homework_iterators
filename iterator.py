import json

class Myiterator:

    def __init__(self, file_json):
        self.file_json = file_json
        with open(self.file_json,) as f:
            self.data = json.load(f)
        self.current_list_index = 0
        self.dict_index1 = 'name'
        self.dict_index2 = 'official'

    
    def __iter__(self):
        return self
    

    def __next__(self):
        current_data = self.data[self.current_list_index]
        item = current_data[self.dict_index1][self.dict_index2]
        self.current_list_index += 1
        if self.current_list_index == len(self.data):
            raise StopIteration
        return item


def write_url():
    url = 'https://www.wikipedia.org/wiki/'
    json_dist = {}
    for item in Myiterator("countries.json"):
        item_list = item.split()
        item_url  = '_'.join(item_list)
        json_dist.setdefault(item, url + item_url)
        with open('country.json', 'w',encoding= "utf-8") as f:
            json.dump(json_dist, f,sort_keys=True, indent=2,ensure_ascii=False)


if __name__ == '__main__':
    write_url()
