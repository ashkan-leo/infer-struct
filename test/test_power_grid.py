#!/usr/bin/env python3

from unittest import TestCase

from infer_struct.data import PowerGridSimpleExample


class PowerGridExampleTests(TestCase):
    def test_vectors_and_matrix_shape(self):
        """Test all the vectors and matrices are in proper shape"""

        ns = [9, 14, 30, 39, 57, 68, 118, 145, 300, 2383]
        for n in ns:
            x = PowerGridSimpleExample(n)

            # check vector lengths
            vectors = [x.pl, x.ql, x.pg, x.qg, x.v, x.d]
            for v in vectors:
                self.assertEqual(v.shape, (n,))

            # check matrices shape
            matrices = [x.Ybus_mag, x.Ybus_theta]
            for m in matrices:
                self.assertEqual(m.shape, (n, n))
