import queue


class Calculator():
    def __init__(self) -> None:
        self._list = []
        self._should_reset = False

    def push_num(self, num) -> bool:
        if self._should_reset:
            self._list = []
            self._should_reset = False
        if len(self._list) == 0:
            self._list.append(num)
            return True
        last = self._list[-1]
        if isinstance(last, int):
            self._list[-1] = 10 * last + num
        else:
            self._list.append(num)
        return True

    def push_op(self, op) -> bool:
        if self._should_reset:
            self._list = []
            self._should_reset = False
        if len(self._list) == 0:
            return False
        if isinstance(self._list[-1], int):
            self._list.append(op)
            return True
        else:
            return False

    def calc(self) -> bool:
        if not self._valid():
            return False
        # * と / を先に計算
        stack = queue.LifoQueue()
        can_calc = False
        for el in self._list:
            stack.put(el)
            if can_calc:
                num1 = int(stack.get())
                op = stack.get()
                num0 = int(stack.get())
                if op == '*':
                    stack.put(num0 * num1)
                elif op == '/':
                    if num1 == 0:
                        return False
                    else:
                        stack.put(num0 / num1)
                can_calc = False
            if el in ['*', '/']:
                can_calc = True

        # + と - を処理
        list = []
        for _ in range(stack.qsize()):
            list.append(stack.get())
        ans = list.pop()
        while(len(list) > 0):
            op = list.pop()
            num = list.pop()
            if op == '+':
                ans += num
            elif op == '-':
                ans -= num

        self._list = ['ans=', ans]
        self._should_reset = True
        return True

    def expression(self) -> str:
        exp = ''
        for el in self._list:
            exp += str(el)
        return exp if exp != '' else '0'

    def clear(self) -> None:
        self._list = []

    def _valid(self) -> bool:
        if not isinstance(self._list[-1], int):
            return False
        for idx, el in enumerate(self._list):
            if idx % 2 == 0:
                if not isinstance(el, int):
                    return False
            else:
                if el not in ['+', '-', '*', '/']:
                    return False
        return True
