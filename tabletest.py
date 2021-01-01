from texttable import Texttable
t = Texttable()
headers = ['Name',
             'Age', 
             'Highest Quali', 
             'Number of Poles', 
             'Best Race Finish', 
             'Number of Podiums',
             'Number of Track Records']
values = ['Carlos Sainz Jr',
             '26', 
             'P3', 
             '0', 
             'P2', 
             '2',
             '1']
t.add_rows([headers, values])
row1 = '|Highest Quali Finish|Highest Race Finish|Number of Podiums|+\n'
row2 = '|:-|:-|:-|+\n'
row3 = '|P3|P2|2|'

response = row1+row2+row3
bot_phrase = "Sainz Jr Stat Bot says: \n"+response 
print(bot_phrase)