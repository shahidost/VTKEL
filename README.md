## Visual-Textual-Knowledge Entity Linking (VTKL) dataset
### Introduction
VTKL dataset, contains documents composed of pictures with five corresponding textual captions for each image. The VTKL dataset is obtained by extending the **Flikr30k** dataset, designed for visual-textual mention alignment, with links to **YAGO ontolgy**, one of the largest *web knowledge base*. These links are obtained automatically by processing each image caption with **PIKES**, an *NLP* tool for *entity recognition* and *linking*. 


To understand VTKL dataset consider the documents shown in below Figure, which is composed of one picture and a short sentence (caption) in natural language. From below figure, one can find five visual mentions, shown in coloured rectangles in the picture, and five textual mention, underlined in the text. Of course one could find many more visual mention in the picture, e.g., windows, road, etc. but suppose we are only intersted in the mentions of certain types. Let us consider a *knowledge base* (e.g. YAGO) that contains knowledge about the named entities e<sup>Vespa</sup>, e<sup>Milan</sup>, e<sup>Italy</sup>, and e<sup>1948</sup> for *Vespa*, *Milan*, *Italy* and *1948* respectively. E.g., *scooter (e<sup>Vespa</sup>)*, *town (e<sup>Milan</sup>), country (e<sup>Italy</sup>)*, and *year (e<sup>1948</sup>)*. Suppose also that the *knowledge base* contains the concepts *Man*, and *Building*. Suppose we focus only on the above mentioned concepts.


<img width="568" alt="Image_vespa" src="https://user-images.githubusercontent.com/25593410/54939550-25539980-4f29-11e9-986b-08d88e371506.png">


The visual and textual mentions of a man shown in red refer to the same entity, and they should be linked together. The other visual mention of a man, should be linked to another differnt entity. These two entities are not known, and therefore two new entities of type man should be added to the knowledge base, i.e., the *A-box* of *K* should be extended with the assertions *Man (e<sup>new1</sup>)* and *Man(e<sup>new2</sup>)*. The textual and visual mentions of *Vespa* are also referring to the same entity. However, this time the entity is known (i.e., **YAGO** contains an entity for *Vespa*) and therefore the two mentions should be linked to the same entity. The other visual mentions should be linked to new entities, with the correct type, i.e., we should add the assertions *bicycle(e<sup>new3</sup>)*, *building(e<sup>new4</sup>)*. For the other textual mentions, i.e., *Milan*, *Italy*, *1948*, we already have instances in the *knowledge base*, so we have to link them to these entities.

In the following example, an image from **Flickr30k** dataset with corresponding captions *(C0,C1,C2,C3 and C4)* is shwon. Our representation of **VTKL dataset** is shwon in button graph (blue color respresent *Flickr30k annotations* and Orange color respresent *PIKES annotations*). The example shows the informations for entity mention *#man*. Similarly one can consider for all entities mentions in Flickr30k dataset by exploiting VTKL dataset. Entity mention *#man* is described in caption *(C0 and C2)* with their respective graph information in blue and orang color.


<img width="810" alt="image_info" src="https://user-images.githubusercontent.com/25593410/54940311-ca22a680-4f2a-11e9-8366-7ffa043d1dcf.png">

You can easily access our dataset for *visual* and *textual enity recognition* and *linking* for Flickr30k images.

For indepth information and exploring VTKL dataset, explore the directories, files and follow the running commands described below.

### Folders:
1. ***Example*** consist of a single entry of VTKL dataset process by PIKES with Flickr30k files.
2. ***PIKES_annotations*** consist of python script to extract entity mentions process by PIKES for entity recognition and linking.
3. ***flickr30k annotation*** consist of flickr annotations and python script for extracting visual and textual information of original Flickr30k.

### Files:
1. **300 random images for evaluations -error_free.ttl** consists of VTKL dataset for 300 randomly selected entries for VTKEL task. The error of these 300 images dataset are fixed manually by selecting each incorrect mention process by PIKES.
2. **Incorrect NER and linking mention.xlsx** consists of all error cases which are wrongly process by PIKES for NER and entites linking for VTKL dataset and the results of our evaluation.
3. [VTKL](https://figshare.com/account/projects/61421/articles/7882781) dataset for 31781 images.

### Prerequisites:
- Python 3.6(+)
- window or unix machine
- rdflib library
- numpy library
- xml.etree.ElementTree library

### Running VTKL dataset:
1. Download VTKL dataset from *300 images dataset* file or the link provided (i.e. VTKL).
2. Update file path of ***pikes_annotations.py*** in ***PIKES annotations***.
3. Run *pikes_annotations.py* by using command:
```
> python pikes_annotations.py
```
3. Download files from ***flickr30k annotations*** .
4. Update file path of ***flickr_annotations.py*** in ***flickr30k annotations*** .
5. Run *flickr_annotations.py* by using command:
```
> python flickr_annotations.py
```
### Quality of VTKL dataset:
We checked and calculate the quality of VTKL dataset by exploiting manually for 4585 mentions of randomly selected 300 entries, which is **96.5%**.

## Citing VTKL dataset
If you use the data, code or concepts of VTKEL in your research work, please cite:
```
TBW {@ABC{VTKL,
      author    = {ABC},
      title     = {{ABC}},
      ABC = {ABC},
      pages     = {000--000},
      year      = {2019}
    }}
```
### License
The VTKL dataset and their codes are licensed under GNU General Public License, version 3 or later.
### References:
- [Flickr30k](http://slazebni.cs.illinois.edu/publications/ijcv16_flickr30k.pdf)
- [PIKES](http://pikes.fbk.eu)
- [YAGO](https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/yago-naga/yago/)


### Contact
If you have any query regarding VTKL or codes or want to contribute to VTKL dataset or VTKEL task contact on *shahidost[at]gmail.com*.
