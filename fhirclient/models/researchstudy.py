#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ResearchStudy) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class ResearchStudy(domainresource.DomainResource):
    """ 
    I
    n
    v
    e
    s
    t
    i
    g
    a
    t
    i
    o
    n
    t
    o
    i
    n
    c
    r
    e
    a
    s
    e
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
    -
    r
    e
    l
    a
    t
    e
    d
    p
    a
    t
    i
    e
    n
    t
    -
    i
    n
    d
    e
    p
    e
    n
    d
    e
    n
    t
    k
    n
    o
    w
    l
    e
    d
    g
    e
    .
    
    
    A
    p
    r
    o
    c
    e
    s
    s
    w
    h
    e
    r
    e
    a
    r
    e
    s
    e
    a
    r
    c
    h
    e
    r
    o
    r
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
    p
    l
    a
    n
    s
    a
    n
    d
    t
    h
    e
    n
    e
    x
    e
    c
    u
    t
    e
    s
    a
    s
    e
    r
    i
    e
    s
    o
    f
    s
    t
    e
    p
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
    i
    n
    c
    r
    e
    a
    s
    e
    t
    h
    e
    f
    i
    e
    l
    d
    o
    f
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
    -
    r
    e
    l
    a
    t
    e
    d
    k
    n
    o
    w
    l
    e
    d
    g
    e
    .
    T
    h
    i
    s
    i
    n
    c
    l
    u
    d
    e
    s
    s
    t
    u
    d
    i
    e
    s
    o
    f
    s
    a
    f
    e
    t
    y
    ,
    e
    f
    f
    i
    c
    a
    c
    y
    ,
    c
    o
    m
    p
    a
    r
    a
    t
    i
    v
    e
    e
    f
    f
    e
    c
    t
    i
    v
    e
    n
    e
    s
    s
    a
    n
    d
    o
    t
    h
    e
    r
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
    b
    o
    u
    t
    m
    e
    d
    i
    c
    a
    t
    i
    o
    n
    s
    ,
    d
    e
    v
    i
    c
    e
    s
    ,
    t
    h
    e
    r
    a
    p
    i
    e
    s
    a
    n
    d
    o
    t
    h
    e
    r
    i
    n
    t
    e
    r
    v
    e
    n
    t
    i
    o
    n
    a
    l
    a
    n
    d
    i
    n
    v
    e
    s
    t
    i
    g
    a
    t
    i
    v
    e
    t
    e
    c
    h
    n
    i
    q
    u
    e
    s
    .
    A
    R
    e
    s
    e
    a
    r
    c
    h
    S
    t
    u
    d
    y
    i
    n
    v
    o
    l
    v
    e
    s
    t
    h
    e
    g
    a
    t
    h
    e
    r
    i
    n
    g
    o
    f
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
    b
    o
    u
    t
    h
    u
    m
    a
    n
    o
    r
    a
    n
    i
    m
    a
    l
    s
    u
    b
    j
    e
    c
    t
    s
    .
    
    """
    
    resource_type = "ResearchStudy"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.arm = None
        """ 
        D
        e
        f
        i
        n
        e
        d
        p
        a
        t
        h
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
        s
        t
        u
        d
        y
        f
        o
        r
        a
        s
        u
        b
        j
        e
        c
        t
        .
        List of `ResearchStudyArm` items (represented as `dict` in JSON). """
        
        self.category = None
        """ 
        C
        l
        a
        s
        s
        i
        f
        i
        c
        a
        t
        i
        o
        n
        s
        f
        o
        r
        t
        h
        e
        s
        t
        u
        d
        y
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        b
        e
        i
        n
        g
        s
        t
        u
        d
        i
        e
        d
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        s
        t
        u
        d
        y
        .
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.description = None
        """ 
        W
        h
        a
        t
        t
        h
        i
        s
        i
        s
        s
        t
        u
        d
        y
        d
        o
        i
        n
        g
        .
        Type `str`. """
        
        self.enrollment = None
        """ 
        I
        n
        c
        l
        u
        s
        i
        o
        n
        &
        e
        x
        c
        l
        u
        s
        i
        o
        n
        c
        r
        i
        t
        e
        r
        i
        a
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.focus = None
        """ 
        D
        r
        u
        g
        s
        ,
        d
        e
        v
        i
        c
        e
        s
        ,
        e
        t
        c
        .
        u
        n
        d
        e
        r
        s
        t
        u
        d
        y
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        f
        o
        r
        s
        t
        u
        d
        y
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.keyword = None
        """ 
        U
        s
        e
        d
        t
        o
        s
        e
        a
        r
        c
        h
        f
        o
        r
        t
        h
        e
        s
        t
        u
        d
        y
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.location = None
        """ 
        G
        e
        o
        g
        r
        a
        p
        h
        i
        c
        r
        e
        g
        i
        o
        n
        (
        s
        )
        f
        o
        r
        s
        t
        u
        d
        y
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.note = None
        """ 
        C
        o
        m
        m
        e
        n
        t
        s
        m
        a
        d
        e
        a
        b
        o
        u
        t
        t
        h
        e
        s
        t
        u
        d
        y
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.objective = None
        """ 
        A
        g
        o
        a
        l
        f
        o
        r
        t
        h
        e
        s
        t
        u
        d
        y
        .
        List of `ResearchStudyObjective` items (represented as `dict` in JSON). """
        
        self.partOf = None
        """ 
        P
        a
        r
        t
        o
        f
        l
        a
        r
        g
        e
        r
        s
        t
        u
        d
        y
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.period = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        s
        t
        u
        d
        y
        b
        e
        g
        a
        n
        a
        n
        d
        e
        n
        d
        e
        d
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.phase = None
        """ 
        n
        -
        a
        |
        e
        a
        r
        l
        y
        -
        p
        h
        a
        s
        e
        -
        1
        |
        p
        h
        a
        s
        e
        -
        1
        |
        p
        h
        a
        s
        e
        -
        1
        -
        p
        h
        a
        s
        e
        -
        2
        |
        p
        h
        a
        s
        e
        -
        2
        |
        p
        h
        a
        s
        e
        -
        2
        -
        p
        h
        a
        s
        e
        -
        3
        |
        p
        h
        a
        s
        e
        -
        3
        |
        p
        h
        a
        s
        e
        -
        4
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.primaryPurposeType = None
        """ 
        t
        r
        e
        a
        t
        m
        e
        n
        t
        |
        p
        r
        e
        v
        e
        n
        t
        i
        o
        n
        |
        d
        i
        a
        g
        n
        o
        s
        t
        i
        c
        |
        s
        u
        p
        p
        o
        r
        t
        i
        v
        e
        -
        c
        a
        r
        e
        |
        s
        c
        r
        e
        e
        n
        i
        n
        g
        |
        h
        e
        a
        l
        t
        h
        -
        s
        e
        r
        v
        i
        c
        e
        s
        -
        r
        e
        s
        e
        a
        r
        c
        h
        |
        b
        a
        s
        i
        c
        -
        s
        c
        i
        e
        n
        c
        e
        |
        d
        e
        v
        i
        c
        e
        -
        f
        e
        a
        s
        i
        b
        i
        l
        i
        t
        y
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.principalInvestigator = None
        """ 
        R
        e
        s
        e
        a
        r
        c
        h
        e
        r
        w
        h
        o
        o
        v
        e
        r
        s
        e
        e
        s
        m
        u
        l
        t
        i
        p
        l
        e
        a
        s
        p
        e
        c
        t
        s
        o
        f
        t
        h
        e
        s
        t
        u
        d
        y
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.protocol = None
        """ 
        S
        t
        e
        p
        s
        f
        o
        l
        l
        o
        w
        e
        d
        i
        n
        e
        x
        e
        c
        u
        t
        i
        n
        g
        s
        t
        u
        d
        y
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.reasonStopped = None
        """ 
        a
        c
        c
        r
        u
        a
        l
        -
        g
        o
        a
        l
        -
        m
        e
        t
        |
        c
        l
        o
        s
        e
        d
        -
        d
        u
        e
        -
        t
        o
        -
        t
        o
        x
        i
        c
        i
        t
        y
        |
        c
        l
        o
        s
        e
        d
        -
        d
        u
        e
        -
        t
        o
        -
        l
        a
        c
        k
        -
        o
        f
        -
        s
        t
        u
        d
        y
        -
        p
        r
        o
        g
        r
        e
        s
        s
        |
        t
        e
        m
        p
        o
        r
        a
        r
        i
        l
        y
        -
        c
        l
        o
        s
        e
        d
        -
        p
        e
        r
        -
        s
        t
        u
        d
        y
        -
        d
        e
        s
        i
        g
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.relatedArtifact = None
        """ 
        R
        e
        f
        e
        r
        e
        n
        c
        e
        s
        a
        n
        d
        d
        e
        p
        e
        n
        d
        e
        n
        c
        i
        e
        s
        .
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        
        self.site = None
        """ 
        F
        a
        c
        i
        l
        i
        t
        y
        w
        h
        e
        r
        e
        s
        t
        u
        d
        y
        a
        c
        t
        i
        v
        i
        t
        i
        e
        s
        a
        r
        e
        c
        o
        n
        d
        u
        c
        t
        e
        d
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.sponsor = None
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
        i
        n
        i
        t
        i
        a
        t
        e
        s
        a
        n
        d
        i
        s
        l
        e
        g
        a
        l
        l
        y
        r
        e
        s
        p
        o
        n
        s
        i
        b
        l
        e
        f
        o
        r
        t
        h
        e
        s
        t
        u
        d
        y
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        a
        c
        t
        i
        v
        e
        |
        a
        d
        m
        i
        n
        i
        s
        t
        r
        a
        t
        i
        v
        e
        l
        y
        -
        c
        o
        m
        p
        l
        e
        t
        e
        d
        |
        a
        p
        p
        r
        o
        v
        e
        d
        |
        c
        l
        o
        s
        e
        d
        -
        t
        o
        -
        a
        c
        c
        r
        u
        a
        l
        |
        c
        l
        o
        s
        e
        d
        -
        t
        o
        -
        a
        c
        c
        r
        u
        a
        l
        -
        a
        n
        d
        -
        i
        n
        t
        e
        r
        v
        e
        n
        t
        i
        o
        n
        |
        c
        o
        m
        p
        l
        e
        t
        e
        d
        |
        d
        i
        s
        a
        p
        p
        r
        o
        v
        e
        d
        |
        i
        n
        -
        r
        e
        v
        i
        e
        w
        |
        t
        e
        m
        p
        o
        r
        a
        r
        i
        l
        y
        -
        c
        l
        o
        s
        e
        d
        -
        t
        o
        -
        a
        c
        c
        r
        u
        a
        l
        |
        t
        e
        m
        p
        o
        r
        a
        r
        i
        l
        y
        -
        c
        l
        o
        s
        e
        d
        -
        t
        o
        -
        a
        c
        c
        r
        u
        a
        l
        -
        a
        n
        d
        -
        i
        n
        t
        e
        r
        v
        e
        n
        t
        i
        o
        n
        |
        w
        i
        t
        h
        d
        r
        a
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
        s
        t
        u
        d
        y
        .
        Type `str`. """
        
        super(ResearchStudy, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ResearchStudy, self).elementProperties()
        js.extend([
            ("arm", "arm", ResearchStudyArm, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("condition", "condition", codeableconcept.CodeableConcept, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("description", "description", str, False, None, False),
            ("enrollment", "enrollment", fhirreference.FHIRReference, True, None, False),
            ("focus", "focus", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("keyword", "keyword", codeableconcept.CodeableConcept, True, None, False),
            ("location", "location", codeableconcept.CodeableConcept, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("objective", "objective", ResearchStudyObjective, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("phase", "phase", codeableconcept.CodeableConcept, False, None, False),
            ("primaryPurposeType", "primaryPurposeType", codeableconcept.CodeableConcept, False, None, False),
            ("principalInvestigator", "principalInvestigator", fhirreference.FHIRReference, False, None, False),
            ("protocol", "protocol", fhirreference.FHIRReference, True, None, False),
            ("reasonStopped", "reasonStopped", codeableconcept.CodeableConcept, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("site", "site", fhirreference.FHIRReference, True, None, False),
            ("sponsor", "sponsor", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
        ])
        return js


from . import backboneelement

class ResearchStudyArm(backboneelement.BackboneElement):
    """ 
    D
    e
    f
    i
    n
    e
    d
    p
    a
    t
    h
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
    s
    t
    u
    d
    y
    f
    o
    r
    a
    s
    u
    b
    j
    e
    c
    t
    .
    
    
    D
    e
    s
    c
    r
    i
    b
    e
    s
    a
    n
    e
    x
    p
    e
    c
    t
    e
    d
    s
    e
    q
    u
    e
    n
    c
    e
    o
    f
    e
    v
    e
    n
    t
    s
    f
    o
    r
    o
    n
    e
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
    n
    t
    s
    o
    f
    a
    s
    t
    u
    d
    y
    .
    E
    .
    g
    .
    E
    x
    p
    o
    s
    u
    r
    e
    t
    o
    d
    r
    u
    g
    A
    ,
    w
    a
    s
    h
    -
    o
    u
    t
    ,
    e
    x
    p
    o
    s
    u
    r
    e
    t
    o
    d
    r
    u
    g
    B
    ,
    w
    a
    s
    h
    -
    o
    u
    t
    ,
    f
    o
    l
    l
    o
    w
    -
    u
    p
    .
    
    """
    
    resource_type = "ResearchStudyArm"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ 
        S
        h
        o
        r
        t
        e
        x
        p
        l
        a
        n
        a
        t
        i
        o
        n
        o
        f
        s
        t
        u
        d
        y
        p
        a
        t
        h
        .
        Type `str`. """
        
        self.name = None
        """ 
        L
        a
        b
        e
        l
        f
        o
        r
        s
        t
        u
        d
        y
        a
        r
        m
        .
        Type `str`. """
        
        self.type = None
        """ 
        C
        a
        t
        e
        g
        o
        r
        i
        z
        a
        t
        i
        o
        n
        o
        f
        s
        t
        u
        d
        y
        a
        r
        m
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ResearchStudyArm, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ResearchStudyArm, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ResearchStudyObjective(backboneelement.BackboneElement):
    """ 
    A
    g
    o
    a
    l
    f
    o
    r
    t
    h
    e
    s
    t
    u
    d
    y
    .
    
    
    A
    g
    o
    a
    l
    t
    h
    a
    t
    t
    h
    e
    s
    t
    u
    d
    y
    i
    s
    a
    i
    m
    i
    n
    g
    t
    o
    a
    c
    h
    i
    e
    v
    e
    i
    n
    t
    e
    r
    m
    s
    o
    f
    a
    s
    c
    i
    e
    n
    t
    i
    f
    i
    c
    q
    u
    e
    s
    t
    i
    o
    n
    t
    o
    b
    e
    a
    n
    s
    w
    e
    r
    e
    d
    b
    y
    t
    h
    e
    a
    n
    a
    l
    y
    s
    i
    s
    o
    f
    d
    a
    t
    a
    c
    o
    l
    l
    e
    c
    t
    e
    d
    d
    u
    r
    i
    n
    g
    t
    h
    e
    s
    t
    u
    d
    y
    .
    
    """
    
    resource_type = "ResearchStudyObjective"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ 
        L
        a
        b
        e
        l
        f
        o
        r
        t
        h
        e
        o
        b
        j
        e
        c
        t
        i
        v
        e
        .
        Type `str`. """
        
        self.type = None
        """ 
        p
        r
        i
        m
        a
        r
        y
        |
        s
        e
        c
        o
        n
        d
        a
        r
        y
        |
        e
        x
        p
        l
        o
        r
        a
        t
        o
        r
        y
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ResearchStudyObjective, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ResearchStudyObjective, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
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
try:
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + '.relatedartifact']
