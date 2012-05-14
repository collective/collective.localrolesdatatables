Introduction
============

This addon display a datatables_ showing @@sharing content of all content in the
site. It has been created to build reports of security settings.

How to install
==============

As any addons, so please follow official documentation_. By the way this
addon add an index to the portal_catalog, so you have to reindex this index.
To achieve this go to http://mysite/portal_catalog/manage_catalogIndexes
check the 'hasLocalRoles' index and push Reindex button.

How to use
==========

Once the addon is installed you have a @@localrolesdatatables_catalog_view
view where you can see every localroles of every content types. Because it use
jquery datatbles you can search and filter per content / users.

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
