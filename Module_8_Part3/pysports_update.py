#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from sqlalchemy import create_engine

rds_connection_string = "postgres:///@localhost:5432/pysports"
engine = create_engine(f'postgresql://{rds_connection_string}')

rds_connection_string = "postgres:////@localhost:5432/pysports"
engine = create_engine(f'postgresql://{rds_connection_string}')


# In[ ]:




