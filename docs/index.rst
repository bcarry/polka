#########
``polka``
#########

.. raw:: html

    <style> .gray {color:#979eab} </style>

.. role:: gray

A ``python`` package to fit polarimetruc phase curves of asteroids.

.. highlight:: python

.. code-block:: python

   import polka

Collect the polarimetry of your favourite asteroid under varying phase angles.

.. code-block:: python

   # Observations 
   phase = [0.57, 1.09, 3.20, 10.99, 14.69, 20.42]
   pol = [6.555, 6.646, 6.793, 7.130, 7.210, 7.414]

Load the observations into ``polka``.

.. code-block:: python

   pc = polka.PhaseCurve(phase=phase, pol=pol)

Fit the traditionnal linear-exponential model to the observations.

.. code-block:: python

   pc.fit()
   pc.plot()



.. toctree::
   :maxdepth: 2
   :caption: Contents
   :hidden:

   Home<self>
   Getting Started<getting_started>
   Basic Usage<core>
   Models<models>


