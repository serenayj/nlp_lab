---
# Leave the homepage title empty to use the site title
title:
date: 2024-05-04
type: landing

sections:
  - block: hero
    content:
       title: |
            Welcome to the LAnguage, Reasoning, and Knowledge (LARK) Lab 
       text: <p> We are a research group within <a href="https://medschool.cuanschutz.edu/dbmi">Department of Biomedical Informatics, University of Colorado, Anschutz Campus</a>, led by <a href="https://serenayj.github.io/">Dr. Yanjun Gao</a>. By developing foundational technologies and conducting cutting-edge research in natural language processing (NLP) with innovative artificial intelligence (AI), the lab is dedicated to creating powerful tools that tackle critical healthcare challenges and integrate seamlessly into healthcare systems. </p> 
       image:
          filename: dbmi_new_lark.png  

  - block: markdown
    content:
      title: Openings 
      subtitle:
      text: |
         As the first NLP research lab at CU-Anschutz, we are currently seeking passionate individuals eager to make a significant impact on NLP and AI in health, with openings available for Postdoctoral Researchers, PhD Students, Data Scientists, and Research Interns. If you are interested in being part of us, apply here: [link](https://forms.gle/DWRmJ86RERBgqqVz9)!  
    
    design:
      columns: '1'
  
  - block: collection
    content:
      title: Latest News # under post
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: card
      columns: '1'
  
  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---
