#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/OrganizationAffiliation) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class OrganizationAffiliation(domainresource.DomainResource):
    """ 
    D
    e
    f
    i
    n
    e
    s
    a
    n
    a
    f
    f
    i
    l
    i
    a
    t
    i
    o
    n
    /
    a
    s
    s
    o
    t
    i
    a
    t
    i
    o
    n
    /
    r
    e
    l
    a
    t
    i
    o
    n
    s
    h
    i
    p
    b
    e
    t
    w
    e
    e
    n
    2
    d
    i
    s
    t
    i
    n
    c
    t
    o
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
    s
    ,
    t
    h
    a
    t
    i
    s
    n
    o
    t
    a
    p
    a
    r
    t
    -
    o
    f
    r
    e
    l
    a
    t
    i
    o
    n
    s
    h
    i
    p
    /
    s
    u
    b
    -
    d
    i
    v
    i
    s
    i
    o
    n
    r
    e
    l
    a
    t
    i
    o
    n
    s
    h
    i
    p
    .
    """
    
    resource_type = "OrganizationAffiliation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        t
        h
        i
        s
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
        f
        f
        i
        l
        i
        a
        t
        i
        o
        n
        r
        e
        c
        o
        r
        d
        i
        s
        i
        n
        a
        c
        t
        i
        v
        e
        u
        s
        e
        .
        Type `bool`. """
        
        self.code = None
        """ 
        D
        e
        f
        i
        n
        i
        t
        i
        o
        n
        o
        f
        t
        h
        e
        r
        o
        l
        e
        t
        h
        e
        p
        a
        r
        t
        i
        c
        i
        p
        a
        t
        i
        n
        g
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
        p
        l
        a
        y
        s
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.endpoint = None
        """ 
        T
        e
        c
        h
        n
        i
        c
        a
        l
        e
        n
        d
        p
        o
        i
        n
        t
        s
        p
        r
        o
        v
        i
        d
        i
        n
        g
        a
        c
        c
        e
        s
        s
        t
        o
        s
        e
        r
        v
        i
        c
        e
        s
        o
        p
        e
        r
        a
        t
        e
        d
        f
        o
        r
        t
        h
        i
        s
        r
        o
        l
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.healthcareService = None
        """ 
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
        s
        e
        r
        v
        i
        c
        e
        s
        p
        r
        o
        v
        i
        d
        e
        d
        t
        h
        r
        o
        u
        g
        h
        t
        h
        e
        r
        o
        l
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        t
        h
        a
        t
        a
        r
        e
        s
        p
        e
        c
        i
        f
        i
        c
        t
        o
        t
        h
        i
        s
        r
        o
        l
        e
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        """ 
        T
        h
        e
        l
        o
        c
        a
        t
        i
        o
        n
        (
        s
        )
        a
        t
        w
        h
        i
        c
        h
        t
        h
        e
        r
        o
        l
        e
        o
        c
        c
        u
        r
        s
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.network = None
        """ 
        H
        e
        a
        l
        t
        h
        i
        n
        s
        u
        r
        a
        n
        c
        e
        p
        r
        o
        v
        i
        d
        e
        r
        n
        e
        t
        w
        o
        r
        k
        i
        n
        w
        h
        i
        c
        h
        t
        h
        e
        p
        a
        r
        t
        i
        c
        i
        p
        a
        t
        i
        n
        g
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
        p
        r
        o
        v
        i
        d
        e
        s
        t
        h
        e
        r
        o
        l
        e
        '
        s
        s
        e
        r
        v
        i
        c
        e
        s
        (
        i
        f
        d
        e
        f
        i
        n
        e
        d
        )
        a
        t
        t
        h
        e
        i
        n
        d
        i
        c
        a
        t
        e
        d
        l
        o
        c
        a
        t
        i
        o
        n
        s
        (
        i
        f
        d
        e
        f
        i
        n
        e
        d
        )
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.organization = None
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
        w
        h
        e
        r
        e
        t
        h
        e
        r
        o
        l
        e
        i
        s
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
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.participatingOrganization = None
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
        p
        r
        o
        v
        i
        d
        e
        s
        /
        p
        e
        r
        f
        o
        r
        m
        s
        t
        h
        e
        r
        o
        l
        e
        (
        e
        .
        g
        .
        p
        r
        o
        v
        i
        d
        i
        n
        g
        s
        e
        r
        v
        i
        c
        e
        s
        o
        r
        i
        s
        a
        m
        e
        m
        b
        e
        r
        o
        f
        )
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ 
        T
        h
        e
        p
        e
        r
        i
        o
        d
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
        h
        e
        p
        a
        r
        t
        i
        c
        i
        p
        a
        t
        i
        n
        g
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
        i
        s
        a
        f
        f
        i
        l
        i
        a
        t
        e
        d
        w
        i
        t
        h
        t
        h
        e
        p
        r
        i
        m
        a
        r
        y
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
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.specialty = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        c
        s
        p
        e
        c
        i
        a
        l
        t
        y
        o
        f
        t
        h
        e
        p
        a
        r
        t
        i
        c
        i
        p
        a
        t
        i
        n
        g
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
        i
        n
        t
        h
        e
        c
        o
        n
        t
        e
        x
        t
        o
        f
        t
        h
        e
        r
        o
        l
        e
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.telecom = None
        """ 
        C
        o
        n
        t
        a
        c
        t
        d
        e
        t
        a
        i
        l
        s
        a
        t
        t
        h
        e
        p
        a
        r
        t
        i
        c
        i
        p
        a
        t
        i
        n
        g
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
        A
        f
        f
        i
        l
        i
        a
        t
        i
        o
        n
        .
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(OrganizationAffiliation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OrganizationAffiliation, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("healthcareService", "healthcareService", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("location", "location", fhirreference.FHIRReference, True, None, False),
            ("network", "network", fhirreference.FHIRReference, True, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("participatingOrganization", "participatingOrganization", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
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
