# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25, 2019 12:00:40 2019

@author: Shahi Dost (shahidost@gmail.com)

Description: This python script is extracting PIKES annotations for NER and entitie linking information from VTKL dataset.
"""

##==> external library(ies)
import rdflib

#insert the path of VTKL dataset file (.ttl)
vtkl_dataset="insert .ttl file path" 

#parsing RDF file
g1=rdflib.ConjunctiveGraph()

g1.parse(vtkl_dataset, format="turtle")

#Sparql query to process VTKL dataset for PIKES annotations

## 
qres1=g1.query("""
         PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
         PREFIX yago: <http://dbpedia.org/class/yago/>
         SELECT *
         WHERE{


                 ?mention_id a ks:Entity .
                 ?mention_id owl:sameAs ?mention_pikes.
                 ?mention_pikes a ?yago_class.
                         
         }
    """)

def Image_information(qres):
    """
    Extracting YAGO class information from VTKL by using Sqarql query
    input:
      qres - Sparql query for extracting YAGO information from VTKL dataset
    
    output:
      YAGO_info- a list of dictionaries for entity mention, its ID and corresponding YAGO class with the following fields:
          mention_id - image id+phrase ID (same phrase ID used by Flickr30k)
          entity_mention - textual entity mentioned extracted by PIKES for all image captions (C0,C1,C2,C3,C4) [Representation:imageID+captionNo/#EntityMention]
          YAGO_class - RUI links for corresponding YAGO class.(e.g. for #man -> 'http://dbpedia.org/class/yago/Man110287213')
    """

    YAGO_info=[]
    image_info={}
    for row in qres:
#        print(row[1][37:],row[2][37:],row[0])
        mention_id=row[1][37:]
        textual_mention=row[2][37:]
        YAGO_class=row[0][:]
        image_info={'mention_id':mention_id,'entity_mention':textual_mention,'YAGO_class':YAGO_class}
        YAGO_info.append(image_info)
    
    return YAGO_info   

YAGO_info=Image_information(qres1)
# test output
#print(YAGO_info[0:5])
