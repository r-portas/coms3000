# Tutorial 6: Access Control

## Q1: User Permissions

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

## Q2: Unix Permissions

a) `-rwxr-x--- bill student thefile.txt`

Owner: read, write, execute

Student group: read, execute

Other: -


b) `-r-xrwxr-- bill student thefile.txt`

Owner: read, execute

Student group: read, write, execute

Other: read

Bill does not have write access, because his owner priviledges override the group ones

## Q3: What is the problem with SUID feature in Unix

SUID allows users to run a program with the owner's priviledges, this is useful for system services such as restarting the network stack. This allows user's to access programs that usually only root has access to. However if a program is replaced with malicous code, an attacker could execute commands as root.

## Q4: What is the difference between DAC and MAC

__Mandatory Access Control__
- Every user has a clearance level
- Each file has a classification
- Follows the principles of need to know

__Discretionary Access Control__
- Classic unix style
- Allows user's to choose who can access a file
- Permissions defined by the owner

## Q5: What is a part of Unix that acts like MAC

From memory, the system startup process (init/systemd) starts up as root, launches the system processes as root then locks out access to those processes once the system startup is done. I believe once systemd has started the system, it revokes its root privileges and becomes a standard system user.

## Q6: What is the difference between a "classification" and a "clearance"?

Documents have a classification, which is the access level required to view or edit it. Clearance is the process of giving a user permission to view classified files.

## Q7: What is the main goal of the Bell-LaPadula model?

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

![Lattice](resources/AuthLattice.png "Lattice")
\ 

## Question 10

Reading a file above the current security level will cause the user's high water mark to move. As this will change the current security level to the level of the file.

## Question 11

A covert channel allows the transfer of information between processes who are not mean't to communicate with each other, as outlined by the system's security policy.
