# Docupy

A (probably silly) terminal command wrapper used for documenting the command 
that was run.

Install:
```
$ pip install git+https://github.com/SamDSchofield/docupy.git
```

Usage:
```
$ doc --output.txt command
```

Example:
```
$ doc --example.txt ls
Notes: Running ls as an example for docupy

$ cat example.txt
Command:
ls

Run at 2021-06-22 17:22:08.432498

Notes:
Running ls as an example for docupy
``` 