#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Address) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class Address(element.Element):
    """ 
    A
    n
    a
    d
    d
    r
    e
    s
    s
    e
    x
    p
    r
    e
    s
    s
    e
    d
    u
    s
    i
    n
    g
    p
    o
    s
    t
    a
    l
    c
    o
    n
    v
    e
    n
    t
    i
    o
    n
    s
    (
    a
    s
    o
    p
    p
    o
    s
    e
    d
    t
    o
    G
    P
    S
    o
    r
    o
    t
    h
    e
    r
    l
    o
    c
    a
    t
    i
    o
    n
    d
    e
    f
    i
    n
    i
    t
    i
    o
    n
    f
    o
    r
    m
    a
    t
    s
    )
    .
    
    
    A
    n
    a
    d
    d
    r
    e
    s
    s
    e
    x
    p
    r
    e
    s
    s
    e
    d
    u
    s
    i
    n
    g
    p
    o
    s
    t
    a
    l
    c
    o
    n
    v
    e
    n
    t
    i
    o
    n
    s
    (
    a
    s
    o
    p
    p
    o
    s
    e
    d
    t
    o
    G
    P
    S
    o
    r
    o
    t
    h
    e
    r
    l
    o
    c
    a
    t
    i
    o
    n
    d
    e
    f
    i
    n
    i
    t
    i
    o
    n
    f
    o
    r
    m
    a
    t
    s
    )
    .
    T
    h
    i
    s
    d
    a
    t
    a
    t
    y
    p
    e
    m
    a
    y
    b
    e
    u
    s
    e
    d
    t
    o
    c
    o
    n
    v
    e
    y
    a
    d
    d
    r
    e
    s
    s
    e
    s
    f
    o
    r
    u
    s
    e
    i
    n
    d
    e
    l
    i
    v
    e
    r
    i
    n
    g
    m
    a
    i
    l
    a
    s
    w
    e
    l
    l
    a
    s
    f
    o
    r
    v
    i
    s
    i
    t
    i
    n
    g
    l
    o
    c
    a
    t
    i
    o
    n
    s
    w
    h
    i
    c
    h
    m
    i
    g
    h
    t
    n
    o
    t
    b
    e
    v
    a
    l
    i
    d
    f
    o
    r
    m
    a
    i
    l
    d
    e
    l
    i
    v
    e
    r
    y
    .
    T
    h
    e
    r
    e
    a
    r
    e
    a
    v
    a
    r
    i
    e
    t
    y
    o
    f
    p
    o
    s
    t
    a
    l
    a
    d
    d
    r
    e
    s
    s
    f
    o
    r
    m
    a
    t
    s
    d
    e
    f
    i
    n
    e
    d
    a
    r
    o
    u
    n
    d
    t
    h
    e
    w
    o
    r
    l
    d
    .
    
    """
    
    resource_type = "Address"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.city = None
        """ 
        N
        a
        m
        e
        o
        f
        c
        i
        t
        y
        ,
        t
        o
        w
        n
        e
        t
        c
        .
        .
        Type `str`. """
        
        self.country = None
        """ 
        C
        o
        u
        n
        t
        r
        y
        (
        e
        .
        g
        .
        c
        a
        n
        b
        e
        I
        S
        O
        3
        1
        6
        6
        2
        o
        r
        3
        l
        e
        t
        t
        e
        r
        c
        o
        d
        e
        )
        .
        Type `str`. """
        
        self.district = None
        """ 
        D
        i
        s
        t
        r
        i
        c
        t
        n
        a
        m
        e
        (
        a
        k
        a
        c
        o
        u
        n
        t
        y
        )
        .
        Type `str`. """
        
        self.line = None
        """ 
        S
        t
        r
        e
        e
        t
        n
        a
        m
        e
        ,
        n
        u
        m
        b
        e
        r
        ,
        d
        i
        r
        e
        c
        t
        i
        o
        n
        &
        P
        .
        O
        .
        B
        o
        x
        e
        t
        c
        .
        .
        List of `str` items. """
        
        self.period = None
        """ 
        T
        i
        m
        e
        p
        e
        r
        i
        o
        d
        w
        h
        e
        n
        a
        d
        d
        r
        e
        s
        s
        w
        a
        s
        /
        i
        s
        i
        n
        u
        s
        e
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.postalCode = None
        """ 
        P
        o
        s
        t
        a
        l
        c
        o
        d
        e
        f
        o
        r
        a
        r
        e
        a
        .
        Type `str`. """
        
        self.state = None
        """ 
        S
        u
        b
        -
        u
        n
        i
        t
        o
        f
        c
        o
        u
        n
        t
        r
        y
        (
        a
        b
        b
        r
        e
        v
        i
        a
        t
        i
        o
        n
        s
        o
        k
        )
        .
        Type `str`. """
        
        self.text = None
        """ 
        T
        e
        x
        t
        r
        e
        p
        r
        e
        s
        e
        n
        t
        a
        t
        i
        o
        n
        o
        f
        t
        h
        e
        a
        d
        d
        r
        e
        s
        s
        .
        Type `str`. """
        
        self.type = None
        """ 
        p
        o
        s
        t
        a
        l
        |
        p
        h
        y
        s
        i
        c
        a
        l
        |
        b
        o
        t
        h
        .
        Type `str`. """
        
        self.use = None
        """ 
        h
        o
        m
        e
        |
        w
        o
        r
        k
        |
        t
        e
        m
        p
        |
        o
        l
        d
        |
        b
        i
        l
        l
        i
        n
        g
        -
        p
        u
        r
        p
        o
        s
        e
        o
        f
        t
        h
        i
        s
        a
        d
        d
        r
        e
        s
        s
        .
        Type `str`. """
        
        super(Address, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Address, self).elementProperties()
        js.extend([
            ("city", "city", str, False, None, False),
            ("country", "country", str, False, None, False),
            ("district", "district", str, False, None, False),
            ("line", "line", str, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("postalCode", "postalCode", str, False, None, False),
            ("state", "state", str, False, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", str, False, None, False),
            ("use", "use", str, False, None, False),
        ])
        return js


import sys
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
