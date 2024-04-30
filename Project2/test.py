import pytest
from aScript import maintenanceLINUX, mis_a_jour_systemLINUX, verifier_integriteLINUX

def mis_a_jour_systemLINUXShouldReturnErreur():
    assert mis_a_jour_systemLINUX() == ""

def maintenanceLINUXShouldReturn():
    assert maintenanceLINUX() == ""

def verifier_integriteLINUXShouldReturnError():
    assert verifier_integriteLINUX() == ""