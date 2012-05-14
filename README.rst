Introduction
============

This addon display a datatables_ showing @@sharing content of all content in the
site. It has been created to build reports of security settings.

How to install
==============

As any addons, so please follow official documentation_.

How to use
==========

Once the addon is installed you have a controlpanel that provide a direct
access to @@localrolesdatatables_catalog_view view where you can see every 
localroles of every content types. Because it use jquery datatbles you can
search and filter per content / users / content type.

This view use the portal_catalog, and build a query using the context path. So
if you want to have a report with only a folder (for an extranet) you just have
to call the view on this folder::

  mysite/extranet/@@localrolesdatatables_catalog_view

Credits
=======

Companies
---------

|cirb|_ CIRB / CIBG

* `Contact us <mailto:irisline@irisnet.be>`_


Authors

- JeanMichel FRANCOIS aka toutpt <toutpt@gmail.com>

.. Contributors

.. |cirb| image:: http://www.cirb.irisnet.be/logo.jpg
.. _cirb: http://cirb.irisnet.be
.. _datatables: http://datatables.net
.. _documentation: http://plone.org/documentation/kb/installing-add-ons-quick-how-to
