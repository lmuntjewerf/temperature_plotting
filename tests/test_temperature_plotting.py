#!/usr/bin/env python
# coding: utf-8


import pytest, os

import temperature_plotting as tpl 



def test_compute_mean():
    calc = tpl.compute_mean([0,10,20])
    assert calc == 10
    assert type(calc) == float
    
    calc = tpl.compute_mean([-10,10])
    assert calc == 0
    
    calc = tpl.compute_mean([0,10,0])
    assert round(calc,4) == 3.3333, "Check that the average is roughtly correct."
    
    with pytest.raises(TypeError):
        calc = tpl.compute_mean(["a","b","c"])
        #calc = tpl.compute_mean([0,10,0])   # --> Failed: DID NOT RAISE <class 'TypeError'>
    
    calc = tpl.compute_mean([])
    assert calc == None
    
    with pytest.raises(TypeError) as e:
        calc = tpl.compute_mean(["a","b","c"])
    assert not e == None, " We are not able to average strings"
    
    
        


def test_create_name():
    name = tpl.create_name(1)
    assert name == 'plot_1.png'
    
    with pytest.raises(TypeError):
        name = tpl.create_name("a")




def test_main():
    tpl.main()



