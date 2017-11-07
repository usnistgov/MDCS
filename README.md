# Materials Data Curation System

The NIST Materials Data Curation System (MDCS) provides a means for capturing, sharing, and transforming materials data
into a structured format that is XML based amenable to transformation to other formats. The data are organized using
user-selected templates encoded in XML Schema. These templates are used to create data entry forms. The documents are
saved in a non-relational (NoSQL) database, namely MongoDB. The data can be searched and retrieved by a template-driven
web-based form or by a RESTful API call. The system also enables the interconnection of MDCS repositories for federated
searches.

The software was developed by the National Institute of Standards and Technology (NIST)

# Disclaimer 

The XML-based schemas provided with the Materials Data Curator are examples of schemas that may be written to represent
different aspects of materials data and to demonstrate some of the features that may be used within an XML schema (i.e.
including tabular data or composition selection using the periodic table). The schemas do not represent “standard”
metadata representations and are specifically release as “as is,” and as such NIST makes no warrant of any kind on the
correctness or accuracy of the content of the schemas, nor the fitness of the schemas for any purpose and accepts any
liability or responsibility for the consequences of the schemas use or misuse by anyone.

Note the Demo-Diffusion data schema is not meant as a metadata standard for diffusion data. It is just an example of
how one might specify some of the metadata associated with typical tracer, intrinsic and chemical (interdiffusion)
diffusivity experiments. This schema can be customized to fit the users’ needs. It should also be noted that while the
Demo-Diffusion schema contains some instruments types (e.g Electron Probe Micro Analyzer or a microtome) not all the
appropriate metadata for each instrument has been defined nor have all of the appropriate instrument types been defined.

Also note that not all XML-schemas will load properly within the Materials Data Curator.
