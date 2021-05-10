# TryHackMe Auto README.md generator

This is a super-simple and lightweight tool to help you speed up your CTF documentation process.

> May, 2021 

---

Now you can create _**directories and README**_ files for your ctf's with only **one line**, all the **data** and **questions** will be automatically listed on the file, don't bother yourself copying those stuff, go directly to the action!

---

Use the pip to **install** the **TryHackMe api**:

````commandline
pip install thmapi
````

Now you just need to choose the **room** and **run the command**:

````commandline
python autoreadme.py vulnversity
````

- Plz note: 
  - ```python``` - calls **python**.
  - ```autoreadme.py``` - it's the **main script**.
  - ```vulnversity``` - it's the **name of the room**, can be changed for any other room.    
    _- **Remember this name needs to be equals to de url**, usually the room name in lowercase_
