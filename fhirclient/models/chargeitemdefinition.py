#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ChargeItemDefinition) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class ChargeItemDefinition(domainresource.DomainResource):
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
    p
    r
    o
    p
    e
    r
    t
    i
    e
    s
    a
    n
    d
    r
    u
    l
    e
    s
    a
    b
    o
    u
    t
    h
    o
    w
    t
    h
    e
    p
    r
    i
    c
    e
    a
    n
    d
    t
    h
    e
    a
    p
    p
    l
    i
    c
    a
    b
    i
    l
    i
    t
    y
    o
    f
    a
    C
    h
    a
    r
    g
    e
    I
    t
    e
    m
    c
    a
    n
    b
    e
    d
    e
    t
    e
    r
    m
    i
    n
    e
    d
    .
    
    
    T
    h
    e
    C
    h
    a
    r
    g
    e
    I
    t
    e
    m
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
    r
    e
    s
    o
    u
    r
    c
    e
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
    p
    r
    o
    p
    e
    r
    t
    i
    e
    s
    t
    h
    a
    t
    a
    p
    p
    l
    y
    t
    o
    t
    h
    e
    (
    b
    i
    l
    l
    i
    n
    g
    )
    c
    o
    d
    e
    s
    n
    e
    c
    e
    s
    s
    a
    r
    y
    t
    o
    c
    a
    l
    c
    u
    l
    a
    t
    e
    c
    o
    s
    t
    s
    a
    n
    d
    p
    r
    i
    c
    e
    s
    .
    T
    h
    e
    p
    r
    o
    p
    e
    r
    t
    i
    e
    s
    m
    a
    y
    d
    i
    f
    f
    e
    r
    l
    a
    r
    g
    e
    l
    y
    d
    e
    p
    e
    n
    d
    i
    n
    g
    o
    n
    t
    y
    p
    e
    a
    n
    d
    r
    e
    a
    l
    m
    ,
    t
    h
    e
    r
    e
    f
    o
    r
    e
    t
    h
    i
    s
    r
    e
    s
    o
    u
    r
    c
    e
    g
    i
    v
    e
    s
    o
    n
    l
    y
    a
    r
    o
    u
    g
    h
    s
    t
    r
    u
    c
    t
    u
    r
    e
    a
    n
    d
    r
    e
    q
    u
    i
    r
    e
    s
    p
    r
    o
    f
    i
    l
    i
    n
    g
    f
    o
    r
    e
    a
    c
    h
    t
    y
    p
    e
    o
    f
    b
    i
    l
    l
    i
    n
    g
    c
    o
    d
    e
    s
    y
    s
    t
    e
    m
    .
    
    """
    
    resource_type = "ChargeItemDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.applicability = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        o
        r
        n
        o
        t
        t
        h
        e
        b
        i
        l
        l
        i
        n
        g
        c
        o
        d
        e
        i
        s
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
        .
        List of `ChargeItemDefinitionApplicability` items (represented as `dict` in JSON). """
        
        self.approvalDate = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        c
        h
        a
        r
        g
        e
        i
        t
        e
        m
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
        w
        a
        s
        a
        p
        p
        r
        o
        v
        e
        d
        b
        y
        p
        u
        b
        l
        i
        s
        h
        e
        r
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.code = None
        """ 
        B
        i
        l
        l
        i
        n
        g
        c
        o
        d
        e
        s
        o
        r
        p
        r
        o
        d
        u
        c
        t
        t
        y
        p
        e
        s
        t
        h
        i
        s
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
        a
        p
        p
        l
        i
        e
        s
        t
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.contact = None
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
        f
        o
        r
        t
        h
        e
        p
        u
        b
        l
        i
        s
        h
        e
        r
        .
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ 
        U
        s
        e
        a
        n
        d
        /
        o
        r
        p
        u
        b
        l
        i
        s
        h
        i
        n
        g
        r
        e
        s
        t
        r
        i
        c
        t
        i
        o
        n
        s
        .
        Type `str`. """
        
        self.date = None
        """ 
        D
        a
        t
        e
        l
        a
        s
        t
        c
        h
        a
        n
        g
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.derivedFromUri = None
        """ 
        U
        n
        d
        e
        r
        l
        y
        i
        n
        g
        e
        x
        t
        e
        r
        n
        a
        l
        l
        y
        -
        d
        e
        f
        i
        n
        e
        d
        c
        h
        a
        r
        g
        e
        i
        t
        e
        m
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
        .
        List of `str` items. """
        
        self.description = None
        """ 
        N
        a
        t
        u
        r
        a
        l
        l
        a
        n
        g
        u
        a
        g
        e
        d
        e
        s
        c
        r
        i
        p
        t
        i
        o
        n
        o
        f
        t
        h
        e
        c
        h
        a
        r
        g
        e
        i
        t
        e
        m
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
        .
        Type `str`. """
        
        self.effectivePeriod = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        c
        h
        a
        r
        g
        e
        i
        t
        e
        m
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
        i
        s
        e
        x
        p
        e
        c
        t
        e
        d
        t
        o
        b
        e
        u
        s
        e
        d
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.experimental = None
        """ 
        F
        o
        r
        t
        e
        s
        t
        i
        n
        g
        p
        u
        r
        p
        o
        s
        e
        s
        ,
        n
        o
        t
        r
        e
        a
        l
        u
        s
        a
        g
        e
        .
        Type `bool`. """
        
        self.identifier = None
        """ 
        A
        d
        d
        i
        t
        i
        o
        n
        a
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
        f
        o
        r
        t
        h
        e
        c
        h
        a
        r
        g
        e
        i
        t
        e
        m
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
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instance = None
        """ 
        I
        n
        s
        t
        a
        n
        c
        e
        s
        t
        h
        i
        s
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
        a
        p
        p
        l
        i
        e
        s
        t
        o
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ 
        I
        n
        t
        e
        n
        d
        e
        d
        j
        u
        r
        i
        s
        d
        i
        c
        t
        i
        o
        n
        f
        o
        r
        c
        h
        a
        r
        g
        e
        i
        t
        e
        m
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
        (
        i
        f
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
        )
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.lastReviewDate = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        c
        h
        a
        r
        g
        e
        i
        t
        e
        m
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
        w
        a
        s
        l
        a
        s
        t
        r
        e
        v
        i
        e
        w
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.partOf = None
        """ 
        A
        l
        a
        r
        g
        e
        r
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
        o
        f
        w
        h
        i
        c
        h
        t
        h
        i
        s
        p
        a
        r
        t
        i
        c
        u
        l
        a
        r
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
        i
        s
        a
        c
        o
        m
        p
        o
        n
        e
        n
        t
        o
        r
        s
        t
        e
        p
        .
        List of `str` items. """
        
        self.propertyGroup = None
        """ 
        G
        r
        o
        u
        p
        o
        f
        p
        r
        o
        p
        e
        r
        t
        i
        e
        s
        w
        h
        i
        c
        h
        a
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
        u
        n
        d
        e
        r
        t
        h
        e
        s
        a
        m
        e
        c
        o
        n
        d
        i
        t
        i
        o
        n
        s
        .
        List of `ChargeItemDefinitionPropertyGroup` items (represented as `dict` in JSON). """
        
        self.publisher = None
        """ 
        N
        a
        m
        e
        o
        f
        t
        h
        e
        p
        u
        b
        l
        i
        s
        h
        e
        r
        (
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
        o
        r
        i
        n
        d
        i
        v
        i
        d
        u
        a
        l
        )
        .
        Type `str`. """
        
        self.replaces = None
        """ 
        C
        o
        m
        p
        l
        e
        t
        e
        d
        o
        r
        t
        e
        r
        m
        i
        n
        a
        t
        e
        d
        r
        e
        q
        u
        e
        s
        t
        (
        s
        )
        w
        h
        o
        s
        e
        f
        u
        n
        c
        t
        i
        o
        n
        i
        s
        t
        a
        k
        e
        n
        b
        y
        t
        h
        i
        s
        n
        e
        w
        r
        e
        q
        u
        e
        s
        t
        .
        List of `str` items. """
        
        self.status = None
        """ 
        d
        r
        a
        f
        t
        |
        a
        c
        t
        i
        v
        e
        |
        r
        e
        t
        i
        r
        e
        d
        |
        u
        n
        k
        n
        o
        w
        n
        .
        Type `str`. """
        
        self.title = None
        """ 
        N
        a
        m
        e
        f
        o
        r
        t
        h
        i
        s
        c
        h
        a
        r
        g
        e
        i
        t
        e
        m
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
        (
        h
        u
        m
        a
        n
        f
        r
        i
        e
        n
        d
        l
        y
        )
        .
        Type `str`. """
        
        self.url = None
        """ 
        C
        a
        n
        o
        n
        i
        c
        a
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
        f
        o
        r
        t
        h
        i
        s
        c
        h
        a
        r
        g
        e
        i
        t
        e
        m
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
        ,
        r
        e
        p
        r
        e
        s
        e
        n
        t
        e
        d
        a
        s
        a
        U
        R
        I
        (
        g
        l
        o
        b
        a
        l
        l
        y
        u
        n
        i
        q
        u
        e
        )
        .
        Type `str`. """
        
        self.useContext = None
        """ 
        T
        h
        e
        c
        o
        n
        t
        e
        x
        t
        t
        h
        a
        t
        t
        h
        e
        c
        o
        n
        t
        e
        n
        t
        i
        s
        i
        n
        t
        e
        n
        d
        e
        d
        t
        o
        s
        u
        p
        p
        o
        r
        t
        .
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ 
        B
        u
        s
        i
        n
        e
        s
        s
        v
        e
        r
        s
        i
        o
        n
        o
        f
        t
        h
        e
        c
        h
        a
        r
        g
        e
        i
        t
        e
        m
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
        .
        Type `str`. """
        
        super(ChargeItemDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItemDefinition, self).elementProperties()
        js.extend([
            ("applicability", "applicability", ChargeItemDefinitionApplicability, True, None, False),
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("derivedFromUri", "derivedFromUri", str, True, None, False),
            ("description", "description", str, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instance", "instance", fhirreference.FHIRReference, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("partOf", "partOf", str, True, None, False),
            ("propertyGroup", "propertyGroup", ChargeItemDefinitionPropertyGroup, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("replaces", "replaces", str, True, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, True),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class ChargeItemDefinitionApplicability(backboneelement.BackboneElement):
    """ 
    W
    h
    e
    t
    h
    e
    r
    o
    r
    n
    o
    t
    t
    h
    e
    b
    i
    l
    l
    i
    n
    g
    c
    o
    d
    e
    i
    s
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
    .
    
    
    E
    x
    p
    r
    e
    s
    s
    i
    o
    n
    s
    t
    h
    a
    t
    d
    e
    s
    c
    r
    i
    b
    e
    a
    p
    p
    l
    i
    c
    a
    b
    i
    l
    i
    t
    y
    c
    r
    i
    t
    e
    r
    i
    a
    f
    o
    r
    t
    h
    e
    b
    i
    l
    l
    i
    n
    g
    c
    o
    d
    e
    .
    
    """
    
    resource_type = "ChargeItemDefinitionApplicability"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ 
        N
        a
        t
        u
        r
        a
        l
        l
        a
        n
        g
        u
        a
        g
        e
        d
        e
        s
        c
        r
        i
        p
        t
        i
        o
        n
        o
        f
        t
        h
        e
        c
        o
        n
        d
        i
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.expression = None
        """ 
        B
        o
        o
        l
        e
        a
        n
        -
        v
        a
        l
        u
        e
        d
        e
        x
        p
        r
        e
        s
        s
        i
        o
        n
        .
        Type `str`. """
        
        self.language = None
        """ 
        L
        a
        n
        g
        u
        a
        g
        e
        o
        f
        t
        h
        e
        e
        x
        p
        r
        e
        s
        s
        i
        o
        n
        .
        Type `str`. """
        
        super(ChargeItemDefinitionApplicability, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItemDefinitionApplicability, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("language", "language", str, False, None, False),
        ])
        return js


class ChargeItemDefinitionPropertyGroup(backboneelement.BackboneElement):
    """ 
    G
    r
    o
    u
    p
    o
    f
    p
    r
    o
    p
    e
    r
    t
    i
    e
    s
    w
    h
    i
    c
    h
    a
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
    u
    n
    d
    e
    r
    t
    h
    e
    s
    a
    m
    e
    c
    o
    n
    d
    i
    t
    i
    o
    n
    s
    .
    
    
    G
    r
    o
    u
    p
    o
    f
    p
    r
    o
    p
    e
    r
    t
    i
    e
    s
    w
    h
    i
    c
    h
    a
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
    u
    n
    d
    e
    r
    t
    h
    e
    s
    a
    m
    e
    c
    o
    n
    d
    i
    t
    i
    o
    n
    s
    .
    I
    f
    n
    o
    a
    p
    p
    l
    i
    c
    a
    b
    i
    l
    i
    t
    y
    r
    u
    l
    e
    s
    a
    r
    e
    e
    s
    t
    a
    b
    l
    i
    s
    h
    e
    d
    f
    o
    r
    t
    h
    e
    g
    r
    o
    u
    p
    ,
    t
    h
    e
    n
    a
    l
    l
    p
    r
    o
    p
    e
    r
    t
    i
    e
    s
    a
    l
    w
    a
    y
    s
    a
    p
    p
    l
    y
    .
    
    """
    
    resource_type = "ChargeItemDefinitionPropertyGroup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.applicability = None
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
        u
        n
        d
        e
        r
        w
        h
        i
        c
        h
        t
        h
        e
        p
        r
        i
        c
        e
        C
        o
        m
        p
        o
        n
        e
        n
        t
        i
        s
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
        .
        List of `ChargeItemDefinitionApplicability` items (represented as `dict` in JSON). """
        
        self.priceComponent = None
        """ 
        C
        o
        m
        p
        o
        n
        e
        n
        t
        s
        o
        f
        t
        o
        t
        a
        l
        l
        i
        n
        e
        i
        t
        e
        m
        p
        r
        i
        c
        e
        .
        List of `ChargeItemDefinitionPropertyGroupPriceComponent` items (represented as `dict` in JSON). """
        
        super(ChargeItemDefinitionPropertyGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItemDefinitionPropertyGroup, self).elementProperties()
        js.extend([
            ("applicability", "applicability", ChargeItemDefinitionApplicability, True, None, False),
            ("priceComponent", "priceComponent", ChargeItemDefinitionPropertyGroupPriceComponent, True, None, False),
        ])
        return js


class ChargeItemDefinitionPropertyGroupPriceComponent(backboneelement.BackboneElement):
    """ 
    C
    o
    m
    p
    o
    n
    e
    n
    t
    s
    o
    f
    t
    o
    t
    a
    l
    l
    i
    n
    e
    i
    t
    e
    m
    p
    r
    i
    c
    e
    .
    
    
    T
    h
    e
    p
    r
    i
    c
    e
    f
    o
    r
    a
    C
    h
    a
    r
    g
    e
    I
    t
    e
    m
    m
    a
    y
    b
    e
    c
    a
    l
    c
    u
    l
    a
    t
    e
    d
    a
    s
    a
    b
    a
    s
    e
    p
    r
    i
    c
    e
    w
    i
    t
    h
    s
    u
    r
    c
    h
    a
    r
    g
    e
    s
    /
    d
    e
    d
    u
    c
    t
    i
    o
    n
    s
    t
    h
    a
    t
    a
    p
    p
    l
    y
    i
    n
    c
    e
    r
    t
    a
    i
    n
    c
    o
    n
    d
    i
    t
    i
    o
    n
    s
    .
    A
    C
    h
    a
    r
    g
    e
    I
    t
    e
    m
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
    r
    e
    s
    o
    u
    r
    c
    e
    t
    h
    a
    t
    d
    e
    f
    i
    n
    e
    s
    t
    h
    e
    p
    r
    i
    c
    e
    s
    ,
    f
    a
    c
    t
    o
    r
    s
    a
    n
    d
    c
    o
    n
    d
    i
    t
    i
    o
    n
    s
    t
    h
    a
    t
    a
    p
    p
    l
    y
    t
    o
    a
    b
    i
    l
    l
    i
    n
    g
    c
    o
    d
    e
    i
    s
    c
    u
    r
    r
    e
    n
    t
    l
    y
    u
    n
    d
    e
    r
    d
    e
    v
    e
    l
    o
    p
    m
    e
    n
    t
    .
    T
    h
    e
    p
    r
    i
    c
    e
    C
    o
    m
    p
    o
    n
    e
    n
    t
    e
    l
    e
    m
    e
    n
    t
    c
    a
    n
    b
    e
    u
    s
    e
    d
    t
    o
    o
    f
    f
    e
    r
    t
    r
    a
    n
    s
    p
    a
    r
    e
    n
    c
    y
    t
    o
    t
    h
    e
    r
    e
    c
    i
    p
    i
    e
    n
    t
    o
    f
    t
    h
    e
    I
    n
    v
    o
    i
    c
    e
    o
    f
    h
    o
    w
    t
    h
    e
    p
    r
    i
    c
    e
    s
    h
    a
    v
    e
    b
    e
    e
    n
    c
    a
    l
    c
    u
    l
    a
    t
    e
    d
    .
    
    """
    
    resource_type = "ChargeItemDefinitionPropertyGroupPriceComponent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ 
        M
        o
        n
        e
        t
        a
        r
        y
        a
        m
        o
        u
        n
        t
        a
        s
        s
        o
        c
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
        i
        s
        c
        o
        m
        p
        o
        n
        e
        n
        t
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.code = None
        """ 
        C
        o
        d
        e
        i
        d
        e
        n
        t
        i
        f
        y
        i
        n
        g
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
        c
        c
        o
        m
        p
        o
        n
        e
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.factor = None
        """ 
        F
        a
        c
        t
        o
        r
        u
        s
        e
        d
        f
        o
        r
        c
        a
        l
        c
        u
        l
        a
        t
        i
        n
        g
        t
        h
        i
        s
        c
        o
        m
        p
        o
        n
        e
        n
        t
        .
        Type `float`. """
        
        self.type = None
        """ 
        b
        a
        s
        e
        |
        s
        u
        r
        c
        h
        a
        r
        g
        e
        |
        d
        e
        d
        u
        c
        t
        i
        o
        n
        |
        d
        i
        s
        c
        o
        u
        n
        t
        |
        t
        a
        x
        |
        i
        n
        f
        o
        r
        m
        a
        t
        i
        o
        n
        a
        l
        .
        Type `str`. """
        
        super(ChargeItemDefinitionPropertyGroupPriceComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItemDefinitionPropertyGroupPriceComponent, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import money
except ImportError:
    money = sys.modules[__package__ + '.money']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']