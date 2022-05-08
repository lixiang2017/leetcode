from typing import final

class Base:
    @final
    def done(self) -> None:
        print('done from Base.')


class Sub(Base):
    def done(self) -> None:  # Error reported by type checker
        print('done from Sub')


s = Sub()
s.done()



'''
$ python3 test_final.py
done from Sub
'''