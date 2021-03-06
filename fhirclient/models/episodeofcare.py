#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/EpisodeOfCare) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class EpisodeOfCare(domainresource.DomainResource):
    """ 
    A
    n
    a
    s
    s
    o
    c
    i
    a
    t
    i
    o
    n
    o
    f
    a
    P
    a
    t
    i
    e
    n
    t
    w
    i
    t
    h
    a
    n
    O
    r
    g
    a
    n
    i
    z
    a
    t
    i
    o
    n
    a
    n
    d
    H
    e
    a
    l
    t
    h
    c
    a
    r
    e
    P
    r
    o
    v
    i
    d
    e
    r
    (
    s
    )
    f
    o
    r
    a
    p
    e
    r
    i
    o
    d
    o
    f
    t
    i
    m
    e
    t
    h
    a
    t
    t
    h
    e
    O
    r
    g
    a
    n
    i
    z
    a
    t
    i
    o
    n
    a
    s
    s
    u
    m
    e
    s
    s
    o
    m
    e
    l
    e
    v
    e
    l
    o
    f
    r
    e
    s
    p
    o
    n
    s
    i
    b
    i
    l
    i
    t
    y
    .
    
    
    A
    n
    a
    s
    s
    o
    c
    i
    a
    t
    i
    o
    n
    b
    e
    t
    w
    e
    e
    n
    a
    p
    a
    t
    i
    e
    n
    t
    a
    n
    d
    a
    n
    o
    r
    g
    a
    n
    i
    z
    a
    t
    i
    o
    n
    /
    h
    e
    a
    l
    t
    h
    c
    a
    r
    e
    p
    r
    o
    v
    i
    d
    e
    r
    (
    s
    )
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
    t
    i
    m
    e
    e
    n
    c
    o
    u
    n
    t
    e
    r
    s
    m
    a
    y
    o
    c
    c
    u
    r
    .
    T
    h
    e
    m
    a
    n
    a
    g
    i
    n
    g
    o
    r
    g
    a
    n
    i
    z
    a
    t
    i
    o
    n
    a
    s
    s
    u
    m
    e
    s
    a
    l
    e
    v
    e
    l
    o
    f
    r
    e
    s
    p
    o
    n
    s
    i
    b
    i
    l
    i
    t
    y
    f
    o
    r
    t
    h
    e
    p
    a
    t
    i
    e
    n
    t
    d
    u
    r
    i
    n
    g
    t
    h
    i
    s
    t
    i
    m
    e
    .
    
    """
    
    resource_type = "EpisodeOfCare"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.account = None
        """ 
        T
        h
        e
        s
        e
        t
        o
        f
        a
        c
        c
        o
        u
        n
        t
        s
        t
        h
        a
        t
        m
        a
        y
        b
        e
        u
        s
        e
        d
        f
        o
        r
        b
        i
        l
        l
        i
        n
        g
        f
        o
        r
        t
        h
        i
        s
        E
        p
        i
        s
        o
        d
        e
        O
        f
        C
        a
        r
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.careManager = None
        """ 
        C
        a
        r
        e
        m
        a
        n
        a
        g
        e
        r
        /
        c
        a
        r
        e
        c
        o
        o
        r
        d
        i
        n
        a
        t
        o
        r
        f
        o
        r
        t
        h
        e
        p
        a
        t
        i
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.diagnosis = None
        """ 
        T
        h
        e
        l
        i
        s
        t
        o
        f
        d
        i
        a
        g
        n
        o
        s
        i
        s
        r
        e
        l
        e
        v
        a
        n
        t
        t
        o
        t
        h
        i
        s
        e
        p
        i
        s
        o
        d
        e
        o
        f
        c
        a
        r
        e
        .
        List of `EpisodeOfCareDiagnosis` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        B
        u
        s
        i
        n
        e
        s
        s
        I
        d
        e
        n
        t
        i
        f
        i
        e
        r
        (
        s
        )
        r
        e
        l
        e
        v
        a
        n
        t
        f
        o
        r
        t
        h
        i
        s
        E
        p
        i
        s
        o
        d
        e
        O
        f
        C
        a
        r
        e
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.managingOrganization = None
        """ 
        O
        r
        g
        a
        n
        i
        z
        a
        t
        i
        o
        n
        t
        h
        a
        t
        a
        s
        s
        u
        m
        e
        s
        c
        a
        r
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.patient = None
        """ 
        T
        h
        e
        p
        a
        t
        i
        e
        n
        t
        w
        h
        o
        i
        s
        t
        h
        e
        f
        o
        c
        u
        s
        o
        f
        t
        h
        i
        s
        e
        p
        i
        s
        o
        d
        e
        o
        f
        c
        a
        r
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ 
        I
        n
        t
        e
        r
        v
        a
        l
        d
        u
        r
        i
        n
        g
        r
        e
        s
        p
        o
        n
        s
        i
        b
        i
        l
        i
        t
        y
        i
        s
        a
        s
        s
        u
        m
        e
        d
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.referralRequest = None
        """ 
        O
        r
        i
        g
        i
        n
        a
        t
        i
        n
        g
        R
        e
        f
        e
        r
        r
        a
        l
        R
        e
        q
        u
        e
        s
        t
        (
        s
        )
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        p
        l
        a
        n
        n
        e
        d
        |
        w
        a
        i
        t
        l
        i
        s
        t
        |
        a
        c
        t
        i
        v
        e
        |
        o
        n
        h
        o
        l
        d
        |
        f
        i
        n
        i
        s
        h
        e
        d
        |
        c
        a
        n
        c
        e
        l
        l
        e
        d
        |
        e
        n
        t
        e
        r
        e
        d
        -
        i
        n
        -
        e
        r
        r
        o
        r
        .
        Type `str`. """
        
        self.statusHistory = None
        """ 
        P
        a
        s
        t
        l
        i
        s
        t
        o
        f
        s
        t
        a
        t
        u
        s
        c
        o
        d
        e
        s
        (
        t
        h
        e
        c
        u
        r
        r
        e
        n
        t
        s
        t
        a
        t
        u
        s
        m
        a
        y
        b
        e
        i
        n
        c
        l
        u
        d
        e
        d
        t
        o
        c
        o
        v
        e
        r
        t
        h
        e
        s
        t
        a
        r
        t
        d
        a
        t
        e
        o
        f
        t
        h
        e
        s
        t
        a
        t
        u
        s
        )
        .
        List of `EpisodeOfCareStatusHistory` items (represented as `dict` in JSON). """
        
        self.team = None
        """ 
        O
        t
        h
        e
        r
        p
        r
        a
        c
        t
        i
        t
        i
        o
        n
        e
        r
        s
        f
        a
        c
        i
        l
        i
        t
        a
        t
        i
        n
        g
        t
        h
        i
        s
        e
        p
        i
        s
        o
        d
        e
        o
        f
        c
        a
        r
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        y
        p
        e
        /
        c
        l
        a
        s
        s
        -
        e
        .
        g
        .
        s
        p
        e
        c
        i
        a
        l
        i
        s
        t
        r
        e
        f
        e
        r
        r
        a
        l
        ,
        d
        i
        s
        e
        a
        s
        e
        m
        a
        n
        a
        g
        e
        m
        e
        n
        t
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(EpisodeOfCare, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EpisodeOfCare, self).elementProperties()
        js.extend([
            ("account", "account", fhirreference.FHIRReference, True, None, False),
            ("careManager", "careManager", fhirreference.FHIRReference, False, None, False),
            ("diagnosis", "diagnosis", EpisodeOfCareDiagnosis, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("period", "period", period.Period, False, None, False),
            ("referralRequest", "referralRequest", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusHistory", "statusHistory", EpisodeOfCareStatusHistory, True, None, False),
            ("team", "team", fhirreference.FHIRReference, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


from . import backboneelement

class EpisodeOfCareDiagnosis(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    l
    i
    s
    t
    o
    f
    d
    i
    a
    g
    n
    o
    s
    i
    s
    r
    e
    l
    e
    v
    a
    n
    t
    t
    o
    t
    h
    i
    s
    e
    p
    i
    s
    o
    d
    e
    o
    f
    c
    a
    r
    e
    .
    """
    
    resource_type = "EpisodeOfCareDiagnosis"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.condition = None
        """ 
        C
        o
        n
        d
        i
        t
        i
        o
        n
        s
        /
        p
        r
        o
        b
        l
        e
        m
        s
        /
        d
        i
        a
        g
        n
        o
        s
        e
        s
        t
        h
        i
        s
        e
        p
        i
        s
        o
        d
        e
        o
        f
        c
        a
        r
        e
        i
        s
        f
        o
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.rank = None
        """ 
        R
        a
        n
        k
        i
        n
        g
        o
        f
        t
        h
        e
        d
        i
        a
        g
        n
        o
        s
        i
        s
        (
        f
        o
        r
        e
        a
        c
        h
        r
        o
        l
        e
        t
        y
        p
        e
        )
        .
        Type `int`. """
        
        self.role = None
        """ 
        R
        o
        l
        e
        t
        h
        a
        t
        t
        h
        i
        s
        d
        i
        a
        g
        n
        o
        s
        i
        s
        h
        a
        s
        w
        i
        t
        h
        i
        n
        t
        h
        e
        e
        p
        i
        s
        o
        d
        e
        o
        f
        c
        a
        r
        e
        (
        e
        .
        g
        .
        a
        d
        m
        i
        s
        s
        i
        o
        n
        ,
        b
        i
        l
        l
        i
        n
        g
        ,
        d
        i
        s
        c
        h
        a
        r
        g
        e
        …
        )
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(EpisodeOfCareDiagnosis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EpisodeOfCareDiagnosis, self).elementProperties()
        js.extend([
            ("condition", "condition", fhirreference.FHIRReference, False, None, True),
            ("rank", "rank", int, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class EpisodeOfCareStatusHistory(backboneelement.BackboneElement):
    """ 
    P
    a
    s
    t
    l
    i
    s
    t
    o
    f
    s
    t
    a
    t
    u
    s
    c
    o
    d
    e
    s
    (
    t
    h
    e
    c
    u
    r
    r
    e
    n
    t
    s
    t
    a
    t
    u
    s
    m
    a
    y
    b
    e
    i
    n
    c
    l
    u
    d
    e
    d
    t
    o
    c
    o
    v
    e
    r
    t
    h
    e
    s
    t
    a
    r
    t
    d
    a
    t
    e
    o
    f
    t
    h
    e
    s
    t
    a
    t
    u
    s
    )
    .
    
    
    T
    h
    e
    h
    i
    s
    t
    o
    r
    y
    o
    f
    s
    t
    a
    t
    u
    s
    e
    s
    t
    h
    a
    t
    t
    h
    e
    E
    p
    i
    s
    o
    d
    e
    O
    f
    C
    a
    r
    e
    h
    a
    s
    b
    e
    e
    n
    t
    h
    r
    o
    u
    g
    h
    (
    w
    i
    t
    h
    o
    u
    t
    r
    e
    q
    u
    i
    r
    i
    n
    g
    p
    r
    o
    c
    e
    s
    s
    i
    n
    g
    t
    h
    e
    h
    i
    s
    t
    o
    r
    y
    o
    f
    t
    h
    e
    r
    e
    s
    o
    u
    r
    c
    e
    )
    .
    
    """
    
    resource_type = "EpisodeOfCareStatusHistory"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.period = None
        """ 
        D
        u
        r
        a
        t
        i
        o
        n
        t
        h
        e
        E
        p
        i
        s
        o
        d
        e
        O
        f
        C
        a
        r
        e
        w
        a
        s
        i
        n
        t
        h
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
        s
        t
        a
        t
        u
        s
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        p
        l
        a
        n
        n
        e
        d
        |
        w
        a
        i
        t
        l
        i
        s
        t
        |
        a
        c
        t
        i
        v
        e
        |
        o
        n
        h
        o
        l
        d
        |
        f
        i
        n
        i
        s
        h
        e
        d
        |
        c
        a
        n
        c
        e
        l
        l
        e
        d
        |
        e
        n
        t
        e
        r
        e
        d
        -
        i
        n
        -
        e
        r
        r
        o
        r
        .
        Type `str`. """
        
        super(EpisodeOfCareStatusHistory, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EpisodeOfCareStatusHistory, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False, None, True),
            ("status", "status", str, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
