*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  mina  12345678
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  12345678
    Output Should Contain  Username is already taken

Register With Too Short Username And Valid Password
    Input Credentials  mo  12345678
    Output Should Contain  Username is too short, it should be at least 3 characters long

Register With Enough Long But Invald Username And Valid Password
    Input Credentials  mo1  12345678
    Output Should Contain  Invalid username, it should only contain letters from a-z

Register With Valid Username And Too Short Password
    Input Credentials  mina  1234
    Output Should Contain  Password is too short, it should be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  mina  abcdefgh
    Output Should Contain  Invalid password, it should contain at least 1 number

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command
