# -*- coding: utf-8 -*-

import pickle

import numpy as np


class DataHandler:
    """
    Read data as created by preprocessor scripts and handle basic array
    manipulations.

    """
    def __init__(self, ic, exp, weights=np.ones(3), datadir='../data'):
        with open('{}/model/{}.pkl'.format(datadir, ic), 'rb') as f:
            self.__dict__.update(pickle.load(f))

        with open('{}/exp/{}.pkl'.format(datadir, exp), 'rb') as f:
            self._exp = pickle.load(f)

        obs = self.mult, self.v2, self.v3
        self._nobs = len(obs)
        self._ncent = obs[0].shape[1]
        assert all(i.shape[1] == self._ncent for i in obs)
        assert all(self._exp[i]['mean'].size == self._ncent
                   for i in ('mult', 'v2', 'v3'))

        weights = np.asarray(weights, dtype=float)
        assert weights.size == self._nobs
        self._weights = weights.repeat(self._ncent)

    @property
    def ndim(self):
        """
        Number of input dimensions.

        """
        return self.design.shape[1]

    @property
    def nfeatures(self):
        """
        Number of outputs.

        """
        return self._nobs * self._ncent

    @property
    def exp_data(self):
        """
        Experimental data (mult, v2, v3).

        """
        mult, v2, v3 = (self._exp[i]['mean'] for i in ('mult', 'v2', 'v3'))
        return self._concat(mult, v2, v3)

    @property
    def cal_data(self):
        """
        Calibration data.

        """
        return self._weights

    @property
    def training_data(self):
        """
        Full matrix of training data (mult, v2, v3).

        Preprocessing:
            - Square root of mult.
            - Apply weights.
            - Scale by experimental data.

        """
        data = self._concat(self.mult, self.v2, self.v3)
        data *= self._weights / self.exp_data
        return data

    @staticmethod
    def _concat(mult, v2, v3):
        """
        Take square root of mult and concatenate rows.

        """
        return np.hstack((np.sqrt(mult), v2, v3))

    def unpack(self, y, std=None):
        """
        Separate a full matrix into a dict of (mult, v2, v3) and invert
        preprocessing steps from self.training_data.

        """
        y = y * self.exp_data / self._weights
        sqrt_mult, v2, v3 = np.hsplit(y, 3)
        mult = np.square(sqrt_mult)

        if std is None:
            return dict(mult=mult, v2=v2, v3=v3)
        else:
            std = std * self.exp_data / self._weights
            sqrt_mult_std, v2_std, v3_std = np.hsplit(std, 3)
            mult_std = 2. * sqrt_mult_std * sqrt_mult
            return dict(
                mult={'mean': mult, 'std': mult_std},
                v2={'mean': v2, 'std': v2_std},
                v3={'mean': v3, 'std': v3_std}
            )
