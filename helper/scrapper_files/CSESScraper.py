# import os

# driver = webdriver.Chrome(ChromeDriverManager().install())


# driver.get("https://cses.fi/problemset/")
# time.sleep(5)
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
#
# ques_table = soup.findAll("li", {"class": "task"})
#
# urls = []
# titles = []
#
# for row in ques_table:
#     anchor = row.find("a")
#     # print(anchor)
#     titles.append(anchor.text)
#     urls.append("https://cses.fi"+anchor['href'])
#
#
# with open("problem_urls.txt", "a+") as f:
#     f.write('\n'.join(urls))
#
# with open("problem_titles.txt", "a+", encoding="utf-8") as f:
#     f.write('\n'.join(titles))


# driver.get("https://cses.fi/problemset/task/1068")
# time.sleep(5)
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# problem = soup.find("div", {"class": "content"})
#
# txt = problem.text
#
# with open("cses_problem_text"+""+".txt", "w+", encoding="utf-8") as f:
#     f.write(txt)

# driver.get("https://www.codechef.com/submit-v2/HIGHSCORE")
# time.sleep(5)
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# problem = soup.find("div", {"id": "problem-statement"})
#
# txt = ""
#
# z = 0
# for tag in problem.findAll(True):
#     z += 1
#     if tag.name == "h2" and z == 1:
#         continue
#     if tag.name == "h3":
#         if z == 2:
#             continue
#         else:
#             break
#     if tag.name == "p" or tag.name == "ul":
#         txt += tag.text
#
# with open("problems/problem_text_"+"0"+".txt", "w+", encoding="utf-8") as f:
#     f.write(txt)


for i in range(2986, 3286):
    quesFile = open("problems/problem_text_"+str(i)+".txt", "r")
    content = quesFile.read()
    line_list = content.split("\n")
    quesFile.close()
    txt = ""
    for line in line_list:
        # print(line)

        if "Time limit:" in line : continue
        if "Memory limit:" in line : continue

        if line == "Input": break

        txt += line
        txt += " "

    with open("problems/problem_text_"+str(i)+".txt", "w") as f:
        f.write(txt)
