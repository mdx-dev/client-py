#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-01-22.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import specimendefinition
from .fhirdate import FHIRDate


class SpecimenDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("SpecimenDefinition", js["resourceType"])
        return specimendefinition.SpecimenDefinition(js)
    
    def testSpecimenDefinition1(self):
        inst = self.instantiate_from("specimendefinition-example-serum-plasma.json")
        self.assertIsNotNone(inst, "Must have instantiated a SpecimenDefinition instance")
        self.implSpecimenDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("SpecimenDefinition", js["resourceType"])
        inst2 = specimendefinition.SpecimenDefinition(js)
        self.implSpecimenDefinition1(inst2)
    
    def implSpecimenDefinition1(self, inst):
        self.assertEqual(inst.id, "2364")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.patientPreparation[0].text, "12 hour fasting")
        self.assertEqual(inst.patientPreparation[1].coding[0].code, "263678003")
        self.assertEqual(inst.patientPreparation[1].coding[0].display, "At rest")
        self.assertEqual(inst.patientPreparation[1].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.timeAspect, "preferrably morning time")
        self.assertEqual(inst.typeCollected.coding[0].code, "122555007")
        self.assertEqual(inst.typeCollected.coding[0].display, "Venous blood specimen")
        self.assertEqual(inst.typeCollected.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.typeTested[0].container.cap.coding[0].code, "yellow")
        self.assertEqual(inst.typeTested[0].container.cap.coding[0].display, "yellow cap")
        self.assertEqual(inst.typeTested[0].container.cap.coding[0].system, "urn:iso:std:iso:6710:2017")
        self.assertEqual(inst.typeTested[0].container.material.coding[0].code, "61088005")
        self.assertEqual(inst.typeTested[0].container.material.coding[0].display, "plastic")
        self.assertEqual(inst.typeTested[0].container.material.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.typeTested[0].container.minimumVolumeQuantity.code, "mL")
        self.assertEqual(inst.typeTested[0].container.minimumVolumeQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[0].container.minimumVolumeQuantity.unit, "ml")
        self.assertEqual(inst.typeTested[0].container.minimumVolumeQuantity.value, 2)
        self.assertEqual(inst.typeTested[0].container.type.coding[0].code, "702281005")
        self.assertEqual(inst.typeTested[0].container.type.coding[0].display, "Evacuated blood collection tube, thrombin/clot activator/gel separator")
        self.assertEqual(inst.typeTested[0].container.type.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.typeTested[0].handling[0].maxDuration.code, "min")
        self.assertEqual(inst.typeTested[0].handling[0].maxDuration.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[0].handling[0].maxDuration.unit, "minute")
        self.assertEqual(inst.typeTested[0].handling[0].maxDuration.value, 60)
        self.assertEqual(inst.typeTested[0].handling[0].temperatureQualifier.text, "Ambient temperature")
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.high.code, "Cel")
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.high.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.high.unit, "°C")
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.high.value, 25)
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.low.code, "Cel")
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.low.unit, "°C")
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.low.value, 15)
        self.assertEqual(inst.typeTested[0].handling[1].maxDuration.code, "h")
        self.assertEqual(inst.typeTested[0].handling[1].maxDuration.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[0].handling[1].maxDuration.unit, "hour")
        self.assertEqual(inst.typeTested[0].handling[1].maxDuration.value, 8)
        self.assertEqual(inst.typeTested[0].handling[1].temperatureQualifier.text, "Refrigerated temperature")
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.high.code, "Cel")
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.high.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.high.unit, "°C")
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.high.value, 8)
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.low.code, "Cel")
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.low.unit, "°C")
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.low.value, 2)
        self.assertEqual(inst.typeTested[0].preference, "preferred")
        self.assertEqual(inst.typeTested[0].type.coding[0].code, "119364003")
        self.assertEqual(inst.typeTested[0].type.coding[0].display, "Serum specimen")
        self.assertEqual(inst.typeTested[0].type.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.typeTested[1].container.cap.coding[0].code, "green")
        self.assertEqual(inst.typeTested[1].container.cap.coding[0].display, "green cap")
        self.assertEqual(inst.typeTested[1].container.cap.coding[0].system, "urn:iso:std:iso:6710:2017")
        self.assertEqual(inst.typeTested[1].container.material.coding[0].code, "32039001")
        self.assertEqual(inst.typeTested[1].container.material.coding[0].display, "glass")
        self.assertEqual(inst.typeTested[1].container.material.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.typeTested[1].container.minimumVolumeQuantity.code, "mL")
        self.assertEqual(inst.typeTested[1].container.minimumVolumeQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[1].container.minimumVolumeQuantity.unit, "ml")
        self.assertEqual(inst.typeTested[1].container.minimumVolumeQuantity.value, 2)
        self.assertEqual(inst.typeTested[1].container.type.coding[0].code, "767390000")
        self.assertEqual(inst.typeTested[1].container.type.coding[0].display, "Evacuated blood collection tube with heparin lithium and gel separator")
        self.assertEqual(inst.typeTested[1].container.type.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.typeTested[1].handling[0].maxDuration.code, "min")
        self.assertEqual(inst.typeTested[1].handling[0].maxDuration.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[1].handling[0].maxDuration.unit, "minute")
        self.assertEqual(inst.typeTested[1].handling[0].maxDuration.value, 60)
        self.assertEqual(inst.typeTested[1].handling[0].temperatureQualifier.text, "Ambient temperature")
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.high.code, "Cel")
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.high.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.high.unit, "°C")
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.high.value, 25)
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.low.code, "Cel")
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.low.unit, "°C")
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.low.value, 15)
        self.assertEqual(inst.typeTested[1].handling[1].maxDuration.code, "h")
        self.assertEqual(inst.typeTested[1].handling[1].maxDuration.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[1].handling[1].maxDuration.unit, "hour")
        self.assertEqual(inst.typeTested[1].handling[1].maxDuration.value, 8)
        self.assertEqual(inst.typeTested[1].handling[1].temperatureQualifier.text, "Refrigerated temperature")
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.high.code, "Cel")
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.high.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.high.unit, "°C")
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.high.value, 8)
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.low.code, "Cel")
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.low.unit, "°C")
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.low.value, 2)
        self.assertEqual(inst.typeTested[1].preference, "alternate")
        self.assertEqual(inst.typeTested[1].rejectionCriterion[0].coding[0].code, "insufficient")
        self.assertEqual(inst.typeTested[1].rejectionCriterion[0].coding[0].display, "insufficient specimen volume")
        self.assertEqual(inst.typeTested[1].rejectionCriterion[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/rejection-criteria")
        self.assertEqual(inst.typeTested[1].rejectionCriterion[1].coding[0].code, "hemolized")
        self.assertEqual(inst.typeTested[1].rejectionCriterion[1].coding[0].display, "hemolized specimen")
        self.assertEqual(inst.typeTested[1].rejectionCriterion[1].coding[0].system, "http://terminology.hl7.org/CodeSystem/rejection-criteria")
        self.assertEqual(inst.typeTested[1].type.coding[0].code, "119361006")
        self.assertEqual(inst.typeTested[1].type.coding[0].display, "Plasma specimen")
        self.assertEqual(inst.typeTested[1].type.coding[0].system, "http://snomed.info/sct")

