import sys
from json import dumps as jdumps
from pathlib import Path
from time import time
import dask.dataframe as dd
import itertools

PWD = Path(__file__).resolve().parent.parent


class Benchmark:
    reader: str
    dpath: Path

    def __init__(self):
        self.reader = sys.argv[1]
        self.dpath = PWD / "data" / sys.argv[2]

    def init(self):
        pass

    def run(self) -> None:
        self.init()
        then = time()
        self.bench()
        elapsed = time() - then
        result = {"name": self.__class__.__name__, "elapsed": elapsed}
        print(jdumps(result))

    def bench(self) -> None:
        pass


class BenchmarkX:
    reader: str
    dpath: Path

    def __init__(self):
        self.reader = sys.argv[1]
        self.dpath = PWD / "data" / sys.argv[2]

    def init(self):
        pass

    def run(self) -> None:
        self.init()
        if self.dpath.suffix == ".parquet":
            df = dd.read_parquet(self.dpath)
        elif self.dpath.suffix == ".csv":
            df = dd.read_csv(self.dpath)

        times = []
        cols = []
        for col in df.columns:
            then = time()
            self.bench(col)
            times.append(time() - then)
            cols.append(col)

        result = {"name": self.__class__.__name__, "times": times, "columns": cols}
        print(jdumps(result))

    def bench(self) -> None:
        pass


class BenchmarkCorrX:
    reader: str
    dpath: Path

    def __init__(self):
        self.reader = sys.argv[1]
        self.dpath = PWD / "data" / sys.argv[2]

    def init(self):
        pass

    def run(self) -> None:
        self.init()
        if self.dpath.suffix == ".parquet":
            df = dd.read_parquet(self.dpath)
        elif self.dpath.suffix == ".csv":
            df = dd.read_csv(self.dpath)

        df = df.select_dtypes(include="number")
        times = []
        cols = []
        for col in df.columns:
            then = time()
            self.bench(col)
            times.append(time() - then)
            cols.append(col)

        result = {"name": self.__class__.__name__, "times": times, "columns": cols}
        print(jdumps(result))

    def bench(self) -> None:
        pass


class BenchmarkXY:
    reader: str
    dpath: Path

    def __init__(self):
        self.reader = sys.argv[1]
        self.dpath = PWD / "data" / sys.argv[2]

    def init(self):
        pass

    def run(self) -> None:
        self.init()
        if self.dpath.suffix == ".parquet":
            df = dd.read_parquet(self.dpath)
        elif self.dpath.suffix == ".csv":
            df = dd.read_csv(self.dpath)

        df_cat = df.select_dtypes(object)
        cols = []
        for x in df.columns:
            if x in df_cat.columns:
                nuniq = df[x].nunique().compute()
                if nuniq <= 100:
                    cols.append(x)
            else:
                cols.append(x)
        times = []
        col_pairs = []
        for x, y in itertools.combinations(cols, 2):
            then = time()
            self.bench(x, y)
            times.append(time() - then)
            col_pairs.append((x, y))

        result = {
            "name": self.__class__.__name__,
            "times": times,
            "column_pairs": col_pairs,
            "all_columns": cols,
        }
        print(jdumps(result))

    def bench(self) -> None:
        pass


class BenchmarkCorrXY:
    reader: str
    dpath: Path

    def __init__(self):
        self.reader = sys.argv[1]
        self.dpath = PWD / "data" / sys.argv[2]

    def init(self):
        pass

    def run(self) -> None:
        self.init()
        if self.dpath.suffix == ".parquet":
            df = dd.read_parquet(self.dpath)
        elif self.dpath.suffix == ".csv":
            df = dd.read_csv(self.dpath)

        df = df.select_dtypes(include="number")
        cols = []
        for x in df.columns:
            cols.append(x)
        times = []
        col_pairs = []
        for x, y in itertools.combinations(cols, 2):
            then = time()
            self.bench(x, y)
            times.append(time() - then)
            col_pairs.append((x, y))

        result = {
            "name": self.__class__.__name__,
            "times": times,
            "column_pairs": col_pairs,
            "all_columns": cols,
        }
        print(jdumps(result))

    def bench(self) -> None:
        pass


class BenchmarkMissXY:
    reader: str
    dpath: Path

    def __init__(self):
        self.reader = sys.argv[1]
        self.dpath = PWD / "data" / sys.argv[2]

    def init(self):
        pass

    def run(self) -> None:
        self.init()
        if self.dpath.suffix == ".parquet":
            df = dd.read_parquet(self.dpath)
        elif self.dpath.suffix == ".csv":
            df = dd.read_csv(self.dpath)

        cols = []
        for x in df.columns:
            cols.append(x)
        times = []
        col_pairs = []
        for x, y in itertools.combinations(cols, 2):
            then = time()
            self.bench(x, y)
            times.append(time() - then)
            col_pairs.append((x, y))

        result = {
            "name": self.__class__.__name__,
            "times": times,
            "column_pairs": col_pairs,
            "all_columns": cols,
        }
        print(jdumps(result))

    def bench(self) -> None:
        pass
