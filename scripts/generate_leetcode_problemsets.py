""" 从Leetcode官网爬取一些关于问题的基本数据
"""
import pathlib
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json
import os


def step1():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    questions = []

    for i in range(1, 65 + 1):
        driver.get("https://leetcode.cn/problemset/all/?page=" + str(i))
        time.sleep(10)
        question = driver.find_element(value="__next")
        question_html = question.get_attribute("innerHTML")
        if question_html is None:
            continue
        soup = BeautifulSoup(question_html, "html.parser")
        question_title = soup.find_all(
            "div",
            class_="odd:bg-layer-1 even:bg-overlay-1 dark:odd:bg-dark-layer-bg dark:even:bg-dark-fill-4",
        )
        for t in question_title:
            is_plus = False
            if list(t.children)[0].svg is not None:
                is_plus = True

            questions.append(
                {
                    "is_plus": is_plus,
                    "number": ".".join(list(t.children)[1].a.string.split(".")[:-1]),
                    "name": list(t.children)[1].a.string.split(".")[-1],
                    "href": list(t.children)[1].a["href"],
                    "origin_str": list(t.children)[1].a.string,
                    "pass_rate": list(t.children)[3].string,
                    "difficulty": list(t.children)[4].string,
                }
            )
        print(questions)
    with open("docs\\problems.json", "w", encoding="utf-8") as f:
        json.dump(questions, f)


def step2():
    with open("docs\\problems.json", "r", encoding="utf-8") as f:
        questions = json.load(f)

    for question in questions:
        print(question)
        new_question_dir_path = pathlib.Path("problemset/" + question["origin_str"])
        if not new_question_dir_path.exists():
            os.mkdir("problemset/" + question["origin_str"])


if __name__ == "__main__":
    step1()
    # step2()
