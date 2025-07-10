###################
``Basic Usage``
###################


:octicon:`telescope;1em` Providing Observations
===============================================

The first step is to create a ``PhaseCurve`` instance, representing the observed polarimetric phase curve
of the target. In its simplest form, this consists of providing a list of ``phase`` (in degrees)
and a list of ``pol`` to the ``PhaseCurve``.

.. code-block:: python

   from phunk import PhaseCurve

   phase = [14.4, 18.5, 19.9, 23.7]
   pol = [-1.63, -1.25, -1.14, -0.65]
   
   pc = PhaseCurve(phase=phase, pol=pol)
   
.. Note::

   Where applicable, ``polka`` expects values to be in degrees rather than radians.


:octicon:`file-symlink-file;1em` Referencing observation
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

You can pass information about the observations to the ``PhaseCurve`` class using the ``src`` argument,
which should be a list which defines the source of each observation.

.. code-block:: python

   from phunk import PhaseCurve

   phase = [14.4, 18.5, 19.9, 23.7]
   pol = [-1.63, -1.25, -1.14, -0.65]
   src = ["Cellino+2005", "Cellino+2005", "Cellino+2005", "Cellino+2005"]]

   pc = PhaseCurve(phase=phase, pol=pol, src=src)

At any point, you can check the sources of your observations using the ``src`` attribute of the ``PhaseCurve`` object.

.. code-block:: python

   >>> pc.src
   ['Cellino+2005', 'Cellino+2005', 'Cellino+2005', 'Cellino+2005']
   

:octicon:`issue-reopened;1em` Computing Ephemerides
+++++++++++++++++++++

If you do not have the ``phase`` angle , ``polka``
can query the required values for you from the
`LTE <https://lte.observatoiredeparis.psl.eu/>`_'s `Miriade <https://ssp.imcce.fr/webservices/miriade/>`_ webservice.
For this, you have to specify the ``epoch`` of observation in :term:`JD<Julian date (JD)>` format and an identifier of your target.
``polka`` uses `rocks <https://rocks.readthedocs.io>`_ of 
`SsODNet <https://ssp.imcce.fr/webservices/ssodnet/>`_ 
(`Berthier et al. 2023 <https://ui.adsabs.harvard.edu/abs/2023A&A...671A.151B/abstract>`_)
to resolve target identities.


.. code-block:: python

   from polka import PhaseCurve

   epoch = [2452709.5660, 2450638.5964, 2450570.7753, 2453184.5245]
   pol = [-1.63, -1.25, -1.14, -0.65]

   pc = PhaseCurve(mag=mag, epoch=epoch, target="barbara")
   pc.get_ephems()



You can then access the :term:`phase angle<Phase angle>` of your observations using the ``phase``
attribute of the ``PhaseCurve`` object:

.. code-block:: python

   >>> pc.phase
   [14.4, 18.5, 19.9, 23.7]



:octicon:`sliders;1em` Fitting Models
==============

To fit one of the available :ref:`polarimetric models <models>`, use the ``.fit`` method of the ``PhaseCurve``
and provide a list of models to fit.

.. code-block:: python

   pc.fit(["LinExp"])

If you don't provide any argument, ``polka`` will fit all implemented models.


.. Note::

   You need the :term:`phase angle<Phase angle>` to be given to ``PhaseCurve`` object before you can ``fit`` the model.


Datapoints can be weighted by providing the ``weights`` argument.

.. code-block:: python

   pc.fit(["LinExp"], weights=1/pol_err**2)

Once the models have been fit, you can access the model parameters as attributes of
the ``PhaseCurve`` via the dot notation.

.. code-block:: python

   pc.LinExp.a
   pc.LinExp.alpha_inv
   pc.LinExp.pol_min

All available model attributes are given in the model description.


:octicon:`graph;1em` Plotting Curves
===============

Use the ``.plot`` method of the ``PhaseCurve`` class to plot phase curves.
You can select which models to add to the plot using the ``models`` argument.
The plot will open in an interactive window by default. Provide a path to the ``save``
argument to save the plot under the specified path.

You can highlight the sources of the observations by setting the ``label_sources`` argument to ``True``.
You can also choose to show the model parameters in the plot by setting the ``show_parameters`` argument to ``True``.
Finally, you can set the ``black`` argument to ``True`` to use a dark background for the plot.

.. code-block:: python

   pc.plot()
   pc.plot(models=["LinExp"])
   pc.plot(models=["LinExp"], save="barbara.png")

   pc.plot(models=["LinExp"], show_parameters=True, black=True)

   pc.plot(models=["LinExp"], show_parameters=True, label_sources=True))

.. Note::

   You need to ``fit`` a model before you can ``plot`` it.
