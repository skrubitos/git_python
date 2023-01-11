'''
program for scraping email adresses
made by skrubitos
in this program we will import some lis
'''
import time

print('This is a list of emails that you found on a web and you want to scrape just emails')
time.sleep(2)

# you can change random_emails and put your list
random_emails = '''
Please send your documents to john@gmail.com
My email address is sarahm@yahoo.com
You can reach me at peterj@outlook.com
For any inquiries, please email info@company.com
Thank you for your email, jane@hotmail.com
Our sales team can be reached at sales@company.com
I can be contacted at michaelb@aol.com
You can find our latest product offerings at catalog@company.com
Our support team can be reached at support@company.com
Please send all press inquiries to press@company.com
If you have any questions, you can email me at tom@gmail.com
You can contact our HR department at hr@company.com
For any billing issues, please email billing@company.com
Our marketing team can be reached at marketing@company.com
You can find our latest job openings at jobs@company.com
Please send all vendor inquiries to vendors@company.com
If you need to contact me, you can email me at dave@yahoo.com
Our finance team can be reached at finance@company.com
You can contact our customer service department at customerservice@company.com
Please send all legal inquiries to legal@company.com
If you have any comments or suggestions, you can email me at kim@outlook.com
You can contact our IT department at IT@company.com
Please send all partnership inquiries to partnerships@company.com
If you have any questions about our products, you can email me at sam@aol.com
You can contact our design team at design@company.com
Please send all event inquiries to events@company.com
If you need to reach me, you can email me at anna@hotmail.com
You can contact our research and development team at R&D@company.com
Please send all investor inquiries to investors@company.com
If you have any questions about our company, you can email me at matt@gmail.com'''
print(random_emails)
time.sleep(3)
print('\n\n Scrapping emails please wait a moment')
time.sleep(0.5)
for i in range(10):
    print('*' * i)
    time.sleep(0.15)

for z in range(10, 0, -1):
    print('*' * z)
    time.sleep(0.05)

# now we will find index number of monkey character
index_monkey = []  # we will store index in this list
ind = -1
for monkey in random_emails:
    ind += 1
    if monkey == "@":
        index_monkey.append(ind)

# creating list to store index numbers of ending whitespace
end_email = []  # end email= ee
for index in index_monkey:
    find_ee = random_emails.find(" ", int(index))
    end_email.append(find_ee)

# merging together mid indexes and end indexes
mid_end = []  # list containing mid monkey character to end of email containtg TLD Topl Level Domain
for i in range(len(end_email)):
    try:
        mid_end.append(random_emails[int(index_monkey[i]): int(end_email[i])])
    except IndexError:
        pass
# finding first part till mid monkey
begin_email = []  # list to put index numbers of first characters BE
for i in index_monkey:
    find_be = random_emails.rfind(" ", 0, i)
    begin_email.append(find_be)

begin_mid = []  # list that will merge beginning to mid monkey
for i in range(len(index_monkey)):
    begin_mid.append(random_emails[int(begin_email[i]):  int(index_monkey[i])])

# now we have list begin_mid and mid_end and we will merge them together
all_mergano = []  # since there is \n in random_emails it will not look good graphicly so we will need to edit it more
for i in range(len(mid_end)):
    all_mergano.append(begin_mid[i] + mid_end[i])

# if he finds \n in list index he will remove it and everything after it
for i in range(len(all_mergano)):
    if '\n' in all_mergano[i]:
        all_mergano[i] = all_mergano[i].split('\n')[0]
    else:
        pass

time.sleep(2)
print('Scrapping done')
# now we will add option to save or not to save
choice = input('\n\nDo you want to save file as txt? (Y|N):')
if choice.upper() == 'Y':
    name_of_file = input('How would you like to name your file?: ')
    print(f'File {name_of_file} was created')
    with open(name_of_file, 'w') as f:
        f.write(f'We found exactly {len(all_mergano)} emails \n')
        for i in all_mergano:
            f.write(str(i) + '\n')
else:
    print('Okay here is your list of emails')
    for i in all_mergano:
        print(i)

end = input('this is end of program if you want to end just press enter')
