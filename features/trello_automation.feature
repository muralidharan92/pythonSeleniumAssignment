Feature: Automating Trello

  Background: Pre-request
    Given launch "chrome" browser and open trello
    When user login to the application using username "username" and password "password"


  Scenario: Automate Trello and perform trello functional activities
    When click "Create new board" from board tiles
    And add board using with visibility "Team Visible"
    Then verify board added successfully
    When add list with name of "Not Started,In Progress,QA,Done"
    Then verify "Not Started,In Progress,QA,Done" list added
    When create card "Card 1,Card 2,Card 3,Card 4" under "Not Started" list
    And move "Card 2" from "Not Started" list to "In Progress" list
    And move "Card 3" from "Not Started" list to "QA" list
    And move "Card 2" from "In Progress" list to "QA" list
    And open "Card 1" card from "Not Started" list
    And assign it to current logged in user and add comment as "I am done"
    Then verify current user assigned and comment added as "I am done"