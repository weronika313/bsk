import random
from typing import Final

import pandas as pd


class LFSR:
    def __init__(self, string_function:str):
        self.function: list[bool] = parse_function(string_function)
        self.register: Final[Register] = Register(len(self.function))

        self.blocks_to_xor: list[int] = None
        for i in range(1, len(self.function)):
            if self.function[i]:
                self.blocks_to_xor.append(i-1)

        self.output = self.generate_output()

    def generate_output(self) -> list[bool]:
        starting_register: Register = self.register
        self.next_bit()
        output = []
        while starting_register.blocks != self.register.blocks:
            output.append(self.register.get_blocks()[0])
            self.next_bit()

        output.append(self.register.get_blocks()[0])

        return output


    def next_bit(self) -> bool:
        return self.register.tick(self.blocks_to_xor)


def parse_function(function: str) -> list[bool]:
    last_char: str = function[-1]
    length: int = 2 if last_char == 'x' else int(last_char) + 1
    bool_list: list[bool] = [False for i in range(length)]
    polynomial_terms: list[str] = function.split("+")

    for term in polynomial_terms:
        if term == "1":
            bool_list[0] = True
        elif term == "x":
            bool_list[1] = True
        else:
            bool_list[int(term[-1])] = True

    return bool_list


class Register(object):
    def __init__(self, size:int):
        self.blocks :list[bool] = []
        self.result: bool = None
        if size > 2:
            for i in range(size-1):
                self.blocks.append(random.choice([True, False]))

            while pd.Series(self.blocks).nunique():
                self.randomize()
        else:
            self.blocks.append(True)


    def randomize(self):
        for i in range(len(self.blocks)):
            self.blocks[i] = random.choice([True, False])

    def get_blocks(self)-> list[bool]:
        return self.blocks

    def set_result(self, result:bool):
        self.result = result

    def get_result(self):
        return 1 if self.result else 0

    def shift(self, q1_value:bool):
        if len(self.blocks) > 1:
            for i in range(len(self.blocks)-1, 0, -1):
                self.blocks[i] = self.blocks[i-1]

            self.blocks[0] = q1_value

    def tick (self, blocks_to_xor: list[int]) -> bool:
        q1_value:bool

        q1_value = self.blocks[blocks_to_xor[0]] if len(blocks_to_xor) == 1 else self.blocks[blocks_to_xor[0]] ^ self.blocks[blocks_to_xor[1]]

        if len(blocks_to_xor) > 2:
            for i in range(2, len(blocks_to_xor)):
                q1_value = q1_value ^ self.blocks[blocks_to_xor[i]]

        self.shift(q1_value)
        self.result = q1_value

        return q1_value






