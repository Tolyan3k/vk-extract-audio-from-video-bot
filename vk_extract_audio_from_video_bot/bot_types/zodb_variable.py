"""TODO."""

import ZODB


class ZodbVariable:
    """TODO."""

    def __init__(self, zodb_db: ZODB.DB, var_name: str) -> None:
        """TODO.

        Args:
        ----
            zodb_db (ZODB.DB): _description_
            var_name (str): _description_

        """
        self._zodb_db: ZODB.DB = zodb_db
        self._var_name: str = var_name

    # Methods
    def set_value(self, value: object) -> None:
        """TODO.

        Args:
        ----
            value (_type_): _description_

        """
        with self._zodb_db.transaction() as conn:
            conn.root()[self._var_name] = value

    def get_value(self) -> object:
        """TODO.

        Returns
        -------
            _type_: _description_

        """
        with self._zodb_db.transaction() as conn:
            return conn.root()[self._var_name]

    def exist(self) -> bool:
        """TODO.

        Returns
        -------
            _type_: _description_

        """
        with self._zodb_db.transaction() as conn:
            if self._var_name in conn.root():
                return True
            return False

    # ================================================
    def __repr__(self) -> str:
        return self.get_value().__repr__()

    def __str__(self) -> str:
        return self.get_value().__str__()

    # Binary operators
    def __add__(self, rhs) -> object:
        return self.get_value().__add__(rhs)

    def __sub__(self, rhs) -> object:
        return self.get_value().__sub__(rhs)

    def __mul__(self, rhs) -> object:
        return self.get_value().__mul__(rhs)

    def __truediv__(self, rhs) -> object:
        return self.get_value().__truediv__(rhs)

    def __floordiv__(self, rhs) -> object:
        return self.get_value().__floordiv__(rhs)

    def __mod__(self, rhs) -> object:
        return self.get_value().__mod__(rhs)

    def __pow__(self, rhs) -> object:
        return self.get_value().__pow__(rhs)

    def __rshift__(self, rhs) -> object:
        return self.get_value().__rshift__(rhs)

    def __lshift__(self, rhs) -> object:
        return self.get_value().__lshift__(rhs)

    def __and__(self, rhs) -> object:
        return self.get_value().__and__(rhs)

    def __or__(self, rhs) -> object:
        return self.get_value().__or__(rhs)

    def __xor__(self, rhs) -> object:
        return self.get_value().__xor__(rhs)

    # Comparison operators
    def __lt__(self, rhs) -> object:
        return self.get_value().__lt__(rhs)

    def __gt__(self, rhs) -> object:
        return self.get_value().__gt__(rhs)

    def __le__(self, rhs) -> object:
        return self.get_value().__le__(rhs)

    def __ge__(self, rhs) -> object:
        return self.get_value().__ge__(rhs)

    def __eq__(self, rhs) -> object:
        return self.get_value().__eq__(rhs)

    def __ne__(self, rhs) -> object:
        return self.get_value().__ne__(rhs)

    # Unary operators
    def __isub__(self, rhs):
        with self._zodb_db.transaction() as conn:
            conn.root()[self._var_name].__isub__(rhs)
        return self

    def __iadd__(self, rhs):
        with self._zodb_db.transaction() as conn:
            conn.root()[self._var_name].__iadd__(rhs)
        return self

    def __imul__(self, rhs):
        with self._zodb_db.transaction() as conn:
            conn.root()[self._var_name].__imul__(rhs)
        return self

    def __idiv__(self, rhs) -> object:
        with self._zodb_db.transaction() as conn:
            conn.root()[self._var_name].__idiv__(rhs)

        return self


# ...
