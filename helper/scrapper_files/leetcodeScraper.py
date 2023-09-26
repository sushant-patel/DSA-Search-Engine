import time
import os.path

from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://leetcode.com/problemset/all/?page=1&topicSlugs=dynamic-programming")
time.sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

allTagsDiv = soup.findAll("div", {"class": "group m-[10px] flex items-center"})

allTagsAnchorTags = []
allTagsSpanTags = []

for tag in allTagsDiv:
    # print(tag)
    # print(tag.find("a"))
    allTagsAnchorTags.append(tag.find("a"))

for tag in allTagsAnchorTags:
    allTagsSpanTags.append(tag.find("span"))

tagTitles = []
tagUrls = []

for tag in allTagsAnchorTags:
    tagUrls.append("https://leetcode.com" + tag['href'])

for tag in allTagsSpanTags:
    tagTitles.append(tag.text)

for i in range(len(tagTitles)):
    driver.get(tagUrls[i])
    time.sleep(10)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    allProbsDiv = soup.findAll("div", {"class": "title-cell__ZGos"})

    allProbsAnchorTags = []

    for prob in allProbsDiv:
        ProbsSpanTag = []
        ProbsSpanTag = prob.findAll("span")
        if len(ProbsSpanTag) > 0:
            continue
        allProbsAnchorTags.append(prob.find("a"))

    Q_Titles = []
    Q_urls = []

    count = 0
    for prob in allProbsAnchorTags:
        if(count >= 100):
            break
        Q_urls.append("https://leetcode.com" + prob['href'])
        Q_Titles.append(prob.text)
        count += 1

    savePath = "C:/Users/Akshat Jain/PycharmProjects/scraper/"
    # os.makedirs(savePath)
    file1Name = "problem_urls.txt"
    file2Name = "problem_titles.txt"
    completeName1 = os.path.join(savePath, file1Name)
    completeName2 = os.path.join(savePath, file2Name)

    with open(completeName1, "a+") as f:
        f.write('\n'.join(Q_urls))
        f.write('\n')
    with open(completeName2, "a+") as f:
        f.write('\n'.join(Q_Titles))
        f.write('\n')
    time.sleep(4);
