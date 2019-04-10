## Visual-Textual-Knowledge Entity Linking (VTKEL) dataset
This repositroy includes **VTKEL** dataset and related files developed for ***visual-textual*** alignment with links to **YAGO ontology** for entity recognition and linking. 

### Introduction
VTKEL dataset, contains documents composed of pictures with five corresponding textual captions for each image. The VTKEL dataset is obtained by extending the **Flikr30k** dataset, designed for visual-textual mention alignment, with links to **YAGO ontolgy**, one of the largest *web knowledge base* extracted from Wikipedia, WordNet and GeoNames. These links are obtained automatically by processing each image caption with **PIKES**, an *NLP* tool for *entity recognition* and *linking*. 


To understand VTKEL dataset consider the document shown in below Figure, which is composed of one picture and a short sentence (caption) in natural language. From below figure, one can find five visual mentions, shown in coloured rectangles in the picture, and five textual mention, underlined in the text. One could find many more visual mention in the picture, e.g., windows, road, etc. but suppose we are only intersted in the mentions of certain types. Let us consider a *knowledge base* (e.g. YAGO) that contains knowledge about the named entities e<sup>Vespa</sup>, e<sup>Milan</sup>, e<sup>Italy</sup>, and e<sup>1948</sup> for *Vespa*, *Milan*, *Italy* and *1948* respectively. E.g., *scooter (e<sup>Vespa</sup>)*, *town (e<sup>Milan</sup>), country (e<sup>Italy</sup>)*, and *year (e<sup>1948</sup>)*. Suppose also that the *knowledge base* contains the concepts *Man*, and *Building*. Suppose we focus only on the above mentioned concepts.


<img width="568" alt="Image_vespa" src="https://user-images.githubusercontent.com/25593410/54939550-25539980-4f29-11e9-986b-08d88e371506.png">


The visual and textual mentions of a man shown in red refer to the same entity, and they should be linked together. The other visual mention of a man, should be linked to another differnt entity. These two entities are not known, and therefore two new entities of type man should be added to the knowledge base, i.e., the *A-box* of *K* should be extended with the assertions *Man (e<sup>new1</sup>)* and *Man(e<sup>new2</sup>)*. The textual and visual mentions of *Vespa* are also referring to the same entity. However, this time the entity is known (i.e., **YAGO** contains an entity for *Vespa*) and therefore the two mentions should be linked to the same entity. The other visual mentions should be linked to new entities, with the correct type, i.e., we should add the assertions *bicycle(e<sup>new3</sup>)*, *building(e<sup>new4</sup>)*. For the other textual mentions, i.e., *Milan*, *Italy*, *1948*, we already have instances in the *knowledge base*, so we have to link them to these entities.

In the following example, an image from **Flickr30k** dataset with the corresponding captions *(C0,C1,C2,C3 and C4)* is shwon. Our representation of **VTKEL dataset** is shwon in button graph (blue color respresent *Flickr30k annotations* and Orange color respresent *PIKES annotations*). The example shows the informations for entity mention *#man*. Similarly one can consider for all entities mentions in Flickr30k dataset by exploiting VTKEL dataset. Entity mention *#man* is described in caption *(C0 and C2)* with their respective graph information in blue and orang colors.


<img width="810" alt="image_info" src="https://user-images.githubusercontent.com/25593410/54940311-ca22a680-4f2a-11e9-8366-7ffa043d1dcf.png">

You can easily access our dataset for *visual* and *textual enity recognition* and *linking* for Flickr30k images.

For indepth information and exploring VTKEL dataset, explore the directories, files and follow the running commands described below.

### Folders:
1. ***Example*** This directory consist of a single entry(document) of VTKEL dataset process by PIKES with Flickr30k files.
2. ***PIKES_annotations*** This directory consists of python script to extract entity mentions process by PIKES for entity recognition and linking.
3. ***flickr30k annotation*** This directory consists of Flickr30k annotations with python script for extracting visual and textual information of the original Flickr30k.

### Files:
1. **VTKEL error free (300 documents).ttl** This file consists of VTKEL dataset for 300 randomly selected entries for VTKEL task. We manually checked the entity mentions for 300 randomly selected entries(documents) and fixed each incorrect mention process by PIKES. We prodcued this gold standard subset of VTEKL dataset for the development of unsupervised and supervised algorithms for solving the VTKEL task.
2. **Incorrect NER and linking mention.xlsx** This file consists of all error cases which are wrongly process by PIKES for entity recognition and linking.
3. [VTKEL](https://figshare.com/articles/VTKL_dataset_file/7882781) dataset for 31781 images.

### Prerequisites:
- Python 3.6 (+) or 2.7(+)
- window or unix machine
- rdflib library 4.2.2
- numpy library 1.16.0
- xml.etree.ElementTree library

### Running VTKEL dataset:
1. Download VTKEL dataset from *300 images dataset* file or the link provided for VTKEL dataset (i.e. VTKEL).
2. Update the file path of ***pikes_annotations.py*** in ***PIKES annotations***.
3. Run *pikes_annotations.py* by using the command:
```
> python pikes_annotations.py
```
3. Download files from ***flickr30k annotations*** .
4. Update file path of ***flickr_annotations.py*** in ***flickr30k annotations*** .
5. Run *flickr_annotations.py* by using the command:
```
> python flickr_annotations.py
```
### Quality of VTKEL dataset:
We checked and calculate the quality of VTKEL dataset by exploiting manually checking 4585 mentions of randomly selected 300 entries(documents), which amounts to an accuracy of **96.5%**.

## Citing VTKEL dataset:
If you use the data, code or concepts of VTKEL in your research work, please cite:
```
@article{Dost2019,
      author = "Shahi Dost and Luciano Serafini and Marco Rospocher and Lamberto Ballan and Alessandro Sperduti",
      title = "{VTKEL: A resource for  Visual-Textual-Knowledge Entity Linking}",
      year = "2019",
      month = "4",
      url = "https://figshare.com/articles/VTKL_dataset_file/7882781",
      doi = "10.6084/m9.figshare.7882781.v4"
}
```
### License:
The VTKEL dataset and their codes are licensed under **CC BY 4.0**.
### Contributors:
- [Luciano Serafini](https://dkm.fbk.eu/people/profile/serafini)
- [Alessandro Sperduti](https://www.math.unipd.it/~sperduti/)
- [Marco Rospocher](https://scholar.google.com/citations?user=wkAcWjMAAAAJ&hl=en)
- [Lamberto Ballan](http://www.lambertoballan.net/)
### References:
- [Flickr30k](http://slazebni.cs.illinois.edu/publications/ijcv16_flickr30k.pdf)
- [PIKES](http://pikes.fbk.eu)
- [YAGO](https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/yago-naga/yago/)


### Contact
If you have any query regarding VTKEL dataset, code, want to contribute to VTKEL dataset, or VTKEL task contact on ***sdost[at]fbk.eu***.
