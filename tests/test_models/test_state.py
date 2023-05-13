#!/usr/bin/python3
'''Tests User class'''

import models
from models.base_model import BaseModel
from models.state import State
import os
import unittest


class TestState(unittest.TestCase):
    '''start test'''

    def test_docstring(self):
        '''test forf if funcions, methods, classes
        and modules have docstring'''
        msj = "Módulo does not has docstring"
        self.assertIsNotNone(models.state.__doc__, msj)  # Modules
        msj = "Clase does not has docstring"
        self.assertIsNotNone(State.__doc__, msj)  # Classes

    def test_executable_file(self):
        '''test for if file has permissions u+x to execute'''
        # Check for read access
        is_read_true = os.access('models/state.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('models/state.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('models/state.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        '''check for if my_model is an instance of BaseModel'''
        my_state = State()
        self.assertIsInstance(my_state, State)
