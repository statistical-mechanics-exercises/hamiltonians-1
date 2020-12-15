import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_eng(self) : 
        for i in range(2**5) :
            num, spins = i, 5*[0]
            for j in range(5) :
                spins[j] = np.floor( num / 2**(4-j) )
                num = num - spins[j]*2**(4-j)
                if spins[j]==0 : spins[j] = -1
            sumspins = sum( spins )
            self.assertTrue( hamiltonian( spins, 1)==-sumspins, "Hamiltonian gives the wrong value for the energy" )
