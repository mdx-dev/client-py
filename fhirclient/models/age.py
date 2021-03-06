#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Age) on 2019-01-22.
#  2019, SMART Health IT.


from . import quantity

class Age(quantity.Quantity):
    """ 
    A
    d
    u
    r
    a
    t
    i
    o
    n
    o
    f
    t
    i
    m
    e
    d
    u
    r
    i
    n
    g
    w
    h
    i
    c
    h
    a
    n
    o
    r
    g
    a
    n
    i
    s
    m
    (
    o
    r
    a
    p
    r
    o
    c
    e
    s
    s
    )
    h
    a
    s
    e
    x
    i
    s
    t
    e
    d
    .
    """
    
    resource_type = "Age"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        super(Age, self).__init__(jsondict=jsondict, strict=strict)


