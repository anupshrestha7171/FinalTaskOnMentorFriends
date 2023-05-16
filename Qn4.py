import spacy
import networkx as nx

# Load the spaCy English language model
nlp = spacy.load('en_core_web_sm')

# Read the text content from the file
with open('website_text.txt', 'r', encoding='utf-8') as f:
    website_text = f.read()

# Process the text content with spaCy
doc = nlp(website_text)

# Initialize a directed graph
graph = nx.DiGraph()

# Extract entities and relationships from each sentence
for sent in doc.sents:
    subj, obj, rel = None, None, None
    for token in sent:
        if token.dep_ == 'nsubj':
            subj = token.text
        elif token.dep_ == 'dobj':
            obj = token.text
        elif token.dep_ == 'relcl':
            rel = token.text
    if subj and obj and rel:
        # Add nodes and edges to the graph
        graph.add_node(subj, label=subj)
        graph.add_node(obj, label=obj)
        graph.add_edge(subj, obj, label=rel)

# Save the graph as a GraphML file
#nx.write_graphml(graph, 'graph.graphml')
