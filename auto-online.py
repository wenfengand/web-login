import requests

def test_login():
    test_url = 'https://www.baidu.com'
    ret = requests.get(test_url).text 
    if 'location=' in ret:
        return False 
    else:
        return True 
if __name__ == '__main__':
    print(test_login())