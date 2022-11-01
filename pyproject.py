import time

a = 0
while a < 3:
    a += 1
    print(a)
    time.sleep(0.4)
["project"]
name = "oybegim"
keywords = ["automation", "flake8", "pycodestyle", "pyflakes", "pylint"]
classifiers = [
    "Develompent Status :: 3-Alpha",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Software Development :: Quality Assurance",
]
print(name)
print(keywords)
print(classifiers)


b = 0
while b < 4:
    b += 1
    print(b)
    time.sleep(0.4)
author = "Oybegim"
author_email = "sultonovaoybegim@gmail.com"
description = "An extremely fast Python linter, written in Rust."
requires_python = ">=3.7"

print(author)
print(author_email)
print(description)
print(requires_python)


c = 0
while c < 4:
    c += 1
    print(c)
    time.sleep(0.4)
print("project.urls")
repository = "github.com/oybegim"
print(repository)


d = 0
while d < 4:
    d += 1
    print(d)
    time.sleep(0.4)
print("buil-system")
requires = ["maturin>=0.13,<0.14"]
build_backend = "maturin"
print(requires)
print(build_backend)


e = 0
while e < 4:
    e += 1
    print(e)
    time.sleep(0.4)
print("tool.maturin")
bindings = "bin"
sdist_include = ["Cargo.lock"]
strip = "true" 
print(bindings)
print(sdist_include)
print(strip)