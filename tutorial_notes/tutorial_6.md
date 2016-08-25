# Tutorial 6: Access Control

## Question 1

a)

|              | alice.sh         | bob.sh          | charlie.sh             |
| ------------ | ---------------- | --------------- | ---------------------- |
| Alice        | {execute}        | {read}          | -                      |
| Bob          | {read}           | {execute}       | -                      |
| Charlie      | {read}           | {read, write}   | {read, write, execute} |

b)

|              | alice.sh               | bob.sh                 | charlie.sh             |
| ------------ | ---------------------- | ---------------------- | ---------------------- |
| Alice        | {execute}              | {read}                 | {read}                 |
| Bob          | -                      | {execute}              | -                      |
| Charlie      | {read, write, execute} | {read, write, execute} | {read, write, execute} |

## Question 2

a) 


Owner: read, write, execute

Student group: read, execute

Other: -


b)

Owner: read, execute

Student group: read, write, execute

Other: read

Bill does not have write access, because his owner priviledges override the group ones

## Question 3

SUID allows users to run a program with the owner's priviledges, this is useful for system services such as restarting the network stack. This allows user's to access programs that usually only root has access to. However if a program is replaced with malicous code, an attacker could execute commands as root.

## Question 4

__Mandatory Access Control__
- Every user has a clearance level
- Each file has a classification
- Follows the principles of need to know

__Discretionary Access Control__
- Classic unix style
- Allows user's to choose who can access a file
- Permissions defined by the owner

## Question 5

From memory, the system startup process (init/systemd) starts up as root, launches the system processes as root then locks out access to those processes once the system startup is done. I believe once systemd has started the system, it revokes its root privileges and becomes a standard system user.

## Question 6

Documents have a classification, which is the access level required to view or edit it. Clearance is the process of giving a user permission to view classified files.

## Question 7

The main goal of the Bell-LaPadula model is to ensure information does not leak down. Meaning a person with unclassified clearance cannot access files with classified clearance. It can be broken down into two rules

- __Simple Security Policy__

A subject can only read an object if its clearance dominates the object's classification

- __Star Property__

A subject at a given security level must not write to any object at a lower security level

## Question 8

Allowed methods:

- Alice reads a document written by Bob
- Bob sends Alice a document that he has written
- Alice reads a document with the label 'secret'
- Bob reads an unclassified document and sends it to Alice

## Question 9

![Lattice](resources/tut_5_block_diagram.png "Lattice")

## Question 10


