import networkx as nx
import numpy as np
from numpy import ndarray
from pandas import DataFrame, read_csv

from .. import util
from ..settings import Settings


class PowerGridSimpleExample:
    """A wrapper class around a dataset of a simple power grid simulation example
    The data is provided by Amir"""

    base_data_path: str = Settings["path"]["power_grid_simple_examples"]

    def __init__(self, node: int):

        self.number_of_nodes = node
        self.example_id = f"{node}_nodes"

        self.pl = self.get_vector("pl")
        self.ql = self.get_vector("ql")

        self.pg = self.get_vector("pg")
        self.qg = self.get_vector("qg")

        self.v = self.get_vector("vs")
        self.d = self.get_vector("ds")

        self.Ybus_theta = self.get_matrix("Ybus_theta")
        self.Ybus_mag = self.get_matrix("Ybus_mag")

        self.Gbus_mag = nx.from_numpy_array(self.Ybus_mag)
        self.Gbus_theta = nx.from_numpy_array(self.Ybus_theta)

    def _get_path(self, arr_name: str) -> str:
        return f"{self.base_data_path}/network_{self.example_id}_{arr_name}.csv"

    def get_vector(self, name: str) -> ndarray:
        """Load a vector by name"""
        vector_path = self._get_path(name)
        vector_df = DataFrame(read_csv(vector_path, header=None))
        ixs = list(map(lambda i: i - 1, vector_df.iloc[:, 0]))
        vals = vector_df.iloc[:, 1]
        return util.create_array(ixs, vals, self.number_of_nodes)

    def get_matrix(self, name: str) -> ndarray:
        """Load a matrix by name. always assumes the first row is missing"""
        matrix_path = self._get_path(name)
        matrix = DataFrame(read_csv(matrix_path, header=None)).to_numpy()
        # NOTE Pad a vector of zero to the top of the matrix
        # TODO verify this is the correct assumption
        # return np.vstack((np.zeros_like(matrix[0]), matrix))
        return matrix
