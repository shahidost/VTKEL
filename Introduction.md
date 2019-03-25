
Visual-textual-knowledge-linking (VTKL) dataset, contains documents composed of pictures with five corresponding textual captions. The VTKL dataset is obtained by extending the Flikr30k dataset, designed for visual-textual mention alignment, with links to YAGO, one of the largest web knowledge base. These links are obtained automatically by processing each image caption with PIKES, an NLP tool for entity recognition and linking.

To understand VTKL dataset consider the documents shown in below Figure, which is composed of one picture and a short sentence (caption) in natural language. From figure, one can find five visual mentions, shown in coloured rectangles in the picture, and five textual mention, underlined in the text. Of course one could find many more visual mention in the picture, e.g., windows, road, etc. but suppose we are only intersted in the mentions of certain types. Let us consider a knowledge base (e.g. YAGO) that contains knowledge about the named entities e_Vespa, e_Milan, e_Italy, and e_1948 for for 'Vespa', 'Milan', 'Italy' and '1948' respectively. E.g.,scooter (e_Vespa), town (e_Milan), country (e_Italy), and year (e_1948). Suppose also that the knowledge base contains the concepts Man, and Building. Suppose we focus only on the above mentioned concepts.


<img width="568" alt="Image_vespa" src="https://user-images.githubusercontent.com/25593410/54939550-25539980-4f29-11e9-986b-08d88e371506.png">


The visual and textual mentions of a man shown in red refer to the same entity, and they should be linked together. The other visual mention of a man, should be linked to another differnt entity. These two entities are not known, and therefore two new entities of type man should be added to the knowledge base, i.e., the A-box of K should be extended with the assertions Man (e_new1) and Man(e_new2). The textual and visual mentions of Vespa are also referring to the same entity. However, this time the entity is known (i.e., YAGO contains an entity for Vespa) and therefore the two mentions should be linked to the same entity. The other visual mentions should be linked to new entities, with the correct type, i.e., we should add the assertions bicycle(e_new3), building(e_new4). For the other textual mentions, i.e., Milan, Italy, 1948, we already have instances in the knowledge base, so we have to link them to these entities.

In the following example, an image from Flickr30k dataset with corresponding captions (C0,C1,C2,C3 and C4) is shwon. Our representation of VTKL dataset is shwon in button diagram (blue color respresent Flickr30k annotations and Orange color respresent PIKES annotations). These informations are for entity mention #man. Similarly one can consider for all entities mentions of Flickr30k dataset by using VTKL dataset. Entity mention #man is described in caption (C0 and C2) with their respective information in blue and orang color.


<img width="410" alt="image_info" src="https://user-images.githubusercontent.com/25593410/54940311-ca22a680-4f2a-11e9-8366-7ffa043d1dcf.png">


You can easily access our dataset for visual and textual enity recognition and linking for images by explring the master directory of this repositorty.
