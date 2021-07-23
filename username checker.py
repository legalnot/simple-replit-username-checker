import requests
import os
checked = 0

m = input("Would you like to log your hits with a webhook? (y/n):  ")
if m == "y":
    webhook = input("Enter webhook:  ")
    with open("users.txt", "r") as f:
      lines = f.readlines()
      found = [None] * len(lines)

      c = 1
      t = 0
      for word in lines:
        if c != len(lines):
            word = word[:-1]
        url = 'https://replit.com/@' + word
        x = requests.get(url)
        if x.status_code== 200:
            checked = (checked + 1)
            print('(', checked, ')', word, ' Is Taken')
            print('')
        if x.status_code == 404:
          checked = (checked + 1)
          print('(', checked, ')', word, 'Is Available')
          data = {
            "content": word + " Is available!"
          }
          requests.post(webhook, data=data)
          print('')
          found[t] = word
          t += 1
        c += 1




else:
    with open("users.txt", "r") as f:
      lines = f.readlines()
      found = [None] * len(lines)

      c = 1
      t = 0
      for word in lines:
        if c != len(lines):
            word = word[:-1]
        url = 'https://replit.com/@' + word
        x = requests.get(url)
        if x.status_code== 200:
            checked = (checked + 1)
            print('(', checked, ')', word, ' Is Taken')
            print('')
        if x.status_code == 404:
          checked = (checked + 1)
          print('(', checked, ')', word, 'Is Available')
          print('')
          found[t] = word
          t += 1
        c += 1


with open("hits.txt", "w") as f:
  for i in found:
    if i == None:
      break
    f.write(i + str("\n"))
