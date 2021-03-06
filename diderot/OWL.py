"""
    Utility model to create ``OWL`` namespace, not
    include in ``RDFlib`` 2.4.2, so that users can
    refer to OWL constructs easily.

    .. code-block:: python

       from diderot import OWL
       from diderot.utils import get_empty_graph

       graph = get_empty_graph
       graph.add((URIRef(":Mortal"), RDF.type, OWL.Class))
"""

from rdflib.Namespace import Namespace

OWLNS = Namespace("http://www.w3.org/2002/07/owl#")

Class = OWLNS["Class"]
AnnotationProperty = OWLNS["AnnotationProperty"]
DataRange = OWLNS["DataRange"]
DatatypeProperty = OWLNS["DatatypeProperty"]
DeprecatedClass = OWLNS["DeprecatedClass"]
DeprecatedProperty = OWLNS["DeprecatedProperty "]
FunctionalProperty = OWLNS["FunctionalProperty"]
InverseFunctionalProperty = OWLNS["InverseFunctionalProperty"]
Nothing = OWLNS["Nothing"]
ObjectProperty = OWLNS["ObjectProperty"]
OntologyProperty = OWLNS["OntologyProperty"]
Restriction = OWLNS["Restriction"]
SymmetricProperty = OWLNS["SymmetricProperty"]
Thing = OWLNS["Thing"]
TransitiveProperty = OWLNS["TransitiveProperty"]

allValuesFrom = OWLNS["allValuesFrom"]
cardinality = OWLNS["cardinality"]
complementOf = OWLNS["complementOf"]
differentFrom = OWLNS["differentFrom"]
disjointWith = OWLNS["disjointWith"]
distinctMembers = OWLNS["distinctMembers"]
hasValue = OWLNS["hasValue"]
intersectionOf = OWLNS["intersectionOf"]
inverseOf = OWLNS["inverseOf"]
maxCardinality = OWLNS["maxCardinality"]
minCardinality = OWLNS["minCardinality"]
onProperty = OWLNS["onProperty"]
oneOf = OWLNS["oneOf"]
sameAs = OWLNS["sameAs"]
someValuesFrom = OWLNS["someValuesFrom"]
unionOf = OWLNS["unionOf"]
