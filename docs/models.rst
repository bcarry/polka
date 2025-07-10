.. _models:

####################
``Models``
####################

.. raw:: html

    <style> .gray {color:#979eab} </style>

.. role:: gray


.. |br| raw:: html

     <br>

.. highlight:: python



|br|

.. _LinExp: 

:octicon:`light-bulb;1em` Linear-exponential model
==================================================

The linear-exponential model is an empirical model describing the polarization of light
reflected from a surface as function of the phase angle. It was defined by 
`Muinonen et al. (2002) <https://ui.adsabs.harvard.edu/abs/2002MmSAI..73..716M/abstract>`_.
In POLKA, we use the reformulation by
`Devogèle et al. (2017) <https://ui.adsabs.harvard.edu/abs/2017MNRAS.465.4335D/abstract>`_:

.. math ::
    P_r = a \left( e^{-\alpha/b} -1 \right) + c \alpha



