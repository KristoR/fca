"""
FCA - Python libraries to support FCA tasks
Copyright (C) 2017  Victor Codocedo

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
# Kyori code.
from __future__ import print_function
import argparse
from fca.io.input_models import FormalContextModel
from fca.algorithms import dict_printer
from fca.algorithms.next_closure import NextClosure


def exec_ex9(filepath, min_sup=0):
    """
    Executes NextClosure in a single line
    """
    dict_printer(NextClosure(FormalContextModel(filepath=filepath), min_sup=min_sup, lazy=False).poset)


if __name__ == '__main__':
    __parser__ = argparse.ArgumentParser(description='Example 9 - FCA with NextClosure')
    __parser__.add_argument('context_path', metavar='context_path', type=str, help='path to the formal context in txt, space separated values, one object representation per line', action='store')
    __parser__.add_argument('-m', '--min_sup', metavar='min_sup', type=float, help='Relative minimum support [0,1]', default=0.0)
    __args__ = __parser__.parse_args()
    exec_ex9(__args__.context_path, __args__.min_sup)
# okay decompiling ex9_next_closure.pyc
