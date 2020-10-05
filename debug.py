import unittest
import pytest
from nfceget import app
from nfceget.StateInvalidError import StateInvalidError

data = app.json_from_file('./tests/html/pr/receitaestadual1.html')

print(data)