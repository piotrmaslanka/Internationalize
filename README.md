internationalize
========
[![PyPI version](https://badge.fury.io/py/internationalize.svg)](https://badge.fury.io/py/internationalize)
[![PyPI](https://img.shields.io/pypi/pyversions/internationalize.svg)]()
[![PyPI](https://img.shields.io/pypi/implementation/internationalize.svg)]()
[![PyPI](https://img.shields.io/pypi/wheel/internationalize.svg)]()
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)]()

A library to help you with internationalizing your application.
[Here's a guide to using it](https://github.com/piotrmaslanka/Internationalize/wiki/How-to-use-Internationalize)

Intro
-----

While most Python internationalize libraries take an approach
with your providing a language and a keyword, and returning
a resembling string from an internal database, Internationalize 
takes a different approach.

Internationalize asks you to provide a keyword, and then returning
a string containing a selection of the languages.

Where you would configure the standard library with dictionary of mappings,
where each mapping would contain

```
configure_me({'hello': {'pl': 'Witaj'}, {'en': 'Hello'}})
pick_language('en')
...
assert get_translation('hello') == 'Hello' 
```

Internationalize does the following:

```
configure_me({'hello': {'pl': 'Witaj'}, {'en': 'Hello'}})
...
assert get_translation('hello') == {'pl': 'Witaj', {'en': Hello'}}
```

Which is super useful for handling certain applications that require those.
