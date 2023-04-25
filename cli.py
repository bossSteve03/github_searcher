import requests
from time import sleep

username = input("Enter GitHub username:\n")

r = requests.get(f'https://api.github.com/users/{username}/repos')
print('')
print(f'Status: {r.status_code}')
print('')
json_response = r.json()

number = 1

for e in json_response:
  repo_name = e['name']
  sleep(0.1)
  print(f'{number}. {repo_name}')
  number = number + 1
print('')

sleep(0.5)

while (True):
  try:
    def input_text():
      print("Select repo by list number (for more details)")
      sleep(0.1)
      print("Enter \'exit\' to exit program.")
      sleep(0.1)
      print("Enter \'list\' to relist repos.\n")
      global select_number
      select_number = input('')
    input_text()
    if select_number == 'exit':
      exit()
    elif select_number == 'list':
      number = 1
      for e in json_response:
        repo_name = e['name']
        sleep(0.1)
        print(f'{number}. {repo_name}')
        number = number + 1
      print('')
    else:
      select_number = int(select_number) - 1
      if select_number < len(json_response) and select_number > -1:
        repo = json_response[select_number]
        print('')
        sleep(0.1)
        print('name: ' + repo['name'])
        sleep(0.1)
        print('visiblity: ' + repo['visibility'])
        sleep(0.1)
        print('id: ' + str(repo['id']))
        sleep(0.1)
        print('description: ' + str(repo['description']))
        sleep(0.1)
        print('forks: ' + str(repo['forks']))
        sleep(0.1)
        print('watchers: ' + str(repo['watchers']))
        sleep(0.1)
        print('clone git url: ' + repo['git_url'])
        sleep(0.1)
        print('clone ssh url: ' + repo['ssh_url'])
        print('')
      else:
        print('Number doesnt exist on list, try again.')
        {sleep(0.1)}
  except ValueError:
    continue
