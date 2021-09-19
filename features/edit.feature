# Created by מנחם אורן at 9/19/2021
Feature:  edit a new task
  # Enter feature description here

  Scenario: # Enter scenario name here
        Given I am in the todos page And there is a task "Wake up" in the list
		When I edit the task "Wake up" to be "Go to sleep"
		Then the task list will be
			| TaskName    | IsCompleted |
			| Go to sleep | False       |