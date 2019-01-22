#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ProdCharacteristic) on 2019-01-22.
#  2019, SMART Health IT.


from . import backboneelement

class ProdCharacteristic(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    m
    a
    r
    k
    e
    t
    i
    n
    g
    s
    t
    a
    t
    u
    s
    d
    e
    s
    c
    r
    i
    b
    e
    s
    t
    h
    e
    d
    a
    t
    e
    w
    h
    e
    n
    a
    m
    e
    d
    i
    c
    i
    n
    a
    l
    p
    r
    o
    d
    u
    c
    t
    i
    s
    a
    c
    t
    u
    a
    l
    l
    y
    p
    u
    t
    o
    n
    t
    h
    e
    m
    a
    r
    k
    e
    t
    o
    r
    t
    h
    e
    d
    a
    t
    e
    a
    s
    o
    f
    w
    h
    i
    c
    h
    i
    t
    i
    s
    n
    o
    l
    o
    n
    g
    e
    r
    a
    v
    a
    i
    l
    a
    b
    l
    e
    .
    """
    
    resource_type = "ProdCharacteristic"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.color = None
        """ 
        W
        h
        e
        r
        e
        a
        p
        p
        l
        i
        c
        a
        b
        l
        e
        ,
        t
        h
        e
        c
        o
        l
        o
        r
        c
        a
        n
        b
        e
        s
        p
        e
        c
        i
        f
        i
        e
        d
        A
        n
        a
        p
        p
        r
        o
        p
        r
        i
        a
        t
        e
        c
        o
        n
        t
        r
        o
        l
        l
        e
        d
        v
        o
        c
        a
        b
        u
        l
        a
        r
        y
        s
        h
        a
        l
        l
        b
        e
        u
        s
        e
        d
        T
        h
        e
        t
        e
        r
        m
        a
        n
        d
        t
        h
        e
        t
        e
        r
        m
        i
        d
        e
        n
        t
        i
        f
        i
        e
        r
        s
        h
        a
        l
        l
        b
        e
        u
        s
        e
        d
        .
        List of `str` items. """
        
        self.depth = None
        """ 
        W
        h
        e
        r
        e
        a
        p
        p
        l
        i
        c
        a
        b
        l
        e
        ,
        t
        h
        e
        d
        e
        p
        t
        h
        c
        a
        n
        b
        e
        s
        p
        e
        c
        i
        f
        i
        e
        d
        u
        s
        i
        n
        g
        a
        n
        u
        m
        e
        r
        i
        c
        a
        l
        v
        a
        l
        u
        e
        a
        n
        d
        i
        t
        s
        u
        n
        i
        t
        o
        f
        m
        e
        a
        s
        u
        r
        e
        m
        e
        n
        t
        T
        h
        e
        u
        n
        i
        t
        o
        f
        m
        e
        a
        s
        u
        r
        e
        m
        e
        n
        t
        s
        h
        a
        l
        l
        b
        e
        s
        p
        e
        c
        i
        f
        i
        e
        d
        i
        n
        a
        c
        c
        o
        r
        d
        a
        n
        c
        e
        w
        i
        t
        h
        I
        S
        O
        1
        1
        2
        4
        0
        a
        n
        d
        t
        h
        e
        r
        e
        s
        u
        l
        t
        i
        n
        g
        t
        e
        r
        m
        i
        n
        o
        l
        o
        g
        y
        T
        h
        e
        s
        y
        m
        b
        o
        l
        a
        n
        d
        t
        h
        e
        s
        y
        m
        b
        o
        l
        i
        d
        e
        n
        t
        i
        f
        i
        e
        r
        s
        h
        a
        l
        l
        b
        e
        u
        s
        e
        d
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.externalDiameter = None
        """ 
        W
        h
        e
        r
        e
        a
        p
        p
        l
        i
        c
        a
        b
        l
        e
        ,
        t
        h
        e
        e
        x
        t
        e
        r
        n
        a
        l
        d
        i
        a
        m
        e
        t
        e
        r
        c
        a
        n
        b
        e
        s
        p
        e
        c
        i
        f
        i
        e
        d
        u
        s
        i
        n
        g
        a
        n
        u
        m
        e
        r
        i
        c
        a
        l
        v
        a
        l
        u
        e
        a
        n
        d
        i
        t
        s
        u
        n
        i
        t
        o
        f
        m
        e
        a
        s
        u
        r
        e
        m
        e
        n
        t
        T
        h
        e
        u
        n
        i
        t
        o
        f
        m
        e
        a
        s
        u
        r
        e
        m
        e
        n
        t
        s
        h
        a
        l
        l
        b
        e
        s
        p
        e
        c
        i
        f
        i
        e
        d
        i
        n
        a
        c
        c
        o
        r
        d
        a
        n
        c
        e
        w
        i
        t
        h
        I
        S
        O
        1
        1
        2
        4
        0
        a
        n
        d
        t
        h
        e
        r
        e
        s
        u
        l
        t
        i
        n
        g
        t
        e
        r
        m
        i
        n
        o
        l
        o
        g
        y
        T
        h
        e
        s
        y
        m
        b
        o
        l
        a
        n
        d
        t
        h
        e
        s
        y
        m
        b
        o
        l
        i
        d
        e
        n
        t
        i
        f
        i
        e
        r
        s
        h
        a
        l
        l
        b
        e
        u
        s
        e
        d
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.height = None
        """ 
        W
        h
        e
        r
        e
        a
        p
        p
        l
        i
        c
        a
        b
        l
        e
        ,
        t
        h
        e
        h
        e
        i
        g
        h
        t
        c
        a
        n
        b
        e
        s
        p
        e
        c
        i
        f
        i
        e
        d
        u
        s
        i
        n
        g
        a
        n
        u
        m
        e
        r
        i
        c
        a
        l
        v
        a
        l
        u
        e
        a
        n
        d
        i
        t
        s
        u
        n
        i
        t
        o
        f
        m
        e
        a
        s
        u
        r
        e
        m
        e
        n
        t
        T
        h
        e
        u
        n
        i
        t
        o
        f
        m
        e
        a
        s
        u
        r
        e
        m
        e
        n
        t
        s
        h
        a
        l
        l
        b
        e
        s
        p
        e
        c
        i
        f
        i
        e
        d
        i
        n
        a
        c
        c
        o
        r
        d
        a
        n
        c
        e
        w
        i
        t
        h
        I
        S
        O
        1
        1
        2
        4
        0
        a
        n
        d
        t
        h
        e
        r
        e
        s
        u
        l
        t
        i
        n
        g
        t
        e
        r
        m
        i
        n
        o
        l
        o
        g
        y
        T
        h
        e
        s
        y
        m
        b
        o
        l
        a
        n
        d
        t
        h
        e
        s
        y
        m
        b
        o
        l
        i
        d
        e
        n
        t
        i
        f
        i
        e
        r
        s
        h
        a
        l
        l
        b
        e
        u
        s
        e
        d
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.image = None
        """ 
        W
        h
        e
        r
        e
        a
        p
        p
        l
        i
        c
        a
        b
        l
        e
        ,
        t
        h
        e
        i
        m
        a
        g
        e
        c
        a
        n
        b
        e
        p
        r
        o
        v
        i
        d
        e
        d
        T
        h
        e
        f
        o
        r
        m
        a
        t
        o
        f
        t
        h
        e
        i
        m
        a
        g
        e
        a
        t
        t
        a
        c
        h
        m
        e
        n
        t
        s
        h
        a
        l
        l
        b
        e
        s
        p
        e
        c
        i
        f
        i
        e
        d
        b
        y
        r
        e
        g
        i
        o
        n
        a
        l
        i
        m
        p
        l
        e
        m
        e
        n
        t
        a
        t
        i
        o
        n
        s
        .
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.imprint = None
        """ 
        W
        h
        e
        r
        e
        a
        p
        p
        l
        i
        c
        a
        b
        l
        e
        ,
        t
        h
        e
        i
        m
        p
        r
        i
        n
        t
        c
        a
        n
        b
        e
        s
        p
        e
        c
        i
        f
        i
        e
        d
        a
        s
        t
        e
        x
        t
        .
        List of `str` items. """
        
        self.nominalVolume = None
        """ 
        W
        h
        e
        r
        e
        a
        p
        p
        l
        i
        c
        a
        b
        l
        e
        ,
        t
        h
        e
        n
        o
        m
        i
        n
        a
        l
        v
        o
        l
        u
        m
        e
        c
        a
        n
        b
        e
        s
        p
        e
        c
        i
        f
        i
        e
        d
        u
        s
        i
        n
        g
        a
        n
        u
        m
        e
        r
        i
        c
        a
        l
        v
        a
        l
        u
        e
        a
        n
        d
        i
        t
        s
        u
        n
        i
        t
        o
        f
        m
        e
        a
        s
        u
        r
        e
        m
        e
        n
        t
        T
        h
        e
        u
        n
        i
        t
        o
        f
        m
        e
        a
        s
        u
        r
        e
        m
        e
        n
        t
        s
        h
        a
        l
        l
        b
        e
        s
        p
        e
        c
        i
        f
        i
        e
        d
        i
        n
        a
        c
        c
        o
        r
        d
        a
        n
        c
        e
        w
        i
        t
        h
        I
        S
        O
        1
        1
        2
        4
        0
        a
        n
        d
        t
        h
        e
        r
        e
        s
        u
        l
        t
        i
        n
        g
        t
        e
        r
        m
        i
        n
        o
        l
        o
        g
        y
        T
        h
        e
        s
        y
        m
        b
        o
        l
        a
        n
        d
        t
        h
        e
        s
        y
        m
        b
        o
        l
        i
        d
        e
        n
        t
        i
        f
        i
        e
        r
        s
        h
        a
        l
        l
        b
        e
        u
        s
        e
        d
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.scoring = None
        """ 
        W
        h
        e
        r
        e
        a
        p
        p
        l
        i
        c
        a
        b
        l
        e
        ,
        t
        h
        e
        s
        c
        o
        r
        i
        n
        g
        c
        a
        n
        b
        e
        s
        p
        e
        c
        i
        f
        i
        e
        d
        A
        n
        a
        p
        p
        r
        o
        p
        r
        i
        a
        t
        e
        c
        o
        n
        t
        r
        o
        l
        l
        e
        d
        v
        o
        c
        a
        b
        u
        l
        a
        r
        y
        s
        h
        a
        l
        l
        b
        e
        u
        s
        e
        d
        T
        h
        e
        t
        e
        r
        m
        a
        n
        d
        t
        h
        e
        t
        e
        r
        m
        i
        d
        e
        n
        t
        i
        f
        i
        e
        r
        s
        h
        a
        l
        l
        b
        e
        u
        s
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.shape = None
        """ 
        W
        h
        e
        r
        e
        a
        p
        p
        l
        i
        c
        a
        b
        l
        e
        ,
        t
        h
        e
        s
        h
        a
        p
        e
        c
        a
        n
        b
        e
        s
        p
        e
        c
        i
        f
        i
        e
        d
        A
        n
        a
        p
        p
        r
        o
        p
        r
        i
        a
        t
        e
        c
        o
        n
        t
        r
        o
        l
        l
        e
        d
        v
        o
        c
        a
        b
        u
        l
        a
        r
        y
        s
        h
        a
        l
        l
        b
        e
        u
        s
        e
        d
        T
        h
        e
        t
        e
        r
        m
        a
        n
        d
        t
        h
        e
        t
        e
        r
        m
        i
        d
        e
        n
        t
        i
        f
        i
        e
        r
        s
        h
        a
        l
        l
        b
        e
        u
        s
        e
        d
        .
        Type `str`. """
        
        self.weight = None
        """ 
        W
        h
        e
        r
        e
        a
        p
        p
        l
        i
        c
        a
        b
        l
        e
        ,
        t
        h
        e
        w
        e
        i
        g
        h
        t
        c
        a
        n
        b
        e
        s
        p
        e
        c
        i
        f
        i
        e
        d
        u
        s
        i
        n
        g
        a
        n
        u
        m
        e
        r
        i
        c
        a
        l
        v
        a
        l
        u
        e
        a
        n
        d
        i
        t
        s
        u
        n
        i
        t
        o
        f
        m
        e
        a
        s
        u
        r
        e
        m
        e
        n
        t
        T
        h
        e
        u
        n
        i
        t
        o
        f
        m
        e
        a
        s
        u
        r
        e
        m
        e
        n
        t
        s
        h
        a
        l
        l
        b
        e
        s
        p
        e
        c
        i
        f
        i
        e
        d
        i
        n
        a
        c
        c
        o
        r
        d
        a
        n
        c
        e
        w
        i
        t
        h
        I
        S
        O
        1
        1
        2
        4
        0
        a
        n
        d
        t
        h
        e
        r
        e
        s
        u
        l
        t
        i
        n
        g
        t
        e
        r
        m
        i
        n
        o
        l
        o
        g
        y
        T
        h
        e
        s
        y
        m
        b
        o
        l
        a
        n
        d
        t
        h
        e
        s
        y
        m
        b
        o
        l
        i
        d
        e
        n
        t
        i
        f
        i
        e
        r
        s
        h
        a
        l
        l
        b
        e
        u
        s
        e
        d
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.width = None
        """ 
        W
        h
        e
        r
        e
        a
        p
        p
        l
        i
        c
        a
        b
        l
        e
        ,
        t
        h
        e
        w
        i
        d
        t
        h
        c
        a
        n
        b
        e
        s
        p
        e
        c
        i
        f
        i
        e
        d
        u
        s
        i
        n
        g
        a
        n
        u
        m
        e
        r
        i
        c
        a
        l
        v
        a
        l
        u
        e
        a
        n
        d
        i
        t
        s
        u
        n
        i
        t
        o
        f
        m
        e
        a
        s
        u
        r
        e
        m
        e
        n
        t
        T
        h
        e
        u
        n
        i
        t
        o
        f
        m
        e
        a
        s
        u
        r
        e
        m
        e
        n
        t
        s
        h
        a
        l
        l
        b
        e
        s
        p
        e
        c
        i
        f
        i
        e
        d
        i
        n
        a
        c
        c
        o
        r
        d
        a
        n
        c
        e
        w
        i
        t
        h
        I
        S
        O
        1
        1
        2
        4
        0
        a
        n
        d
        t
        h
        e
        r
        e
        s
        u
        l
        t
        i
        n
        g
        t
        e
        r
        m
        i
        n
        o
        l
        o
        g
        y
        T
        h
        e
        s
        y
        m
        b
        o
        l
        a
        n
        d
        t
        h
        e
        s
        y
        m
        b
        o
        l
        i
        d
        e
        n
        t
        i
        f
        i
        e
        r
        s
        h
        a
        l
        l
        b
        e
        u
        s
        e
        d
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(ProdCharacteristic, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProdCharacteristic, self).elementProperties()
        js.extend([
            ("color", "color", str, True, None, False),
            ("depth", "depth", quantity.Quantity, False, None, False),
            ("externalDiameter", "externalDiameter", quantity.Quantity, False, None, False),
            ("height", "height", quantity.Quantity, False, None, False),
            ("image", "image", attachment.Attachment, True, None, False),
            ("imprint", "imprint", str, True, None, False),
            ("nominalVolume", "nominalVolume", quantity.Quantity, False, None, False),
            ("scoring", "scoring", codeableconcept.CodeableConcept, False, None, False),
            ("shape", "shape", str, False, None, False),
            ("weight", "weight", quantity.Quantity, False, None, False),
            ("width", "width", quantity.Quantity, False, None, False),
        ])
        return js


import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
