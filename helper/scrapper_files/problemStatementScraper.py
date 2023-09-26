import time
import os.path

# save_path = 'C:/example/'
# name_of_file = raw_input("What is the name of the file: ")
# completeName = os.path.join(save_path, name_of_file+".txt")
# file1 = open(completeName, "w")
# toFile = raw_input("Write what you want into the field")
# file1.write(toFile)
# file1.close()

from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

allUrlsFile = open("C:/Users/Akshat Jain/PycharmProjects/scraper/problem_urls.txt", "r")
content = allUrlsFile.read()
# print(content)
url_list = content.split("\n")
allUrlsFile.close()
# print(content_list)

driver = webdriver.Chrome(ChromeDriverManager().install())


# driver.get("https://leetcode.com/problemset/all/?page=1&topicSlugs=dynamic-programming")
# time.sleep(2)
# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")
#
# allTagsDiv = soup.findAll("div", {"class": "group m-[10px] flex items-center"})
#
# allTagsAnchorTags = []
# allTagsSpanTags = []
#
# for tag in allTagsDiv:
#     allTagsAnchorTags.append(tag.find("a"))
#
# for tag in allTagsAnchorTags:
#     allTagsSpanTags.append(tag.find("span"))
#
# tagTitles = []
#
# for tag in allTagsSpanTags:
#     tagTitles.append(tag.text)



# cnt = 126
for cnt in range(1734, 2986):
    # cnt += 1
    driver.get(url_list[cnt])
    time.sleep(6)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    allPTags = soup.findAll("div", {"class": "content__u3I1 question-content__JfgR"})[0].findAll("p")

    allPTextContent = []

    fullProblemStatement = ""

    for tag in allPTags:
        if tag.text == "Example 1:":
            break
        fullProblemStatement = fullProblemStatement + tag.text

    #print(fullProblemStatement)
    savePath = "C:/Users/Akshat Jain/PycharmProjects/scraper/problems"
    # if not os.path.exists(savePath):
    #     os.makedirs(savePath)
    fileName = "problem_text_" + str(cnt + 1) + ".txt"
    completeName = os.path.join(savePath, fileName)
    file1 = open(completeName, "wb")
    file1.write(fullProblemStatement.encode('utf-8'))
    file1.close()
