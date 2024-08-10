import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    # file_name = f'{user_id}.csv'
    url = url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    user_name = user.get("username")
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    
    with open(f'{user_id}.csv', "w", newline="") as file:
            writer = csv.writer(file,quoting=csv.QUOTE_ALL)
            for t in todos:
                writer.writerow(
                    [ user_id,
                    user_name,
                    t.get('completed'),
                    t.get("title")
                ]
                        )