# TryHackMe Auto README.md generator

This is a super-simple and lightweight tool to help you speed up your CTF documentation process.

> May, 2021 

---

Now you can create _**directories and README**_ files for your ctf's with only **one line**, all the **data** and **questions** will be automatically listed on the file, don't bother yourself copying those stuff, go directly to the action!

---

### Basic Information: 

- Tags:
  - ```-r``` - it's the operator to select the **room**.
    - Ex: ```-r vulnversity``` 
  - ```-A``` - it's the **Aggressive** mode, creates full README.md with **Scan, System Info, Directory Scan and Users & Passwords notation area.**
    - Ex: ```-r vulnversity -A``` 

---

### Installation: 


Use the pip to **install** the **TryHackMe api**:

````shell
pip install thmapi
````

Now you just need to choose the **room** and **run the command**:

- For the simple README.md file:
````commandline
python autoreadme.py -r vulnversity
````

- For the advanced README.md file:
````commandline
python autoreadme.py -r vulnversity -A
````

- Plz note: 
  - ```python``` - calls **python**.
  - ```autoreadme.py``` - it's the **main script**.
    - ```-r``` - it's the operator to select the **room**.
  - ```vulnversity``` - it's the **name of the room**, can be changed for any other room.    
    _- **Remember this name needs to be equals to de url**, usually the room name in lowercase_
    - ```-A``` - it's the **Aggressive** mode, creates full README.md with **Scan, System Info, Directory Scan and Users & Passwords notation area.**
