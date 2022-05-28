[tox]
envlist = py37
skipsdist = True
 
[testenv]
deps =
    pytest
    coverage
commands =
    coverage run -m pytest
    coverage xml
 
[coverage:run]
relative_files = True
source = devopslab-7ASO/
branch = True