# Basic Bash

[Bash](https://www.gnu.org/software/bash/) (Bourne Again SHell) is used as the GNU shell, and is what you will most commonly use when you open a terminal.

You can use bash to navigate and modify your computer's file system, execute programs, control jobs, and as a scripting language (so basically you can do everything).

Importantly, you can do many things in bash that are impossible to do just using your standard file system graphical browers.  Also importantly, when you access remote machines, you will have no other choice than to use bash.

Here is basic use, which will assume you have opened a terminal.  Comments follow a pound symbol (`#`).  Open up a terminal and follow along.

```bash
pwd # print working directory
```
should print your working directory.  Usually this will start out as `/home/user` where `user` is your user name

```bash
whoami # prints your user name
```

```bash
mkdir test # makes a directory called test
```

```bash
ls # lists files and directories
```
You will likely see a variety of files if you execute this in your home directory

```bash
cd test # changes working directory to test
```

Now, if you execute `pwd`, you should see something like `home/user/test`.  If you execute `ls`, you shouldn't see anything (because there is nothing in test)

```bash
touch a.txt # creates empty file a.txt
```

Now, try `ls` - what do you see?

```bash
mv a.txt b.txt # moves a.txt to b.txt
```

Now what do you see with `ls`?

```bash
cp b.txt c.txt # makes a copy of b.txt and calls it c.txt
```

Now what do you see with `ls`?

```bash
rm c.txt # deletes c.txt
```

try using `ls` again.

```bash
echo 'print("hello world!")' >> hello.py # prints text to file hello.py
```

try using `ls` again.

Let's see what is in `hello.py`
```bash
cat hello.py # prints contents of hello.py
```
Assuming you have python installed, you can run `hello.py` as a python script
```bash
python hello.py
```
This should print `hello world!` to the terminal.

```bash
cd .. # goes up one directory level
```

Now if you `pwd`, you should be back at `/home/user`

```bash
rm -r test # removes test folder recursively
```

What happens if you try `cd test`?

```bash
exit # closes terminal
```
