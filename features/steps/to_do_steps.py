from behave import given, when, then
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


def set_up(context):
    context.chrome_options = Options()
    context.chrome_options.add_argument("--disable-extensions")
    context.chrome_options.add_argument("--incognito")
    context.chrome_options.add_argument("--disable-popup-blocking")
    context.chrome_options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(options=context.chrome_options)
    context.driver.get("https://todomvc.com/examples/angularjs/#/")
    context.driver.implicitly_wait(10)
    context.action_chains = ActionChains(context.driver)


def add_a_new_task(context, task):
    context.driver.find_element_by_xpath("/html/body/ng-view/section/header/form/input").send_keys(task + "\n")


@given(u'I am in the todos page And there is a task "Wake up" in the list')
def step_impl(context):
    set_up(context)
    time.sleep(1)
    add_a_new_task(context, "Nothing to do")
    add_a_new_task(context, "i actually cen do something")
    add_a_new_task(context, "Wake up")
    add_a_new_task(context, "Clean the house")
    add_a_new_task(context, "i'm done")
    time.sleep(1)


@when(u'I edit the task "Wake up" to be "Go to sleep"')
def step_impl(context):
    todo_list = context.driver.find_elements_by_xpath("/html/body/ng-view/section/section/ul/li")
    form_list = context.driver.find_elements_by_class_name("edit")
    i = 0
    for i in range(len(todo_list)):
        if todo_list[i].text == "Wake up":
            print(str(i))
            task_to_edit_line = todo_list[i]
            context.action_chains.double_click(task_to_edit_line).perform()
            for j in range(len("Wake up")):
                form_list[i].send_keys("\u0008")
            form_list[i].send_keys("Go to sleep" + "\n")
            break
    context.num = i


def get_all_task(context):
    context.list =  [t.text for t in context.driver.find_elements_by_xpath("/html/body/ng-view/section/section/ul/li/div")]


@then(u'the task list will be')
def step_impl(context):
    get_all_task(context)
    assert(context.list[context.num] == "Go to sleep", "Go to sleep is not in the todo list")
    context.driver.close()
