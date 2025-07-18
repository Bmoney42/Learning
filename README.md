# Learning
**Over The Wire - War Games - Bandit**

Level 0 - First One Was Easy. 
Open Up Shell Terminal 
>ssh -p 2220 bandit0@bandit.labs.overthewire.org

**Level 0 --> Level 1** 
I Did 
```
ls
```
And 
```
cat readme.txt
```
Password: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

**Level 1 --> Level 2:** i Used Cat to Redirect The File "-" to reveal the password

```
cat < -
```

Password: 263JGJPfgU6LtdEvgfWU1XP5yac29mFx

**Level 2 -> level 3**

Same As Before Cat < but I Used Tab To Complete The File Name 
```bash
 cat < spaces\ in\ this\ filename
```

Password:MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

**Level 3 --> level 4**

There is a hidden file in here. 
```bash
cd  inhere
ls -a
cat <  ...Hiding-From-You
```
Password: 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

**Level 4 --> Level 5** 

```bash
ls inhere
cat < -file07

```

Password: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

**Level 5 --> Level 6**

inside the level they gave you some clues, like how large the file was 1033 bytes so I searched the system for a file with 1033 btyes

```bash
find / -type f -size 1033c
```

Password: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

**level 6 --> Level 7**
Same as before but expanded to -user and -group 

```bash
find / -type f -size 33c -user brandit7 -group bandit6
```
Password: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

**level 7 --> Level 8**

We had to use grep to find a string within a file to find the password:


```bash
 grep "millionth" data.txt
```
Password: dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

**Level 8 --> Level 9**

Sort And Find Uniq Lines 

```bash
sort data.txt | uniq -u 
```

Password: 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM

**Level 9 --> Level 10**
only shows readable human data

```bash
strings data.txt
```
password: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey

**Level 10 --> level 11**

We are looking for decode the base64 data  in data.txt

```bash
base64 -d data.txt
```
Password: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr

**Level 11 --> Level 12**

```bash

```

**Level 12 --> Level 13**

```bash

```
