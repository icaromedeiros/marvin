import warnings

from FuXi.Rete.RuleStore import SetupRuleStore
from FuXi.Horn.HornRules import HornFromN3
from FuXi.Rete.Util import generateTokenSet
from rdflib.Graph import Graph


warnings.filterwarnings("ignore")


def build_rdfs_owl_rules():
    rule_store, rule_graph, network = SetupRuleStore(makeNetwork=True)
    rdfs_rules = HornFromN3('rules/rdfs_rules.n3')
    for rule in rdfs_rules:
        network.buildNetworkFromClause(rule)

    owl_rules = HornFromN3('rules/owl_rules.n3')
    for rule in owl_rules:
        try:
            network.buildNetworkFromClause(rule)
        except:
            pass  # TODO ignoring FuXi errors
    return network


class Inference():

    def __init__(self):
        self.network = build_rdfs_owl_rules()
        closureDeltaGraph = Graph()
        self.network.inferredFacts = closureDeltaGraph

    def add_facts(self, facts):
        self.network.feedFactsToAdd(generateTokenSet(facts))

    def get_inferred_facts(self):
        return self.network.inferredFacts