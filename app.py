import os, json
import streamlit.components.v1 as components

from pollination_streamlit_io import (get_geometry, get_hbjson, send_geometry, send_hbjson, get_host)

import streamlit as st

st.header("Pollination-Streamlit-IO")

host = get_host()

st.header("Host: " + host)

st.subheader('Get geometry')

# rg = received geometry
rg_col1, rg_col2 = st.columns(2)

with rg_col1:
    geometry = get_geometry('get-geometry')
    st.info('The get_geometry component gets geometry from the host CAD environment and returns a dictionary of objects. It can be configured to work either by user selection or through a continuous subscription to geometry in the CAD environment.')
with rg_col2:
    st.json(geometry, expanded=False)

st.subheader('Get hbjson')

# rh = received hbjson
rh_col1, rh_col2 = st.columns(2)

with rh_col1:
    hbjson = get_hbjson('get-hbjson')
    st.info('The get_hbjson component gets an hbjson model from the host CAD environment and returns the hbjson as a json document. It can be configured to work either by user selection or through a continuous subscription to the hbjson model in the CAD environment.')
with rh_col2:
    st.json(hbjson, expanded=False)

st.subheader('Send geometry')

# sg = sent geometry
sg_col1, sg_col2 = st.columns(2)

geometry_file = open(os.getcwd() + '/sample-assets/geometry.json')
geometry_to_send = json.load(geometry_file)

with sg_col1:
    sent_geometry = send_geometry('send-geometry', geometry=geometry_to_send)
    st.info('The get_hbjson component gets an hbjson model from the host CAD environment and returns the hbjson as a json document. It can be configured to work either by user selection or through a continuous subscription to the hbjson model in the CAD environment.')

with sg_col2:
    st.text(os.getcwd() + '/sample-assets/single-family-home.hbjson')
    st.json(geometry_to_send, expanded=False)

st.subheader('Send hbjson')

# sh = sent hbjson
sh_col1, sh_col2 = st.columns(2)

hbjson_file = open(os.getcwd() + '/sample-assets/single-family-home.hbjson')
hbjson_to_send = json.load(hbjson_file)

with sh_col1:
    sent_hbjson = send_hbjson('send-hbjson', hbjson=hbjson_to_send)
    st.info('The get_hbjson component gets an hbjson model from the host CAD environment and returns the hbjson as a json document. It can be configured to work either by user selection or through a continuous subscription to the hbjson model in the CAD environment.')

with sh_col2:
    st.text(os.getcwd() + '/sample-assets/single-family-home.hbjson')
    st.json(hbjson_to_send, expanded=False)
