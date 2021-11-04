import streamlit as st
import math

st.title('SPHERE CALCULATOR')  
st.caption('built by Indra Yanto')
st.markdown('_**Can\'t remember how to calculate the sphere volume? Then this app is for you**_')
with st.container():
    '''
    ### Output Parameter 
    '''
    option=st.selectbox('Solve for:', ('Volume','Radius','Surface Area')) 
    if option=='Volume':
        '''
        ### Formula
        '''
        st.latex(r'''
                 V=\frac{4}{3}\,\pi\,r^3''')
        col1, col2 = st.columns(2)
        with col1:
            '''
            ### Input Value 
            '''
            inp=st.number_input('Enter value for Radius (r) :',min_value=0.000,value=1.000,step=1.000,format="%.3f")
        with col2:
            '''
            ### Output Value 
            '''
            st.metric(label="Volume (V) :", value=round(4*math.pi*(inp**3)/3,3), delta=None)
    elif option=='Radius':
        '''
        ### Formula
        '''
        st.latex(r'''
                 r=\left(\frac{3\,V}{4\,\pi}\right)^{1/3}''')
        col1, col2 = st.columns(2)
        with col1:
            '''
            ### Input Value 
            '''
            inp=st.number_input('Enter value for Volume (V) :',min_value=0.000,value=1.000,step=1.000,format="%.3f")
        with col2:
            '''
            ### Output Value 
            '''
            st.metric(label="Radius (r) :", value=round(((3*inp)/(4*math.pi))**(1/3),3), delta=None)
    elif option=='Surface Area':
        '''
        ### Formula
        '''
        st.latex(r'''
                 A=4\,\pi\,r^2''')
        col1, col2 = st.columns(2)
        with col1:
            '''
            ### Input Value 
            '''
            inp=st.number_input('Enter value for Radius (r) :',min_value=0.000,value=1.000,step=1.000,format="%.3f")
        with col2:
            '''
            ### Output Value 
            '''
            st.metric(label="Surface Area (A) :", value=round(4*math.pi*inp**2,3), delta=None)
