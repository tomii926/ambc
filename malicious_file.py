import hashlib
import os


class MaliciousFile:
    """不正なファイルのファイル名を格納"""

    def __init__(self, filepath):
        self.filepath = filepath

    def md5sum(self):
        """md5チェックサムを計算し、16真数表記の文字列を返す"""

        with open(self.filepath, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()

    def __eq__(self, other):
        """ ==演算の結果を返す。

        ハッシュ可能オブジェクトとして利用するには__eq__も必要らしい。
        """
        return self.md5sum() == other.md5sum()

    def __hash__(self):
        """hash値を整数で返す。

        __hash__メソッドは返り値が整数であることを要求する
        """
        return int(self.md5sum(), 16)

    def fullpath(self):
        return os.path.abspath(self.filepath)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.filepath})"


if __name__ == "__main__":
    a = MaliciousFile("binaries/curl.sh")
    b = MaliciousFile("binaries/sleep.sh")
    c = MaliciousFile("./binaries/curl2.sh")

    l = [a,b,c]
    print(set(l))
    print(a.md5sum())
    print(a.__hash__())
